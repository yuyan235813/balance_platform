#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.permission_setup import Ui_permissionSetupForm
from ui.user_manage import Ui_Form
from ui.role_manage import Ui_roleForm
from utils.sqllite_util import EasySqlite
from functools import partial
from utils import normal_utils
import logging


class PermissionSetupForm(QtWidgets.QWidget, Ui_permissionSetupForm):
    """
    车辆管理
    """
    permission_changed = pyqtSignal(bool)

    def __init__(self, parent):
        super(PermissionSetupForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.parent = parent
        self.savePushButton.clicked.connect(self.__save_data)
        self.cancelPushButton.clicked.connect(self.close)
        self.addUserPushButton.clicked.connect(self.__add_user)
        self.addRolePushButton.clicked.connect(self.__add_role)
        self.editUserPushButton.clicked.connect(self.__change_user)
        self.deleteUserPushButton.clicked.connect(self.__delete_user)
        self.deleteRolePushButton.clicked.connect(self.__delete_role)
        self.userMangeForm = UserManageForm()
        self.userMangeForm.my_signal.connect(self.__init_data)
        self.roleManageForm = RoleManageForm()
        self.roleManageForm.my_signal.connect(self.__init_data)
        self.optionTableView.doubleClicked.connect(partial(self.__change_permissions, 1))
        self.permissionTableView.doubleClicked.connect(partial(self.__change_permissions, 2))
        self.superLabel.doubleClicked.connect(self.__manage_permissions)

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        self.flag = ''
        # 用户
        self.userListWidget.clear()
        self.roleListWidget.clear()
        user_sql = 'select user_id, user_name from t_user where status = 1 order by id;'
        user_ret = self.db.query(user_sql)
        user_item = []
        row_no = 0
        for idx, item in enumerate(user_ret):
            user_item.append(item.get('user_name'))
            if self.parent.user_name == item.get('user_name'):
                row_no = idx
        self.userListWidget.addItems(user_item)
        self.userListWidget.setCurrentRow(row_no)
        # 角色
        role_sql = 'select id, role_name from t_role where status = 1 order by id;'
        role_ret = self.db.query(role_sql)
        role_item = []
        for item in role_ret:
            role_item.append(item.get('role_name'))
        self.roleListWidget.addItems(role_item)
        self.userListWidget.itemClicked.connect(self.__show_user_permissions)
        self.roleListWidget.itemClicked.connect(self.__show_role_permissions)
        model = QStandardItemModel(1, 2)
        model.setHorizontalHeaderLabels(('允许', '功能名称'))
        self.permissionTableView.setModel(model)
        model.setHorizontalHeaderLabels(('允许', '菜单名称'))
        self.optionTableView.setModel(model)
        # 初始化用户权限
        self.__show_user_permissions(self.parent.user_name)

    def show(self):
        """
        显示界面
        :return:
        """
        super().show()
        self.__init_data()

    def __show_user_permissions(self, model):
        """
        显示用户权限
        :param model:
        :return:
        """
        if isinstance(model, str):
            self.user_name = model
        else:
            self.user_name = model.text()
        self.role_name = ''
        #　or (a.role_id = b.object_id and b.object_type = 1)
        sql_tmp = """
            select t1.opt_type, opt_name, case when t2.operation_id is null then 0 else 1 end as has_permission
            from
            (select opt_type, opt_name, id from t_operation where status = 1) t1
            left join
            (select operation_id from (select user_id, role_id from t_user where user_name = '%s' and status = 1) a 
                join t_permission b 
                on (a.user_id = b.object_id and b.object_type = 2) 
                where b.status = 1
                group by operation_id
            ) t2 on t1.id = t2.operation_id"""
        sql = sql_tmp % self.user_name
        ret = self.db.query(sql)
        opt_item = []
        permission_item = []
        for item in ret:
            row_data = ('√' if item.get('has_permission') else 'X', item.get('opt_name'))
            if item.get('opt_type') == 1:
                opt_item.append(row_data)
            else:
                permission_item.append(row_data)
        model = QStandardItemModel(len(opt_item), 2)
        model.setHorizontalHeaderLabels(('允许', '菜单名称'))
        for row in range(len(opt_item)):
            for col in range(2):
                item = QStandardItem(opt_item[row][col])
                model.setItem(row, col, item)
        self.optionTableView.setModel(model)

        model = QStandardItemModel(len(permission_item), 2)
        model.setHorizontalHeaderLabels(('允许', '功能名称'))
        for row in range(len(permission_item)):
            for col in range(2):
                item = QStandardItem(permission_item[row][col])
                model.setItem(row, col, item)
        self.permissionTableView.setModel(model)
        if "系统管理员" == self.parent.user_name:
            self.permissionTableView.setEnabled(True)
            self.optionTableView.setEnabled(True)
        else:
            self.permissionTableView.setEnabled(False)
            self.optionTableView.setEnabled(False)

    def __show_role_permissions(self, model):
        """
        显示角色权限
        :param model:
        :return:
        """
        self.user_name = ''
        self.role_name = model.text()
        sql_tmp = """
                    select t1.opt_type, opt_name, case when t2.object_id is null then 0 else 1 end as has_permission
                    from
                    (select opt_type, opt_name, id from t_operation where status = 1) t1
                    left join
                    (select * from (select id as role_id from t_role where role_name = '%s' and status = 1) a 
                        join t_permission b 
                        on a.role_id = b.object_id and b.object_type = 1 and b.status = 1
                    ) t2 on t1.id = t2.operation_id"""
        sql = sql_tmp % self.role_name
        ret = self.db.query(sql)
        opt_item = []
        permission_item = []
        for item in ret:
            row_data = ('√' if item.get('has_permission') else 'X', item.get('opt_name'))
            if item.get('opt_type') == 1:
                opt_item.append(row_data)
            else:
                permission_item.append(row_data)
        model = QStandardItemModel(len(opt_item), 2)
        model.setHorizontalHeaderLabels(('允许', '菜单名称'))
        for row in range(len(opt_item)):
            for col in range(2):
                item = QStandardItem(opt_item[row][col])
                model.setItem(row, col, item)
        self.optionTableView.setModel(model)

        model = QStandardItemModel(len(permission_item), 2)
        model.setHorizontalHeaderLabels(('允许', '功能名称'))
        for row in range(len(permission_item)):
            for col in range(2):
                item = QStandardItem(permission_item[row][col])
                model.setItem(row, col, item)
        self.permissionTableView.setModel(model)
        if "系统管理员" == self.parent.user_name:
            self.permissionTableView.setEnabled(True)
            self.optionTableView.setEnabled(True)
        else:
            self.permissionTableView.setEnabled(False)
            self.optionTableView.setEnabled(False)

    def __change_permissions(self, type, index):
        """
        更新权限设置
        :return:
        """
        row = index.row()
        if type == 1:
            index = self.optionTableView.model().index(row, 0)
            has_permission = '√' if 'X' == self.optionTableView.model().data(index) else 'X'
            self.optionTableView.model().setData(index, has_permission)
        else:
            index = self.permissionTableView.model().index(row, 0)
            has_permission = '√' if 'X' == self.permissionTableView.model().data(index) else 'X'
            self.permissionTableView.model().setData(index, has_permission)

    def __save_data(self):
        """
        保存权限
        :return:
        """
        # 保存功能
        model = self.optionTableView.model()
        row = model.rowCount()
        for i in range(row):
            has_permission = 0 if model.data(model.index(i, 0)) == 'X' else 1
            opt_name = model.data(model.index(i, 1))
            if self.user_name:
                sql = """update t_permission set status = %s where object_type = 2
                        and operation_id = (select id from t_operation where opt_name = '%s')
                        and object_id = (select user_id from t_user where user_name = '%s')
                        """ % (has_permission, opt_name, self.user_name)
                self.db.update(sql, commit=False)
            if self.role_name:
                sql = """update t_permission set status = %s where object_type = 1
                                        and operation_id = (select id from t_operation where opt_name = '%s')
                                        and object_id = (select id from t_role where role_name = '%s')
                                        """ % (has_permission, opt_name, self.role_name)
                self.db.update(sql, commit=False)
        # 保存功能
        model = self.permissionTableView.model()
        row = model.rowCount()
        for i in range(row):
            has_permission = 0 if model.data(model.index(i, 0)) == 'X' else 1
            opt_name = model.data(model.index(i, 1))
            if self.user_name:
                sql = """update t_permission set status = %s where object_type = 2
                        and operation_id = (select id from t_operation where opt_name = '%s')
                        and object_id = (select user_id from t_user where user_name = '%s')
                        """ % (has_permission, opt_name, self.user_name)
                self.db.update(sql, commit=False)
            if self.role_name:
                sql = """update t_permission set status = %s where object_type = 1
                                        and operation_id = (select id from t_operation where opt_name = '%s')
                                        and object_id = (select id from t_role where role_name = '%s')
                                        """ % (has_permission, opt_name, self.role_name)
                self.db.update(sql, commit=False)
        ret = self.db.update('')
        if ret:
            self.permission_changed.emit(True)
            QtWidgets.QMessageBox.information(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)

    def __add_user(self):
        """
        添加用户
        :return:
        """
        if "系统管理员" == self.parent.user_name:
            self.userMangeForm.show(0)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "您没有添加角色的权限！", QtWidgets.QMessageBox.Ok)
            return

    def __add_role(self):
        """
        添加用户
        :return:
        """
        if "系统管理员" == self.parent.user_name:
            self.roleManageForm.show()
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "您没有添加角色的权限！", QtWidgets.QMessageBox.Ok)
            return

    def __change_user(self):
        """
        更改用户
        :param model:
        :return:
        """
        if not self.userListWidget.currentItem():
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要修改的用户！", QtWidgets.QMessageBox.Ok)
            return
        user_name = self.userListWidget.currentItem().text()
        if not ("系统管理员" == self.parent.user_name or self.user_name == self.parent.user_name):
            QtWidgets.QMessageBox.warning(self, '本程序', "此用户不能被修改！", QtWidgets.QMessageBox.Ok)
            return
        self.userMangeForm.show(user_name)

    def __delete_user(self):
        """
        添加用户
        :return:
        """
        if not self.userListWidget.currentItem():
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的用户！", QtWidgets.QMessageBox.Ok)
            return
        user_name = self.userListWidget.currentItem().text()
        if "系统管理员" != self.parent.user_name or user_name == "系统管理员":
            QtWidgets.QMessageBox.warning(self, '本程序', "此用户不能被删除！", QtWidgets.QMessageBox.Ok)
            return
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要删除用户 %s？" % user_name,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sql = """delete from t_permission where object_id in (select user_id from t_user where user_name = '%s') 
                                 and object_type = 2;""" % user_name
            self.db.update(sql, commit=False)
            sql2 = "delete from t_user where user_name = '%s'" % user_name
            ret = self.db.update(sql2)
            if ret:
                QtWidgets.QMessageBox.warning(self, '本程序', "删除成功！", QtWidgets.QMessageBox.Ok)
                self.__init_data()
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "删除失败！", QtWidgets.QMessageBox.Ok)
        else:
            return

    def __delete_role(self):
        """
        删除角色
        :return:
        """
        if not self.roleListWidget.currentItem():
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的角色！", QtWidgets.QMessageBox.Ok)
            return
        role_name = self.roleListWidget.currentItem().text()
        if "系统管理员" != self.parent.user_name:
            QtWidgets.QMessageBox.warning(self, '本程序', "您没有删除角色权限！", QtWidgets.QMessageBox.Ok)
            return
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要删除角色 %s？" % role_name,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            query_sql = """select * from t_user a join t_role b on a.role_id = b.id where b.role_name = '%s'""" % role_name
            query_ret = self.db.query(query_sql)
            if query_ret:
                QtWidgets.QMessageBox.warning(self, '本程序', "该角色下有用户存在，不允许删除！", QtWidgets.QMessageBox.Ok)
                return
            sql = """delete from t_permission where object_id in (select id from t_role where role_name = '%s') 
                     and object_type = 1;""" % role_name
            self.db.update(sql, commit=False)
            sql2 = """delete from t_role where role_name = '%s';""" % role_name
            ret = self.db.update(sql2, commit=True)
            if ret:
                QtWidgets.QMessageBox.warning(self, '本程序', "删除成功！", QtWidgets.QMessageBox.Ok)
                self.__init_data()
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "删除失败！", QtWidgets.QMessageBox.Ok)
        else:
            return

    def __manage_permissions(self):
        """
        管理权限
        :return:
        """
        pass


class UserManageForm(QtWidgets.QWidget, Ui_Form):
    """
    用户管理
    """
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(UserManageForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.savePushButton.clicked.connect(self.__save_data)
        self.cancelPushButton.clicked.connect(self.close)
        self.user_id = 0
        self.password = -1

    def show(self, user_name):
        """
        展示界面
        :return:
        """
        super().show()
        sql = "select role_name from t_role where status = 1"
        ret=self.db.query(sql, result_dict=False)
        if ret:
            role_list = list(list(zip(*ret))[0])
            self.roleComboBox.clear()
            self.roleComboBox.addItems(role_list)
            logging.debug(user_name)
            if user_name == 0:
                self.userIDLineEdit.clear()
                self.userIDLineEdit.setEnabled(True)
                self.userNameLineEdit.clear()
                self.passwordLineEdit1.clear()
                self.passwordLineEdit2.clear()
            else:
                sql = "select a.user_id, a.user_name, a.password, b.role_name from t_user a join t_role b on a.role_id = b.id where a.user_name = '%s'" % user_name
                ret = self.db.query(sql)
                if ret:
                    self.user_id = ret[0].get('user_id')
                    user_name = ret[0].get('user_name')
                    self.password = ret[0].get('password')
                    role_name = ret[0].get('role_name')
                    self.roleComboBox.setCurrentText(role_name)
                    self.userIDLineEdit.setText(self.user_id)
                    self.userIDLineEdit.setEnabled(False)
                    self.userNameLineEdit.setText(user_name)
                    self.passwordLineEdit1.setText(self.password)
                    self.passwordLineEdit2.setText(self.password)

    def __save_data(self):
        """
        保存数据
        :return:
        """
        role_name = self.roleComboBox.currentText()
        user_id = self.userIDLineEdit.text()
        if user_id:
            sql = "select user_id from t_user where user_id <> '%s'" % self.user_id
            ret = self.db.query(sql, result_dict=False)
            if ret:
                user_id_list = list(list(zip(*ret))[0])
                if user_id in user_id_list:
                    QtWidgets.QMessageBox.warning(self, '本程序', "用户代码已存在！", QtWidgets.QMessageBox.Ok)
                    return
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "请输入用户代码！", QtWidgets.QMessageBox.Ok)
            return
        user_name = self.userNameLineEdit.text()
        if user_name:
            sql = "select user_name from t_user where user_id <> '%s'" % self.user_id
            ret = self.db.query(sql, result_dict=False)
            if ret:
                user_name_list = list(list(zip(*ret))[0])
                if user_name in user_name_list:
                    QtWidgets.QMessageBox.warning(self, '本程序', "用户名已存在！", QtWidgets.QMessageBox.Ok)
                    return
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "请输入用户名！", QtWidgets.QMessageBox.Ok)
            return
        user_pwd1 = self.passwordLineEdit1.text()
        user_pwd2 = self.passwordLineEdit2.text()
        if user_pwd1 and user_pwd2:
            if user_pwd1 != user_pwd2:
                QtWidgets.QMessageBox.warning(self, '本程序', "两次密码不一样！", QtWidgets.QMessageBox.Ok)
                return
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "请输入密码！", QtWidgets.QMessageBox.Ok)
            return
        user_pwd = "321"
        if user_pwd1 == self.password:
            user_pwd = user_pwd1
        else:
            user_pwd = normal_utils.get_pwd_md5(user_pwd1)
        role_sql = "select id from t_role where role_name = '%s'" % role_name
        ret = self.db.query(role_sql)
        role_id = ret[0].get('id')
        permission_sql = ''
        if self.user_id == 0:
            user_sql = "insert into t_user(user_id, user_name, role_id, password) values('%s','%s','%s','%s')" % \
                       (user_id, user_name, role_id, user_pwd)
            permission_sql = """insert into t_permission (object_type, object_id, operation_id, status) 
                                 select 2 as object_type, '%s' as object_id, id, 0 as status from t_operation
                                 where status = 1 """ % user_id
        else:
            user_sql = "update t_user set user_name='%s', role_id='%s', password='%s' where user_id = '%s'" % \
                       (user_name, role_id, user_pwd, user_id)
        ret = self.db.update(user_sql)
        if ret:
            if permission_sql:
                self.db.update(permission_sql)
            QtWidgets.QMessageBox.information(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
            self.my_signal.emit(user_name)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)


class RoleManageForm(QtWidgets.QWidget, Ui_roleForm):
    """
    角色管理
    """
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(RoleManageForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.savePushButton.clicked.connect(self.__save_data)
        self.cancelPushButton.clicked.connect(self.close)

    def show(self):
        """
        显示界面
        :return:
        """
        super().show()
        self.roleLineEdit.clear()

    def __save_data(self):
        """
        保存数据
        :return:
        """
        role_name = self.roleLineEdit.text()
        if role_name:
            sql = "select role_name from t_role"
            ret = self.db.query(sql, result_dict=False)
            if ret:
                role_name_list = list(list(zip(*ret))[0])
                if role_name in role_name_list:
                    QtWidgets.QMessageBox.warning(self, '本程序', "角色已存在！", QtWidgets.QMessageBox.Ok)
                    return
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "请输入角色名称！", QtWidgets.QMessageBox.Ok)
            return

        role_sql = "insert into t_role(role_name) values('%s')" % role_name
        permission_sql = """insert into t_permission (object_type, object_id, operation_id, status) 
                                         select 1 as object_type, b.role_id as object_id, id, 0 as status from t_operation a
                                         left join (select id as role_id from t_role where role_name = '%s') b on 1 = 1 
                                         where status = 1 """ % role_name
        ret = self.db.update(role_sql)
        if ret:
            self.db.update(permission_sql)
            QtWidgets.QMessageBox.information(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
            self.my_signal.emit(role_name)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = PermissionSetupForm()
    myshow.show()
    sys.exit(app.exec_())