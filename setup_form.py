#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from ui.balance_setup import Ui_balanceSetup
from utils import normal_utils
import subprocess
from utils.sqllite_util import EasySqlite
import logging
import os


class SetupForm(QtWidgets.QWidget, Ui_balanceSetup):
    """
    磅单设置
    RMReport.exe -d dbFile -s dbStr -r rmf -a action
    """
    def __init__(self):
        super(SetupForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.p = None
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.exitPushButton.clicked.connect(self.close)
        self.rmf_path = os.path.join(os.getcwd(), r'rmf\rmf')
        self.report_file = os.path.join(os.getcwd(), r'rmf\RMReport.exe')
        self.defaultPushButton.clicked.connect(self.set_default_rmf)
        self.previewPushButton.clicked.connect(self.preview_rmf)
        self.setupPushButton.clicked.connect(self.setup_rmf)
        self.checkBox.stateChanged.connect(self.set_auto_print)
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)

    def show(self):
        super(SetupForm, self).show()
        list_parh = normal_utils.get_file_list(self.rmf_path)
        list_rmf = [os.path.split(path)[1] for path in list_parh]
        self.listWidget.addItems(list_rmf)
        db = EasySqlite(r'rmf/db/balance.db')
        select_sql = 'select * from t_rmf'
        ret = db.query(select_sql)
        if ret and len(ret) > 0:
            self.selectedLineEdit.setText(ret[0]['default_rmf'])
            self.checkBox.setChecked(True if ret[0]['auto_print'] else False)
        elif self.listWidget.currentItem():
            self.selectedLineEdit.setText(self.listWidget.currentItem().text())
        elif list_rmf:
            self.selectedLineEdit.setText(list_rmf[0])
        self.listWidget.itemClicked.connect(self.selected_item)

    def selected_item(self, item):
        """
        点击list中的item事件
        :param item:
        :return:
        """
        self.selectedLineEdit.setText(item.text())

    def set_auto_print(self, signal):
        """
        设置是否自动打印
        :param signal:
        :return:
        """
        print(signal)
        sql = """update t_rmf set auto_print = %s where id = 1""" % signal
        ret = self.db.update(sql)
        if ret:
            logging.info("设置自动打印状态为: %s" % ("打开" if signal else "关闭"))
        else:
            logging.error("设置自动打印失败！")

    def set_default_rmf(self):
        db = EasySqlite(r'rmf/db/balance.db')
        insert_sql = 'replace into t_rmf values(1, "%s")' % self.selectedLineEdit.text()
        logging.debug(insert_sql)
        ret = db.update(insert_sql)
        if ret:
            QtWidgets.QMessageBox.information(self, '本程序', "设置成功", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "设置失败102", QtWidgets.QMessageBox.Ok)

    def preview_rmf(self):
        """
        预览空磅单
        :return:
        """
        cmd_str = self.report_file + u' -d "balance.db" -s "db1:select date(\'now\')" -r "%s" -a 0' % \
                  self.selectedLineEdit.text()
        logging.debug(cmd_str)
        self.p = subprocess.Popen(cmd_str)

    def setup_rmf(self):
        """
        设置磅单
        :return:
        """
        cmd_str = self.report_file + u' -d "balance.db" -s "db1:select t_balance.*,t_supplier.* from t_balance,t_supplier where t_balance.supplier = t_supplier.supplier_name" -r "%s" -a 2' % \
                  self.selectedLineEdit.text()
        logging.debug(cmd_str)
        self.p = subprocess.Popen(cmd_str)

    def closeEvent(self, event):
        """
        关闭事件
        :param event:
        :return:
        """
        super().closeEvent(event)
        if self.p:
            self.p.kill()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = SetupForm()
    myshow.show()
    sys.exit(app.exec_())