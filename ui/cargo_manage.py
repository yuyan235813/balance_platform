# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargo_manage.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cargo_ManageForm(object):
    def setupUi(self, cargo_ManageForm):
        cargo_ManageForm.setObjectName("Form")
        cargo_ManageForm.resize(832, 555)
        self.tableView = QtWidgets.QTableView(cargo_ManageForm)
        self.tableView.setStyleSheet("QTableView QHeaderView::section { background-color:#dadada}")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setGeometry(QtCore.QRect(150, 70, 531, 192))
        self.tableView.setObjectName("tableView")
        self.layoutWidget = QtWidgets.QWidget(cargo_ManageForm)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 440, 491, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.savePushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_3.addWidget(self.savePushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_3.addWidget(self.cancelPushButton)
        self.horizontalLayout_3.setStretch(0, 6)
        self.groupBox = QtWidgets.QGroupBox(cargo_ManageForm)
        self.groupBox.setGeometry(QtCore.QRect(150, 270, 512, 71))
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
        self.CargoNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.CargoNameLineEdit.setMaxLength(15)
        self.CargoNameLineEdit.setObjectName("CargoNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CargoNameLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.CargopriceLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.CargopriceLineEdit.setMaxLength(15)
        self.CargopriceLineEdit.setObjectName("CargopriceLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CargopriceLineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(cargo_ManageForm)
        QtCore.QMetaObject.connectSlotsByName(cargo_ManageForm)

    def retranslateUi(self, cargo_ManageForm):
        _translate = QtCore.QCoreApplication.translate
        cargo_ManageForm.setWindowTitle(_translate("cargo_ManageForm", "货物管理"))
        self.savePushButton.setText(_translate("cargo_ManageForm", "保存"))
        self.cancelPushButton.setText(_translate("cargo_ManageForm", "取消"))
        self.groupBox.setTitle(_translate("cargo_ManageForm", "货物管理"))
        self.label_5.setText(_translate("cargo_ManageForm", "货物名称："))
        self.label_8.setText(_translate("cargo_ManageForm", "单      价："))

