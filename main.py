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
from utils import com_interface_utils, normal_utils
from utils.log_utils import Logger as logger
from conf.constant import NormalParam
from conf.config import (COM_BAUD_RATE, COM_INTERFACE)
import sys
import serial
import time


class MainForm(QtWidgets.QMainWindow, Ui_mainWindow):
    u"""
    mainform
    """
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.init_serial()
        self.initData()

    def initData(self):
        u"""
        初始化数据和定时器
        :return:
        """
        self._weightList = []
        self._weightLength = com_interface_utils.get_bytes_num()
        self._timer = QTimer(self)  # 新建一个定时器
        # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
        self._timer.timeout.connect(self.showLcd)
        self._timer.timeout.connect(self.check_weight_state)
        self._timer.start(NormalParam.COM_READ_DURATION)  # 设置定时间隔为1000ms即1s，并启动定时器

    def showLcd(self):
        u"""
        显示数据
        :return:
        """
        weight = com_interface_utils.read_com_interface(self.__serial)
        # weight = self.read_com_interface()
        # print(weight)
        self.weightLcdNumber.display(weight)
        if len(self._weightList) < self._weightLength:
            self._weightList.append(weight)
        else:
            self._weightList.pop(0)
            self._weightList.append(weight)


    def init_serial(self):
        u"""
        :return:
        """
        self._serial = serial.Serial(COM_INTERFACE, COM_BAUD_RATE, timeout=0.5)
        if self._serial.isOpen():
            logger.info("open success")
        else:
            logger.error("open failed")

    def read_com_interface(self):
            self.__count += 1
            return self.__count
            time.sleep(10)


    def check_weight_state(self):
        u"""
        获取停止读取标志
        :return:
        """
        if len(self._weightList) == self._weightLength:
            if normal_utils.stdev(self._weightList) <= NormalParam.STABLES_ERROR:
                self.weightLabel.text(u'稳定')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())