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
from ui.car_manage_change import Ui_dialog
from utils.sqllite_util import EasySqlite
from utils.normal_utils import get_cur_time
from utils.log_utils import Logger as logger
from functools import reduce


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
        self.editRolePushButton.clicked.connect(self.__change_role)
        self.editUserPushButton.clicked.connect(self.__change_user)

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        # 用户
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

    def show(self):
        """
        显示界面
        :return:
        """
        super().show()
        self.__init_data()

    def __change_user(self, model):
        """
        更改用户
        :param model:
        :return:
        """
        print(model.text())

    def __change_role(self, model):
        """
        更改角色
        :param model:
        :return:
        """
        print(model.text())

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

    def __save_data(self):
        pass

    def __add_user(self):
        """
        添加用户
        :return:
        """
        item = self.userListWidget.currentItem()
        print(item.text())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = PermissionSetupForm()
    myshow.show()
    sys.exit(app.exec_())