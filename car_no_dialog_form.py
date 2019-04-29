#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from functools import partial
from ui.car_no_dialog import Ui_DockWidget
import logging


class CarNoDialogForm(QtWidgets.QDockWidget, Ui_DockWidget):
    """
    车牌号输入键盘
    """
    my_signal = pyqtSignal(str)

    def __init__(self):
        super(CarNoDialogForm, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.text = ''
        for row in range(self.gridLayout.rowCount()):
            if row < 3:
                for col in range(self.gridLayout.columnCount()):
                    item = self.gridLayout.itemAtPosition(row, col)
                    if item and isinstance(item, QtWidgets.QWidgetItem):
                        button = item.widget()
                        button.clicked.connect(partial(self.click_province, button.text()))
            else:
                for col in range(self.gridLayout.columnCount()):
                    item = self.gridLayout.itemAtPosition(row, col)
                    if item and isinstance(item, QtWidgets.QWidgetItem):
                        button = item.widget()
                        button.clicked.connect(partial(self.click_letter, button.text()))

        for idx in range(self.horizontalLayout.count()):
            item = self.horizontalLayout.itemAt(idx)
            if item and isinstance(item, QtWidgets.QWidgetItem):
                button = item.widget()
                if button.text() == u'确定':
                    button.clicked.connect(self.close)
                else:
                    button.clicked.connect(partial(self.click_letter, button.text()))

    def click_province(self, char):
        """
        点击省事件
        :param char:
        :return:
        """
        self.text = char
        self.my_signal.emit(self.text)

    def click_letter(self, char):
        """
        点击字母数字事件
        :param char:
        :return:
        """
        self.text += char
        self.my_signal.emit(self.text)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = CarNoDialogForm()
    myshow.show()
    sys.exit(app.exec_())