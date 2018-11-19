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
from ui.login import Ui_loginDialog
from main_form import MainForm
from utils.sqllite_util import EasySqlite
from utils.normal_utils import get_cur_time
from utils.log_utils import Logger as logger


class LoginForm(QtWidgets.QDialog, Ui_loginDialog):
    """
    车辆管理
    """
    def __init__(self):
        super(LoginForm, self).__init__()
        self.setupUi(self)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.cancelPushButton.clicked.connect(self.close)
        self.__init_data()
        self.loginPushButton.clicked.connect(self.__login)

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        sql = "select user_name from t_user where status = 1"
        ret = self.db.query(sql, result_dict=False)
        user_list = list(zip(*ret))[0]
        self.usernameComboBox.addItems(user_list)

    def __login(self):
        """
        登录操作
        :return:
        """
        pwd = self.passwordLineEdit.text()
        user_name = self.usernameComboBox.currentText()
        if not pwd:
            QtWidgets.QMessageBox.warning(self, '本程序', "密码不能为空！", QtWidgets.QMessageBox.Ok)
            return
        sql = "select user_name, password from t_user where user_name = '%s'" % user_name
        ret = self.db.query(sql)
        password = ret[0].get('password')
        if pwd == password:
            self.mainWidget = MainForm(user_name)
            self.mainWidget.show()
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "密码错误！", QtWidgets.QMessageBox.Ok)
            return



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = LoginForm()
    myshow.show()
    sys.exit(app.exec_())