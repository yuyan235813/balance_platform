# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import pyqtSignal


class MyQGraphicsView(QGraphicsView):
    """
    自定义 QImageLabel 控件
    """
    doubleClicked = pyqtSignal(str)

    def __init__(self, *__args):
        super(MyQGraphicsView, self).__init__(*__args)

    def mouseDoubleClickEvent(self, e):
        """
        重写双击事件
        :param e:
        :return:
        """
        self.doubleClicked.emit(self.windowFilePath())
