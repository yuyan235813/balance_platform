# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receiver_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Receiver_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(623, 295)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 512, 151))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.ReceiverNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverNameLineEdit.setMaxLength(15)
        self.ReceiverNameLineEdit.setObjectName("ReceiverNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ReceiverNameLineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.ReceiverPhoneLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverPhoneLineEdit.setObjectName("ReceiverPhoneLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ReceiverPhoneLineEdit)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.ReceiverBankLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverBankLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ReceiverBankLineEdit.setObjectName("ReceiverBankLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ReceiverBankLineEdit)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.ReceiverDutyLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverDutyLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ReceiverDutyLineEdit.setObjectName("ReceiverDutyLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ReceiverDutyLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.ReceiverContactLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverContactLineEdit.setMaxLength(15)
        self.ReceiverContactLineEdit.setObjectName("ReceiverContactLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ReceiverContactLineEdit)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.ReceiverAddressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverAddressLineEdit.setObjectName("ReceiverAddressLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ReceiverAddressLineEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.ReceiverCountLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverCountLineEdit.setObjectName("ReceiverCountLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ReceiverCountLineEdit)
        self.ReceiverIdLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverIdLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ReceiverIdLineEdit.setDragEnabled(True)
        self.ReceiverIdLineEdit.setReadOnly(True)
        self.ReceiverIdLineEdit.setPlaceholderText("")
        self.ReceiverIdLineEdit.setClearButtonEnabled(False)
        self.ReceiverIdLineEdit.setObjectName("ReceiverIdLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ReceiverIdLineEdit)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 220, 491, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.deletePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deletePushButton.setObjectName("deletePushButton")
        self.horizontalLayout_3.addWidget(self.deletePushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.savePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_3.addWidget(self.savePushButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.horizontalLayout_3.setStretch(0, 6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "收货单位"))
        self.label_5.setText(_translate("Dialog", "供货单位："))
        self.label_8.setText(_translate("Dialog", "联系电话："))
        self.label_7.setText(_translate("Dialog", "开  户 行："))
        self.label_12.setText(_translate("Dialog", "税      号："))
        self.label_10.setText(_translate("Dialog", "联 系  人："))
        self.label_9.setText(_translate("Dialog", "地      址："))
        self.label_11.setText(_translate("Dialog", "账      号："))
        self.label_13.setText(_translate("Dialog", "单位序号："))
        self.deletePushButton.setText(_translate("Dialog", "删除"))
        self.savePushButton.setText(_translate("Dialog", "保存"))
        self.cancelPushButton.setText(_translate("Dialog", "取消"))

