#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.permission_setup import Ui_permissionSetupForm
from ui.user_manage import Ui_Form
from ui.car_manage_change import Ui_dialog
from utils.sqllite_util import EasySqlite
from utils.normal_utils import get_cur_time
from utils.log_utils import Logger as logger
from functools import reduce, partial


class PermissionSetupForm(QtWidgets.QWidget, Ui_permissionSetupForm):
    """
    车辆管理
    """
    def __init__(self):
        super(PermissionSetupForm, self).__init__()
        self.setupUi(self)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.savePushButton.clicked.connect(self.__save_data)
        self.cancelPushButton.clicked.connect(self.close)
        self.addUserPushButton.clicked.connect(self.__add_user)
        self.addRolePushButton.clicked.connect(self.__add_role)
        self.editRolePushButton.clicked.connect(self.__change_role)
        self.editUserPushButton.clicked.connect(self.__change_user)
        self.deleteUserPushButton.clicked.connect(self.__delete_user)
        self.deleteUserPushButton.clicked.connect(self.__delete_role)
        self.userMangeForm = UserManageForm()
        self.userMangeForm.my_signal.connect(self.__init_data)

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        # 用户
        self.userListWidget.clear()
        user_sql = 'select user_id, user_name from t_user where status = 1 order by id;'
        user_ret = self.db.query(user_sql)
        user_item = []
        for item in user_ret:
            user_item.append(item.get('user_name'))
        self.userListWidget.addItems(user_item)
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

        self.optionTableView.doubleClicked.connect(partial(self.__change_permissions, 1))
        self.permissionTableView.doubleClicked.connect(partial(self.__change_permissions, 2))

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
        print(model.text())
        user_name = model.text()
        sql_tmp = """
            select t1.opt_type, opt_name, case when t2.object_id is null then 0 else 1 end as has_permission
            from
            (select opt_type, opt_name, id from t_operation where status = 1) t1
            left join
            (select * from (select user_id, role_id from t_user where user_name = '%s' and status = 1) a 
                join t_permission b 
                on (a.user_id = b.object_id and b.object_type = 2) or (a.role_id = b.object_id and b.object_type = 1)
            ) t2 on t1.id = t2.operation_id"""
        sql = sql_tmp % user_name
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

    def __show_role_permissions(self, model):
        """
        显示角色权限
        :param model:
        :return:
        """
        print(model.text())
        role_name = model.text()
        sql_tmp = """
                    select t1.opt_type, opt_name, case when t2.object_id is null then 0 else 1 end as has_permission
                    from
                    (select opt_type, opt_name, id from t_operation where status = 1) t1
                    left join
                    (select * from (select id as role_id from t_role where role_name = '%s' and status = 1) a 
                        join t_permission b 
                        on a.role_id = b.object_id and b.object_type = 1
                    ) t2 on t1.id = t2.operation_id"""
        sql = sql_tmp % role_name
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
        pass

    def __add_user(self):
        """
        添加用户
        :return:
        """
        self.userMangeForm.show(0)

    def __add_role(self):
        """
        添加用户
        :return:
        """
        pass

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
        self.userMangeForm.show(user_name)

    def __change_role(self, model):
        """
        更改角色
        :param model:
        :return:
        """
        pass

    def __delete_user(self):
        """
        添加用户
        :return:
        """
        if not self.userListWidget.currentItem():
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的用户！", QtWidgets.QMessageBox.Ok)
            return
        user_name = self.userListWidget.currentItem().text()
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要删除用户 %s？" % user_name,
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sql = "delete from t_user where user_name = '%s'" % user_name
            ret = self.db.update(sql)
            if ret:
                QtWidgets.QMessageBox.warning(self, '本程序', "删除成功！", QtWidgets.QMessageBox.Ok)
                self.__init_data()
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "删除失败！", QtWidgets.QMessageBox.Ok)
        else:
            return


    def __delete_role(self):
        """
        添加用户
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
        role_list = list(list(zip(*ret))[0])
        self.roleComboBox.addItems(role_list)
        if user_name == 0:
            pass
        else:
            sql = "select a.user_id, a.user_name, a.password, b.role_name from t_user a join t_role b on a.role_id = b.id where a.user_name = '%s'" % user_name
            ret = self.db.query(sql)
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
            sql = "select user_id from t_user"
            ret = self.db.query(sql, result_dict=False)
            user_id_list = list(list(zip(*ret))[0])
            if user_id in user_id_list:
                QtWidgets.QMessageBox.warning(self, '本程序', "用户代码已存在！", QtWidgets.QMessageBox.Ok)
                return
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "请输入用户代码！", QtWidgets.QMessageBox.Ok)
            return
        user_name = self.userNameLineEdit.text()
        if user_name:
            sql = "select user_name from t_user"
            ret = self.db.query(sql, result_dict=False)
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
        # todo 密码加密
        if user_pwd1 == self.password:
            pass
        else:
            pass
        role_sql = "select id from t_role where role_name = '%s'" % role_name
        ret = self.db.query(role_sql)
        role_id = ret[0].get('id')
        if self.user_id == 0:
            user_sql = "insert into t_user(user_id, user_name, role_id, password) values('%s','%s','%s','%s')" % \
                       (user_id, user_name, role_id, user_pwd1)
        else:
            user_sql = "update t_user set user_name='%s', role_id='%s', password='%s'" % \
                       (user_name, role_id, user_pwd1)
        print(user_sql)
        ret = self.db.update(user_sql)
        if ret:
            QtWidgets.QMessageBox.information(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
            self.my_signal.emit(user_name)
            self.close()
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)






if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = PermissionSetupForm()
    myshow.show()
    sys.exit(app.exec_())