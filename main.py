#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from ui.balance import Ui_mainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from utils import com_interface_utils, normal_utils
from utils.log_utils import Logger as logger
from conf.constant import NormalParam
from conf.config import (COM_BAUD_RATE, COM_INTERFACE, DEBUG)
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
        self.weightLcdNumber.display(0)
        self.init_data()

    def init_data(self):
        u"""
        初始化数据和定时器
        :return:
        """
        self._is_open = False
        self._com_worker = COMThread()
        self._com_worker.start()
        self._weightList = []
        self._weightLength = com_interface_utils.get_bytes_num()
        self._timer = QTimer(self)  # 新建一个定时器
        # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
        self._com_worker.trigger.connect(self.show_lcd)
        self._timer.timeout.connect(self.check_weight_state)
        self._timer.start(NormalParam.COM_READ_DURATION)  # 设置定时间隔为1000ms即1s，并启动定时器

    def show_lcd(self, is_open, weight):
        u"""
        显示数据
        :return:
        """
        if is_open:
            self._is_open = True
            self.weightLcdNumber.display(weight)
            if len(self._weightList) < self._weightLength:
                self._weightList.append(weight)
            else:
                self._weightList.pop(0)
                self._weightList.append(weight)

    def check_weight_state(self):
        u"""
        获取停止读取标志
        :return:
        """
        if self._is_open:
            if len(self._weightList) == self._weightLength:
                if normal_utils.stdev(self._weightList) <= NormalParam.STABLES_ERROR:
                    self.stateLabel.setText(u'稳定')
                    self.stateLabel.setStyleSheet('color:green')
                else:
                    self.stateLabel.setText(u'读取中……')
                    self.stateLabel.setStyleSheet('color:black')
            else:
                self.stateLabel.setText(u'读取中……')
        else:
            self.stateLabel.setText(u'称重仪表未连接！')
            self.stateLabel.setStyleSheet('color:red')


class COMThread(QThread):
    """
    串口读取线程
    """
    trigger = pyqtSignal(int, float)

    def __init__(self):
        self._is_conn = False
        super().__init__()

    def init_serial(self):
        u"""
        :return:
        """
        self._serial = serial.Serial(COM_INTERFACE, COM_BAUD_RATE, timeout=0.5)
        if self._serial.is_open():
            logger.info("open success")
        else:
            logger.error("open failed")
            raise Exception(u'%s 串口打开失败！' % COM_INTERFACE)

    def run(self):
        """
        读取串口信息
        :return:
        """
        if DEBUG:
            while True:
                weight = 100
                self.trigger.emit(0, weight)
                time.sleep(NormalParam.COM_READ_DURATION / 2 / 1000)
        else:
            while not self._is_conn:
                try:
                    self.init_serial()
                    self._is_conn = True
                except serial.serialutil.SerialException as e:
                    logger.error(e)
                    logger.info(u'%s 接口未连接！' % COM_INTERFACE)
                    time.sleep(NormalParam.COM_CHECK_CONN_DURATION)
                except Exception as e:
                    logger.error(e)
                    time.sleep(NormalParam.COM_OPEN_DURATION)
            while True:
                is_open = 1
                weight = com_interface_utils.read_com_interface(self._serial)
                self.trigger.emit(is_open, weight)
                time.sleep(NormalParam.COM_READ_DURATION / 2 / 1000)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())