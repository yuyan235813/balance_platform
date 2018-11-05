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
        self.userListWidget.itemDoubleClicked.connect(self.__change_user)
        self.userListWidget.itemClicked.connect(self.__show_user_permissions)
        self.roleListWidget.itemDoubleClicked.connect(self.__change_role)
        self.roleListWidget.itemClicked.connect(self.__show_role_permissions)

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

    def __show_role_permissions(self, model):
        """
        显示角色权限
        :param model:
        :return:
        """
        print(model.text())

    def __save_data(self):
        pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = PermissionSetupForm()
    myshow.show()
    sys.exit(app.exec_())