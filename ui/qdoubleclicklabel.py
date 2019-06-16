# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class QDoubleClickLabel(QLabel):
    """
    自定义 QLabel 控件
    """
    doubleClicked = pyqtSignal(bool)

    def __init__(self, *__args):
        super(QDoubleClickLabel, self).__init__(*__args)

    def mouseDoubleClickEvent(self, e):
        """
        重写双击事件
        :param e:
        :return:
        """
        self.doubleClicked.emit(True)
