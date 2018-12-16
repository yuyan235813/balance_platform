#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from ui.login import Ui_loginDialog
from main_form import MainForm
from utils.sqllite_util import EasySqlite
from winreg import *
import winreg
import Psyunew3
from ctypes import *
import logging.config
import os
logging.config.fileConfig('rmf/log/logging.conf')
logger = logging.getLogger(os.path.basename(__file__))


class LoginForm(QtWidgets.QDialog, Ui_loginDialog):
    """
    车辆管理
    """

    def __init__(self):
        super(LoginForm, self).__init__()
        self.setupUi(self)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.cancelPushButton.clicked.connect(self.close)
        self.isexist = 0
        DevicePath = create_string_buffer(b'\0' * 260)
        ret = c_int()
        # 从加密锁中读取字符串,使用默认的读密码:ffffffff', 'ffffffff', 从加密锁的第0个地址开始读
        mylen = c_short()
        mylen = 9  # 注意这里的长度，长度要与写入的字符串的长度相同,
        outstring = create_string_buffer(b'\0' * (mylen + 1))

        ##这个用于判断系统中是否存在着加密锁。不需要是指定的加密锁,
        ret = Psyunew3.FindPort(0, DevicePath)
        if (ret != 0):
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"")
            # 删除键
            # #winreg.DeleteKey(key, "Advanced")
            # 删除键值
            # winreg.DeleteValue(key, "IconUnderline")
            # 如果知道键的名称，也可以直接取值
            try:
                i = 0
                while 1:
                    name = winreg.EnumKey(key, i)
                    if name == "MyNewkey":
                        self.isexist = 1
                        break
                    i += 1
            except WindowsError as e:
                logger.error(u"操作注册表异常：", e)
            if self.isexist:
                keys = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                      r"MyNewkey")
                usetime = winreg.QueryValue(keys, "ValueName")
                if int(usetime) > 0:
                    if int(usetime) > 100:
                        QtWidgets.QMessageBox.warning(self, '本程序', "无效使用次数！", QtWidgets.QMessageBox.Ok)
                        exit()
                    QtWidgets.QMessageBox.warning(self, '本程序', "你还可以使用本软件 %s次！" % usetime, QtWidgets.QMessageBox.Ok)
                    newtime = int(usetime) - 1;
                    winreg.SetValue(keys, "ValueName", REG_SZ, str(newtime))
                else:
                    QtWidgets.QMessageBox.warning(self, '本程序', "继续使用，请购买本软件！", QtWidgets.QMessageBox.Ok)
                    exit()
            else:
                newKey = winreg.CreateKey(key, "MyNewkey")
                winreg.SetValue(newKey, "ValueName", REG_SZ, "98")
                QtWidgets.QMessageBox.warning(self, '本程序', "未检测到加密狗，你可以使用本软件99次！", QtWidgets.QMessageBox.Ok)
        else:
            if Psyunew3.YReadString(outstring, 0, mylen, b'FFFFFFFF', b'FFFFFFFF', DevicePath) != 0:
                QtWidgets.QMessageBox.warning(self, '本程序', "加密狗密钥错误！", QtWidgets.QMessageBox.Ok)
                exit()
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
        sql = "select user_name, user_id, password from t_user where user_name = '%s'" % user_name
        ret = self.db.query(sql)
        if ret:
            password = ret[0].get('password')
            user_id = ret[0].get('user_id')
            if pwd == password:
                logger.info(user_name)
                self.mainWidget = MainForm(user_id)
                self.mainWidget.show()
                self.close()
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "密码错误！", QtWidgets.QMessageBox.Ok)
                return
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "错误！", QtWidgets.QMessageBox.Ok)
            return


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = LoginForm()
    myshow.show()
    sys.exit(app.exec_())
