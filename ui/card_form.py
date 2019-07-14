# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cardFrom(object):
    def setupUi(self, cardFrom):
        cardFrom.setObjectName("cardFrom")
        cardFrom.setEnabled(True)
        cardFrom.resize(750, 650)
        cardFrom.setMinimumSize(QtCore.QSize(750, 650))
        cardFrom.setMaximumSize(QtCore.QSize(750, 650))
        self.groupBox = QtWidgets.QGroupBox(cardFrom)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 734, 579))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.issuedRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.issuedRadioButton.setChecked(True)
        self.issuedRadioButton.setObjectName("issuedRadioButton")
        self.gridLayout.addWidget(self.issuedRadioButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.endDateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setObjectName("endDateEdit")
        self.gridLayout.addWidget(self.endDateEdit, 0, 4, 1, 1)
        self.userNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.userNameLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.userNameLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        self.gridLayout.addWidget(self.userNameLineEdit, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.supplierLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.supplierLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.supplierLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.supplierLineEdit.setObjectName("supplierLineEdit")
        self.gridLayout.addWidget(self.supplierLineEdit, 2, 1, 1, 1)
        self.beginDateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.beginDateEdit.setCalendarPopup(True)
        self.beginDateEdit.setObjectName("beginDateEdit")
        self.gridLayout.addWidget(self.beginDateEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.receiverLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.receiverLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.receiverLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.receiverLineEdit.setObjectName("receiverLineEdit")
        self.gridLayout.addWidget(self.receiverLineEdit, 2, 4, 1, 1)
        self.unissuedRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.unissuedRadioButton.setObjectName("unissuedRadioButton")
        self.gridLayout.addWidget(self.unissuedRadioButton, 3, 4, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.carNoLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.carNoLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.carNoLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carNoLineEdit.setObjectName("carNoLineEdit")
        self.horizontalLayout_3.addWidget(self.carNoLineEdit)
        self.carNoPushButton = QtWidgets.QPushButton(self.groupBox)
        self.carNoPushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.carNoPushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.carNoPushButton.setObjectName("carNoPushButton")
        self.horizontalLayout_3.addWidget(self.carNoPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 4)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.queryPushButton = QtWidgets.QPushButton(self.groupBox)
        self.queryPushButton.setMinimumSize(QtCore.QSize(80, 80))
        self.queryPushButton.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.queryPushButton.setFont(font)
        self.queryPushButton.setObjectName("queryPushButton")
        self.horizontalLayout.addWidget(self.queryPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tableView)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.priceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.priceDoubleSpinBox.setObjectName("priceDoubleSpinBox")
        self.gridLayout_2.addWidget(self.priceDoubleSpinBox, 4, 8, 1, 1)
        self.genderComboBox = QtWidgets.QComboBox(self.groupBox)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.gridLayout_2.addWidget(self.genderComboBox, 0, 8, 1, 1)
        self.validDateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.validDateEdit.setCalendarPopup(True)
        self.validDateEdit.setObjectName("validDateEdit")
        self.gridLayout_2.addWidget(self.validDateEdit, 3, 8, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 7, 1, 1)
        self.suppliercomboBox = QtWidgets.QComboBox(self.groupBox)
        self.suppliercomboBox.setEditable(True)
        self.suppliercomboBox.setCurrentText("")
        self.suppliercomboBox.setObjectName("suppliercomboBox")
        self.gridLayout_2.addWidget(self.suppliercomboBox, 1, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 7, 1, 1)
        self.receivercomboBox = QtWidgets.QComboBox(self.groupBox)
        self.receivercomboBox.setEditable(True)
        self.receivercomboBox.setObjectName("receivercomboBox")
        self.gridLayout_2.addWidget(self.receivercomboBox, 1, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 7, 1, 1)
        self.cargocomboBox = QtWidgets.QComboBox(self.groupBox)
        self.cargocomboBox.setEditable(True)
        self.cargocomboBox.setObjectName("cargocomboBox")
        self.gridLayout_2.addWidget(self.cargocomboBox, 4, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 4, 7, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 2, 7, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 1)
        self.cardTypeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.cardTypeComboBox.setObjectName("cardTypeComboBox")
        self.cardTypeComboBox.addItem("")
        self.cardTypeComboBox.addItem("")
        self.cardTypeComboBox.addItem("")
        self.gridLayout_2.addWidget(self.cardTypeComboBox, 2, 5, 1, 1)
        self.isValidComboBox = QtWidgets.QComboBox(self.groupBox)
        self.isValidComboBox.setObjectName("isValidComboBox")
        self.isValidComboBox.addItem("")
        self.isValidComboBox.addItem("")
        self.gridLayout_2.addWidget(self.isValidComboBox, 2, 8, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.phoneNumberLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.phoneNumberLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.phoneNumberLineEdit.setMaxLength(11)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")
        self.gridLayout_2.addWidget(self.phoneNumberLineEdit, 1, 8, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.enrollDateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.enrollDateEdit.setCalendarPopup(True)
        self.enrollDateEdit.setObjectName("enrollDateEdit")
        self.gridLayout_2.addWidget(self.enrollDateEdit, 3, 5, 1, 1)
        self.userNameLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.userNameLineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.userNameLineEdit_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.userNameLineEdit_2.setObjectName("userNameLineEdit_2")
        self.gridLayout_2.addWidget(self.userNameLineEdit_2, 0, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 4, 4, 1, 1)
        self.credNoLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.credNoLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.credNoLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.credNoLineEdit.setObjectName("credNoLineEdit")
        self.gridLayout_2.addWidget(self.credNoLineEdit, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 4, 1, 1)
        self.addressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.addressLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.addressLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.gridLayout_2.addWidget(self.addressLineEdit, 3, 2, 1, 1)
        self.extraDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.extraDoubleSpinBox.setObjectName("extraDoubleSpinBox")
        self.gridLayout_2.addWidget(self.extraDoubleSpinBox, 4, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 5, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 6, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.carNoLineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.carNoLineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.carNoLineEdit_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carNoLineEdit_2.setObjectName("carNoLineEdit_2")
        self.horizontalLayout_4.addWidget(self.carNoLineEdit_2)
        self.carNoPushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.carNoPushButton_2.setMinimumSize(QtCore.QSize(25, 25))
        self.carNoPushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.carNoPushButton_2.setObjectName("carNoPushButton_2")
        self.horizontalLayout_4.addWidget(self.carNoPushButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addPushButton = QtWidgets.QPushButton(self.groupBox)
        self.addPushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.addPushButton.setObjectName("addPushButton")
        self.horizontalLayout_2.addWidget(self.addPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.savePushButton = QtWidgets.QPushButton(self.groupBox)
        self.savePushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout_2.addWidget(self.savePushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.issuePushButton = QtWidgets.QPushButton(self.groupBox)
        self.issuePushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.issuePushButton.setObjectName("issuePushButton")
        self.horizontalLayout_2.addWidget(self.issuePushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.readPushButton = QtWidgets.QPushButton(self.groupBox)
        self.readPushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.readPushButton.setObjectName("readPushButton")
        self.horizontalLayout_2.addWidget(self.readPushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.deletePushButton = QtWidgets.QPushButton(self.groupBox)
        self.deletePushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.deletePushButton.setObjectName("deletePushButton")
        self.horizontalLayout_2.addWidget(self.deletePushButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.cancelPushButton = QtWidgets.QPushButton(self.groupBox)
        self.cancelPushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_2.addWidget(self.cancelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(cardFrom)
        self.cardTypeComboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(cardFrom)

    def retranslateUi(self, cardFrom):
        _translate = QtCore.QCoreApplication.translate
        cardFrom.setWindowTitle(_translate("cardFrom", "卡片信息管理"))
        self.groupBox.setTitle(_translate("cardFrom", "卡片管理"))
        self.issuedRadioButton.setText(_translate("cardFrom", "已发行"))
        self.endDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))
        self.label_2.setText(_translate("cardFrom", "起始日期"))
        self.beginDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))
        self.label_3.setText(_translate("cardFrom", "结束日期"))
        self.label.setText(_translate("cardFrom", "姓  名"))
        self.label_6.setText(_translate("cardFrom", "收货单位"))
        self.label_4.setText(_translate("cardFrom", "车牌号"))
        self.label_5.setText(_translate("cardFrom", "供货单位"))
        self.unissuedRadioButton.setText(_translate("cardFrom", "未发行"))
        self.carNoPushButton.setText(_translate("cardFrom", "…"))
        self.queryPushButton.setText(_translate("cardFrom", "查  询"))
        self.genderComboBox.setItemText(0, _translate("cardFrom", "男"))
        self.genderComboBox.setItemText(1, _translate("cardFrom", "女"))
        self.validDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))
        self.label_13.setText(_translate("cardFrom", "卡类型"))
        self.label_15.setText(_translate("cardFrom", "有效期"))
        self.label_19.setText(_translate("cardFrom", "地  址"))
        self.label_11.setText(_translate("cardFrom", "联系电话"))
        self.label_12.setText(_translate("cardFrom", "性  别"))
        self.label_21.setText(_translate("cardFrom", "价  格"))
        self.label_17.setText(_translate("cardFrom", "是否有效"))
        self.label_18.setText(_translate("cardFrom", "货物名称"))
        self.cardTypeComboBox.setItemText(0, _translate("cardFrom", "月卡"))
        self.cardTypeComboBox.setItemText(1, _translate("cardFrom", "临时卡"))
        self.cardTypeComboBox.setItemText(2, _translate("cardFrom", "免费卡"))
        self.isValidComboBox.setItemText(0, _translate("cardFrom", "是"))
        self.isValidComboBox.setItemText(1, _translate("cardFrom", "否"))
        self.label_14.setText(_translate("cardFrom", "证件号码"))
        self.label_7.setText(_translate("cardFrom", "车牌号"))
        self.enrollDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))
        self.label_20.setText(_translate("cardFrom", "另  扣"))
        self.label_9.setText(_translate("cardFrom", "姓  名"))
        self.label_10.setText(_translate("cardFrom", "供货单位"))
        self.label_8.setText(_translate("cardFrom", "收货单位"))
        self.label_16.setText(_translate("cardFrom", "登记日期"))
        self.carNoPushButton_2.setText(_translate("cardFrom", "…"))
        self.addPushButton.setText(_translate("cardFrom", "添  加"))
        self.savePushButton.setText(_translate("cardFrom", "修  改"))
        self.issuePushButton.setText(_translate("cardFrom", "发  行"))
        self.readPushButton.setText(_translate("cardFrom", "读  卡"))
        self.deletePushButton.setText(_translate("cardFrom", "删  除"))
        self.cancelPushButton.setText(_translate("cardFrom", "取  消"))

