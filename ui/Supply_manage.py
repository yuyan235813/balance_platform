# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Supply_manage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 450)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(80, 220, 512, 151))
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
        self.SupplyNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyNameLineEdit.setMaxLength(15)
        self.SupplyNameLineEdit.setObjectName("SupplyNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.SupplyNameLineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.SupplyPhoneLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyPhoneLineEdit.setObjectName("SupplyPhoneLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SupplyPhoneLineEdit)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.SupplyBankLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyBankLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SupplyBankLineEdit.setObjectName("SupplyBankLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SupplyBankLineEdit)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.SupplyDutyLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyDutyLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SupplyDutyLineEdit.setObjectName("SupplyDutyLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SupplyDutyLineEdit)
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
        self.SupplyContactLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyContactLineEdit.setMaxLength(15)
        self.SupplyContactLineEdit.setObjectName("SupplyContactLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.SupplyContactLineEdit)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.SupplyAddressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyAddressLineEdit.setObjectName("SupplyAddressLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SupplyAddressLineEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.SupplyCountLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyCountLineEdit.setObjectName("SupplyCountLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.SupplyCountLineEdit)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.SupplyIDLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.SupplyIDLineEdit.setReadOnly(True)
        self.SupplyIDLineEdit.setObjectName("SupplyIDLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.SupplyIDLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 390, 521, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.savePushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.savePushButton_3.setObjectName("savePushButton_3")
        self.horizontalLayout_3.addWidget(self.savePushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.savePushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.savePushButton_2.setObjectName("savePushButton_2")
        self.horizontalLayout_3.addWidget(self.savePushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.savePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_3.addWidget(self.savePushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.cancelPushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton_2.setObjectName("cancelPushButton_2")
        self.horizontalLayout_3.addWidget(self.cancelPushButton_2)
        self.horizontalLayout_3.setStretch(0, 6)
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(80, 20, 531, 192))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "供货单位管理"))
        self.groupBox.setTitle(_translate("Form", "供货单位"))
        self.label_5.setText(_translate("Form", "供货单位："))
        self.label_8.setText(_translate("Form", "联系电话："))
        self.label_7.setText(_translate("Form", "开  户 行："))
        self.label_12.setText(_translate("Form", "税      号："))
        self.label_10.setText(_translate("Form", "联系人："))
        self.label_9.setText(_translate("Form", "地   址："))
        self.label_11.setText(_translate("Form", "账   号："))
        self.label_13.setText(_translate("Form", "序   号"))
        self.savePushButton_3.setText(_translate("Form", "删除"))
        self.savePushButton_2.setText(_translate("Form", "修改"))
        self.savePushButton.setText(_translate("Form", "添加"))
        self.cancelPushButton.setText(_translate("Form", "取消"))
        self.cancelPushButton_2.setText(_translate("Form", "清空"))

