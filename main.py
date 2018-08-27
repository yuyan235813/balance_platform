#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from ui.balance import Ui_mainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from utils.com_interface_utils import read_com_interface
from conf.constant import NormalParam
from conf.config import (COM_BAUD_RATE, COM_INTERFACE)
import sys
import serial
import time


class MainForm(QtWidgets.QMainWindow, Ui_mainWindow):
    """
    mainform
    """
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.init_serial()
        self.initData()

    def initData(self):
        """
        初始化数据和定时器
        :return:
        """
        self._count = 1
        self._timer = QTimer(self)  # 新建一个定时器
        # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
        self._timer.timeout.connect(self.showLcd)
        self._timer.start(NormalParam.COM_READ_DURATION)  # 设置定时间隔为1000ms即1s，并启动定时器

    def showLcd(self):
        """
        显示数据
        :return:
        """
        weight = read_com_interface(self.__serial)
        # weight = self.read_com_interface()
        # print(weight)
        self.weightLcdNumber.display(weight)

    def init_serial(self):
        """
        :return:
        """
        self._serial = serial.Serial(COM_INTERFACE, COM_BAUD_RATE, timeout=0.5)
        if self._serial.isOpen():
            print("open success")
        else:
            print("open failed")

    def read_com_interface(self):
            self.__count += 1
            return self.__count
            time.sleep(10)


    def get_stop_flag(self):
        """
        获取停止读取标志
        :return:
        """
        pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())