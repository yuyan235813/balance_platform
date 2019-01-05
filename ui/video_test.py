# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_videoTest(object):
    def setupUi(self, videoTest):
        videoTest.setObjectName("videoTest")
        videoTest.resize(826, 655)
        videoTest.setWindowTitle("")
        self.verticalLayout = QtWidgets.QVBoxLayout(videoTest)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(videoTest)
        self.label_2.setMinimumSize(QtCore.QSize(400, 300))
        self.label_2.setMaximumSize(QtCore.QSize(1280, 720))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(videoTest)
        self.label_1.setMinimumSize(QtCore.QSize(400, 300))
        self.label_1.setMaximumSize(QtCore.QSize(1280, 720))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(videoTest)
        self.label_3.setMinimumSize(QtCore.QSize(400, 300))
        self.label_3.setMaximumSize(QtCore.QSize(1280, 720))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(videoTest)
        self.label_4.setMinimumSize(QtCore.QSize(400, 300))
        self.label_4.setMaximumSize(QtCore.QSize(1280, 720))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(videoTest)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(videoTest)
        QtCore.QMetaObject.connectSlotsByName(videoTest)

    def retranslateUi(self, videoTest):
        _translate = QtCore.QCoreApplication.translate
        videoTest.setToolTip(_translate("videoTest", "video"))
        self.pushButton.setText(_translate("videoTest", "截    图"))

