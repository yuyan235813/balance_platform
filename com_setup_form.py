#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from ui.com_setup_form import Ui_ComSetupForm
from PyQt5.QtCore import Qt
from utils.sqllite_util import EasySqlite
import serial.tools.list_ports as list_ports
import logging


class ComSetupForm(QtWidgets.QWidget, Ui_ComSetupForm):
    """
    参数设置
    """
    def __init__(self):
        super(ComSetupForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.cancelPushButton.clicked.connect(self.close)
        self.savePushButton.clicked.connect(self.save)

    def show(self):
        """
        显示ui
        :return:
        """
        super(ComSetupForm, self).show()
        self.issueComboBox.clear()
        self.readComboBox.clear()
        self.barrierComboBox.clear()
        ports = self.list_ports
        self.issueComboBox.addItems(ports)
        self.readComboBox.addItems(ports)
        self.barrierComboBox.addItems(ports)
        query_sql = "select * from t_com_auto where id = 1;"
        ret = self.db.query(query_sql)
        if not ret:
            return
        params = ret[0]
        self.issueComboBox.setCurrentText('COM%s' % params.get('issue_com', '1'))
        self.readComboBox.setCurrentText('COM%s' % params.get('read_com', '1'))
        self.barrierComboBox.setCurrentText('COM%s' % params.get('barrier_com', '1'))

    def save(self):
        """
        保存设置
        :return:
        """
        issue_com = self.issueComboBox.currentText().replace('COM', '')
        read_com = self.issueComboBox.currentText().replace('COM', '')
        barrier_com = self.issueComboBox.currentText().replace('COM', '')
        update_sql = 'replace into t_com_auto(id, issue_com, read_com, barrier_com)' \
                     ' values(1, ?, ?, ?)'
        ret = self.db.query(update_sql, [issue_com, read_com, barrier_com])
        if ret:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)

    @property
    def list_ports(self):
        """
        电脑所有串口
        :return:
        """
        ports = list_ports.comports()
        return [port.device for port in ports]


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = ComSetupForm()
    myshow.show()
    sys.exit(app.exec_())