# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'params_setup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_paramsSetupForm(object):
    def setupUi(self, paramsSetupForm):
        paramsSetupForm.setObjectName("paramsSetupForm")
        paramsSetupForm.resize(530, 460)
        paramsSetupForm.setMinimumSize(QtCore.QSize(450, 440))
        paramsSetupForm.setMaximumSize(QtCore.QSize(530, 460))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(paramsSetupForm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(paramsSetupForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)
        self.dataComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.dataComboBox.setEditable(True)
        self.dataComboBox.setObjectName("dataComboBox")
        self.gridLayout.addWidget(self.dataComboBox, 2, 1, 1, 1)
        self.baudComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.baudComboBox.setEditable(True)
        self.baudComboBox.setObjectName("baudComboBox")
        self.gridLayout.addWidget(self.baudComboBox, 0, 4, 1, 1)
        self.verifyComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.verifyComboBox.setEditable(True)
        self.verifyComboBox.setObjectName("verifyComboBox")
        self.gridLayout.addWidget(self.verifyComboBox, 0, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.stopComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.stopComboBox.setEditable(True)
        self.stopComboBox.setObjectName("stopComboBox")
        self.gridLayout.addWidget(self.stopComboBox, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.portComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.portComboBox.setEditable(True)
        self.portComboBox.setObjectName("portComboBox")
        self.gridLayout.addWidget(self.portComboBox, 0, 1, 1, 1)
        self.verifyPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.verifyPushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.verifyPushButton.setObjectName("verifyPushButton")
        self.gridLayout.addWidget(self.verifyPushButton, 0, 8, 1, 1)
        self.portPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.portPushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.portPushButton.setObjectName("portPushButton")
        self.gridLayout.addWidget(self.portPushButton, 0, 2, 1, 1)
        self.dataPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.dataPushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.dataPushButton.setObjectName("dataPushButton")
        self.gridLayout.addWidget(self.dataPushButton, 2, 2, 1, 1)
        self.stopPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.stopPushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.stopPushButton.setObjectName("stopPushButton")
        self.gridLayout.addWidget(self.stopPushButton, 2, 5, 1, 1)
        self.baudPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.baudPushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.baudPushButton.setObjectName("baudPushButton")
        self.gridLayout.addWidget(self.baudPushButton, 0, 5, 1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(paramsSetupForm)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.ip1LineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ip1LineEdit.setMaxLength(15)
        self.ip1LineEdit.setObjectName("ip1LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ip1LineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.user1LineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.user1LineEdit.setObjectName("user1LineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.user1LineEdit)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.pwd1LineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.pwd1LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd1LineEdit.setObjectName("pwd1LineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pwd1LineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.ip1LineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.ip1LineEdit_2.setMaxLength(15)
        self.ip1LineEdit_2.setObjectName("ip1LineEdit_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ip1LineEdit_2)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.user2LineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.user2LineEdit.setObjectName("user2LineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.user2LineEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.pwd2LineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.pwd2LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd2LineEdit.setObjectName("pwd2LineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pwd2LineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.camera1CheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.camera1CheckBox.setObjectName("camera1CheckBox")
        self.horizontalLayout.addWidget(self.camera1CheckBox)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.camera2CheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.camera2CheckBox.setObjectName("camera2CheckBox")
        self.horizontalLayout.addWidget(self.camera2CheckBox)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.savePushButton = QtWidgets.QPushButton(paramsSetupForm)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_3.addWidget(self.savePushButton)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.cancelPushButton = QtWidgets.QPushButton(paramsSetupForm)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.horizontalLayout_3.setStretch(0, 6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 1)
        self.groupBox.raise_()
        self.groupBox_2.raise_()

        self.retranslateUi(paramsSetupForm)
        QtCore.QMetaObject.connectSlotsByName(paramsSetupForm)

    def retranslateUi(self, paramsSetupForm):
        _translate = QtCore.QCoreApplication.translate
        paramsSetupForm.setWindowTitle(_translate("paramsSetupForm", "参数设置"))
        self.groupBox_2.setTitle(_translate("paramsSetupForm", "通信参数设置"))
        self.label_2.setText(_translate("paramsSetupForm", "奇偶校验:"))
        self.label_4.setText(_translate("paramsSetupForm", "数据位:"))
        self.label.setText(_translate("paramsSetupForm", "端口号:"))
        self.label_3.setText(_translate("paramsSetupForm", "波特率:"))
        self.label_6.setText(_translate("paramsSetupForm", "停止位:"))
        self.portComboBox.setWhatsThis(_translate("paramsSetupForm", "<html><head/><body><p>COM1</p><p>COM2</p><p>COM3</p><p>COM4</p><p>COM5</p><p>COM6</p><p>COM7</p><p>COM8</p><p>COM9</p><p>COM10</p></body></html>"))
        self.verifyPushButton.setText(_translate("paramsSetupForm", "…"))
        self.portPushButton.setText(_translate("paramsSetupForm", "…"))
        self.dataPushButton.setText(_translate("paramsSetupForm", "…"))
        self.stopPushButton.setText(_translate("paramsSetupForm", "…"))
        self.baudPushButton.setText(_translate("paramsSetupForm", "…"))
        self.groupBox.setTitle(_translate("paramsSetupForm", "视频参数设置"))
        self.label_8.setText(_translate("paramsSetupForm", "用户名1:"))
        self.label_7.setText(_translate("paramsSetupForm", "密码1:"))
        self.label_5.setText(_translate("paramsSetupForm", "IP地址1:"))
        self.label_10.setText(_translate("paramsSetupForm", "IP地址2:"))
        self.label_9.setText(_translate("paramsSetupForm", "用户名2:"))
        self.label_11.setText(_translate("paramsSetupForm", "密码2:"))
        self.camera1CheckBox.setText(_translate("paramsSetupForm", "是否启动摄像头1"))
        self.camera2CheckBox.setText(_translate("paramsSetupForm", "是否启动摄像头2"))
        self.savePushButton.setText(_translate("paramsSetupForm", "保存"))
        self.cancelPushButton.setText(_translate("paramsSetupForm", "取消"))

