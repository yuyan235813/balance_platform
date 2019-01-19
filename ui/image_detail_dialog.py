# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_detail_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_imageDetailDialog(object):
    def setupUi(self, imageDetailDialog):
        imageDetailDialog.setObjectName("imageDetailDialog")
        imageDetailDialog.resize(1109, 683)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(imageDetailDialog.sizePolicy().hasHeightForWidth())
        imageDetailDialog.setSizePolicy(sizePolicy)
        imageDetailDialog.setSizeGripEnabled(False)
        self.horizontalLayout = QtWidgets.QHBoxLayout(imageDetailDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView_1 = MyQGraphicsView(imageDetailDialog)
        self.graphicsView_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.horizontalLayout.addWidget(self.graphicsView_1)

        self.retranslateUi(imageDetailDialog)
        QtCore.QMetaObject.connectSlotsByName(imageDetailDialog)

    def retranslateUi(self, imageDetailDialog):
        _translate = QtCore.QCoreApplication.translate
        imageDetailDialog.setWindowTitle(_translate("imageDetailDialog", "图片查看"))

from ui.my_qgraphics_view import MyQGraphicsView
