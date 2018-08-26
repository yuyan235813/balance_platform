#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from balance import Ui_mainWindow
from PyQt5 import QtWidgets
from PyQt5.Qt import QTimer
from com_test import read_com_interface
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
        self.__count = 1
        self.__timer = QTimer(self)  # 新建一个定时器
        # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
        self.__timer.timeout.connect(self.showLcd)
        self.__timer.start(200)  # 设置定时间隔为1000ms即1s，并启动定时器

    def showLcd(self):
        """
        显示数据
        :return:
        """
        weight = read_com_interface(self.__serial)
        # weight = self.read_com_interface()
        print(weight)
        self.weightLcdNumber.display(weight)

    def init_serial(self):
        """
        :return:
        """
        self.__serial = serial.Serial('COM3', 9600, timeout=0.5)  # /dev/ttyUSB0
        if self.__serial.isOpen():
            print("open success")
        else:
            print("open failed")

    def read_com_interface(self):
            self.__count += 1
            return self.__count
            time.sleep(100)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())