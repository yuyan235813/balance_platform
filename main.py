#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlQueryModel
from ui.balance import Ui_mainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from utils import com_interface_utils, normal_utils
from utils.log_utils import Logger as logger
from utils import normal_utils
from conf.constant import NormalParam
from conf.config import (COM_BAUD_RATE, COM_INTERFACE, DEBUG)
from setup_form import SetupForm
from params_form import ParamsForm
from system_params_form import SystemParamsForm
from functools import partial
import subprocess
import sys
import serial
import time
import os


class MainForm(QtWidgets.QMainWindow, Ui_mainWindow):
    u"""
    mainform
    """
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.weightLcdNumber.display(0)
        # 查询模型
        self.queryModel = None
        self.init_data()
        self.params_form = ParamsForm()
        self.actionParameterSetup.triggered.connect(self.params_form.show)
        self.setup_form = SetupForm()
        self.actionBalanceFormSetup.triggered.connect(self.setup_form.show)
        self.system_params_form = SystemParamsForm()
        self.actionSystemParameterSetup.triggered.connect(self.system_params_form.show)

    def show(self):
        """
        显示界面
        :return:
        """
        super().show()
        query_sql = 'select * from t_balance'
        self.setTableView()

    def setTableView(self):
        """

        :return:
        """
        # 声明查询模型
        self.queryModel = QSqlQueryModel(self)
        # 设置模型

        # 设置表格表头
        self.queryModel.setHeaderData(0, Qt.Horizontal, "编号")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "姓名")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "性别")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "年龄")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "院系")
        self.queryModel.setQuery("select 1,2,3,4,5")
        self.tableView.setModel(self.queryModel)


    def init_data(self):
        u"""
        初始化数据和定时器
        :return:
        """
        self._is_open = False
        self._com_worker = COMThread()
        self._com_worker.start()
        self._weight = {}
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
            now = int(time.time() * 1000)
            self._weight[now] = weight
            del_keys = [k for k in self._weight.keys() if now - k > (NormalParam.STABLES_DURATION + 1) * 1000]
            [self._weight.pop(k) for k in del_keys]

    def check_weight_state(self):
        u"""
        获取停止读取标志
        :return:
        """
        if self._is_open:
            now = int(time.time() * 1000)
            first = min(self._weight.keys())
            if first + NormalParam.STABLES_DURATION * 1000 < now:
                weights = [v for k, v in self._weight.items() if now - k <= NormalParam.STABLES_DURATION * 1000]
                if normal_utils.stdev(weights) <= NormalParam.STABLES_ERROR:
                    self.stateLabel.setText(u'稳定')
                    self.stateLabel.setStyleSheet('color:green')
            else:
                self.stateLabel.setText(u'读取中……')
                self.stateLabel.setStyleSheet('color:black')
        else:
            self.stateLabel.setText(u'称重仪表未连接！')
            self.stateLabel.setStyleSheet('color:red')

    def closeEvent(self, event):
        """
        点击X号退出事件
        :param event:
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            event.ignore()


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
        if self._serial.isOpen():
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
                self.trigger.emit(1, weight)
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