# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poll_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_PollmainForm(object):
    def setupUi(self, PollmainForm):
        PollmainForm.setObjectName("Form")
        PollmainForm.resize(710, 489)
        self.layoutWidget = QtWidgets.QWidget(PollmainForm)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 270, 491, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.QueryPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.QueryPushButton.setObjectName("QueryPushButton")
        self.horizontalLayout_3.addWidget(self.QueryPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.horizontalLayout_3.setStretch(0, 6)
        self.groupBox = QtWidgets.QGroupBox(PollmainForm)
        self.groupBox.setGeometry(QtCore.QRect(70, 60, 571, 181))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.CarNoLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.CarNoLineEdit.setObjectName("CarNoLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CarNoLineEdit)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.balanceNoLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.balanceNoLineEdit.setObjectName("balanceNoLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.balanceNoLineEdit)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.SupplyNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyNameLineEdit.setObjectName("SupplyNameLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SupplyNameLineEdit)
        self.begindateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.begindateEdit.setCalendarPopup(True)
        self.begindateEdit.setObjectName("begindateEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.begindateEdit)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.CargoNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.CargoNameLineEdit.setObjectName("CargoNameLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CargoNameLineEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.ReceiverNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.ReceiverNameLineEdit.setObjectName("ReceiverNameLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ReceiverNameLineEdit)
        self.enddateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.enddateEdit.setCalendarPopup(True)
        self.enddateEdit.setObjectName("enddateEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.enddateEdit)
        self.UnCompleteradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.UnCompleteradioButton.setObjectName("UnCompleteradioButton")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.UnCompleteradioButton)
        self.CompleteradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.CompleteradioButton.setObjectName("CompleteradioButton")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.CompleteradioButton)
        self.AllradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.AllradioButton.setObjectName("AllradioButton")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.AllradioButton)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PollmainForm)
        QtCore.QMetaObject.connectSlotsByName(PollmainForm)

    def retranslateUi(self, PollmainForm):
        _translate = QtCore.QCoreApplication.translate
        PollmainForm.setWindowTitle(_translate("PollmainForm", "Form"))
        self.QueryPushButton.setText(_translate("PollmainForm", "查询"))
        self.cancelPushButton.setText(_translate("PollmainForm", "取消"))
        self.groupBox.setTitle(_translate("PollmainForm", "查询条件"))
        self.label_5.setText(_translate("PollmainForm", "起始时间："))
        self.label_8.setText(_translate("PollmainForm", "车      号："))
        self.label_7.setText(_translate("PollmainForm", "磅  单 号："))
        self.label_12.setText(_translate("PollmainForm", "供货单位："))
        self.label_10.setText(_translate("PollmainForm", "截至时间："))
        self.label_9.setText(_translate("PollmainForm", "货物名称："))
        self.label_11.setText(_translate("PollmainForm", "收货单位："))
        self.UnCompleteradioButton.setText(_translate("PollmainForm", "未完成"))
        self.CompleteradioButton.setText(_translate("PollmainForm", "完成"))
        self.AllradioButton.setText(_translate("PollmainForm", "全部"))

