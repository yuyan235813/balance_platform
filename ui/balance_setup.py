# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'balance_setup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_balanceSetup(object):
    def setupUi(self, balanceSetup):
        balanceSetup.setObjectName("balanceSetup")
        balanceSetup.setEnabled(True)
        balanceSetup.resize(357, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(balanceSetup.sizePolicy().hasHeightForWidth())
        balanceSetup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        balanceSetup.setFont(font)
        balanceSetup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox = QtWidgets.QGroupBox(balanceSetup)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 611))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.selectedLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.selectedLineEdit.setEnabled(True)
        self.selectedLineEdit.setDragEnabled(False)
        self.selectedLineEdit.setReadOnly(True)
        self.selectedLineEdit.setObjectName("selectedLineEdit")
        self.verticalLayout.addWidget(self.selectedLineEdit)
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.setupPushButton = QtWidgets.QPushButton(self.groupBox)
        self.setupPushButton.setObjectName("setupPushButton")
        self.horizontalLayout.addWidget(self.setupPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.previewPushButton = QtWidgets.QPushButton(self.groupBox)
        self.previewPushButton.setObjectName("previewPushButton")
        self.horizontalLayout.addWidget(self.previewPushButton)
        self.horizontalLayout.setStretch(0, 12)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.defaultPushButton = QtWidgets.QPushButton(self.groupBox)
        self.defaultPushButton.setObjectName("defaultPushButton")
        self.horizontalLayout_2.addWidget(self.defaultPushButton)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.exitPushButton = QtWidgets.QPushButton(self.groupBox)
        self.exitPushButton.setObjectName("exitPushButton")
        self.horizontalLayout_3.addWidget(self.exitPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(balanceSetup)
        QtCore.QMetaObject.connectSlotsByName(balanceSetup)

    def retranslateUi(self, balanceSetup):
        _translate = QtCore.QCoreApplication.translate
        balanceSetup.setWindowTitle(_translate("balanceSetup", "磅单设置"))
        self.groupBox.setTitle(_translate("balanceSetup", "磅单设置"))
        self.setupPushButton.setText(_translate("balanceSetup", "磅单设置"))
        self.previewPushButton.setText(_translate("balanceSetup", "预览空榜单"))
        self.defaultPushButton.setText(_translate("balanceSetup", "将当前磅单设置为使用磅单"))
        self.exitPushButton.setText(_translate("balanceSetup", "退  出"))

