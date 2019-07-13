# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cardFrom(object):
    def setupUi(self, cardFrom):
        cardFrom.setObjectName("cardFrom")
        cardFrom.setEnabled(True)
        cardFrom.resize(880, 835)
        self.tableView = QtWidgets.QTableView(cardFrom)
        self.tableView.setGeometry(QtCore.QRect(110, 160, 661, 271))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.addPushButton = QtWidgets.QPushButton(cardFrom)
        self.addPushButton.setGeometry(QtCore.QRect(140, 760, 75, 23))
        self.addPushButton.setObjectName("addPushButton")
        self.issuePushButton = QtWidgets.QPushButton(cardFrom)
        self.issuePushButton.setGeometry(QtCore.QRect(360, 760, 75, 23))
        self.issuePushButton.setObjectName("issuePushButton")
        self.readPushButton = QtWidgets.QPushButton(cardFrom)
        self.readPushButton.setGeometry(QtCore.QRect(460, 760, 75, 23))
        self.readPushButton.setObjectName("readPushButton")
        self.savePushButton = QtWidgets.QPushButton(cardFrom)
        self.savePushButton.setGeometry(QtCore.QRect(250, 760, 75, 23))
        self.savePushButton.setObjectName("savePushButton")
        self.deletePushButton = QtWidgets.QPushButton(cardFrom)
        self.deletePushButton.setGeometry(QtCore.QRect(550, 760, 75, 23))
        self.deletePushButton.setObjectName("deletePushButton")
        self.cancelPushButton = QtWidgets.QPushButton(cardFrom)
        self.cancelPushButton.setGeometry(QtCore.QRect(650, 760, 75, 23))
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.queryPushButton = QtWidgets.QPushButton(cardFrom)
        self.queryPushButton.setGeometry(QtCore.QRect(634, 89, 75, 23))
        self.queryPushButton.setObjectName("queryPushButton")
        self.gridLayoutWidget = QtWidgets.QWidget(cardFrom)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 490, 581, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.credNoLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.credNoLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.credNoLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.credNoLineEdit.setObjectName("credNoLineEdit")
        self.gridLayout_2.addWidget(self.credNoLineEdit, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 4, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.addressLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.addressLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.addressLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.gridLayout_2.addWidget(self.addressLineEdit, 3, 1, 1, 1)
        self.extraDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.extraDoubleSpinBox.setObjectName("extraDoubleSpinBox")
        self.gridLayout_2.addWidget(self.extraDoubleSpinBox, 4, 3, 1, 1)
        self.carNoLineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.carNoLineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.carNoLineEdit_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carNoLineEdit_2.setObjectName("carNoLineEdit_2")
        self.gridLayout_2.addWidget(self.carNoLineEdit_2, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.enrollDateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.enrollDateEdit.setCalendarPopup(True)
        self.enrollDateEdit.setObjectName("enrollDateEdit")
        self.gridLayout_2.addWidget(self.enrollDateEdit, 3, 3, 1, 1)
        self.userNameLineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userNameLineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.userNameLineEdit_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.userNameLineEdit_2.setObjectName("userNameLineEdit_2")
        self.gridLayout_2.addWidget(self.userNameLineEdit_2, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 2, 1, 1)
        self.cardTypeComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cardTypeComboBox.setObjectName("cardTypeComboBox")
        self.cardTypeComboBox.addItem("")
        self.cardTypeComboBox.addItem("")
        self.cardTypeComboBox.addItem("")
        self.gridLayout_2.addWidget(self.cardTypeComboBox, 2, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 4, 1, 1)
        self.genderComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.genderComboBox.setObjectName("genderComboBox")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.gridLayout_2.addWidget(self.genderComboBox, 0, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 3, 4, 1, 1)
        self.priceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.priceDoubleSpinBox.setObjectName("priceDoubleSpinBox")
        self.gridLayout_2.addWidget(self.priceDoubleSpinBox, 4, 5, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 2, 4, 1, 1)
        self.validDateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.validDateEdit.setCalendarPopup(True)
        self.validDateEdit.setObjectName("validDateEdit")
        self.gridLayout_2.addWidget(self.validDateEdit, 3, 5, 1, 1)
        self.isValidComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.isValidComboBox.setObjectName("isValidComboBox")
        self.isValidComboBox.addItem("")
        self.isValidComboBox.addItem("")
        self.gridLayout_2.addWidget(self.isValidComboBox, 2, 5, 1, 1)
        self.suppliercomboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.suppliercomboBox.setEditable(True)
        self.suppliercomboBox.setCurrentText("")
        self.suppliercomboBox.setObjectName("suppliercomboBox")
        self.gridLayout_2.addWidget(self.suppliercomboBox, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 4, 4, 1, 1)
        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.phoneNumberLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.phoneNumberLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.phoneNumberLineEdit.setMaxLength(11)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")
        self.gridLayout_2.addWidget(self.phoneNumberLineEdit, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 4, 1, 1)
        self.receivercomboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.receivercomboBox.setEditable(True)
        self.receivercomboBox.setObjectName("receivercomboBox")
        self.gridLayout_2.addWidget(self.receivercomboBox, 1, 3, 1, 1)
        self.cargocomboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cargocomboBox.setEditable(True)
        self.cargocomboBox.setObjectName("cargocomboBox")
        self.gridLayout_2.addWidget(self.cargocomboBox, 4, 1, 1, 1)
        self.issuedRadioButton = QtWidgets.QRadioButton(cardFrom)
        self.issuedRadioButton.setGeometry(QtCore.QRect(185, 128, 59, 16))
        self.issuedRadioButton.setChecked(True)
        self.issuedRadioButton.setObjectName("issuedRadioButton")
        self.userNameLineEdit = QtWidgets.QLineEdit(cardFrom)
        self.userNameLineEdit.setGeometry(QtCore.QRect(474, 66, 133, 25))
        self.userNameLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.userNameLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        self.supplierLineEdit = QtWidgets.QLineEdit(cardFrom)
        self.supplierLineEdit.setGeometry(QtCore.QRect(250, 97, 133, 25))
        self.supplierLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.supplierLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.supplierLineEdit.setObjectName("supplierLineEdit")
        self.endDateEdit = QtWidgets.QDateEdit(cardFrom)
        self.endDateEdit.setGeometry(QtCore.QRect(474, 40, 88, 20))
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setObjectName("endDateEdit")
        self.label_5 = QtWidgets.QLabel(cardFrom)
        self.label_5.setGeometry(QtCore.QRect(185, 97, 48, 16))
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(cardFrom)
        self.label.setGeometry(QtCore.QRect(409, 66, 36, 16))
        self.label.setObjectName("label")
        self.carNoLineEdit = QtWidgets.QLineEdit(cardFrom)
        self.carNoLineEdit.setGeometry(QtCore.QRect(250, 66, 133, 25))
        self.carNoLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.carNoLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.carNoLineEdit.setObjectName("carNoLineEdit")
        self.label_2 = QtWidgets.QLabel(cardFrom)
        self.label_2.setGeometry(QtCore.QRect(185, 40, 48, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(cardFrom)
        self.label_3.setGeometry(QtCore.QRect(409, 40, 48, 16))
        self.label_3.setObjectName("label_3")
        self.receiverLineEdit = QtWidgets.QLineEdit(cardFrom)
        self.receiverLineEdit.setGeometry(QtCore.QRect(474, 97, 133, 25))
        self.receiverLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.receiverLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.receiverLineEdit.setObjectName("receiverLineEdit")
        self.label_6 = QtWidgets.QLabel(cardFrom)
        self.label_6.setGeometry(QtCore.QRect(409, 97, 48, 16))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(cardFrom)
        self.label_4.setGeometry(QtCore.QRect(185, 66, 36, 16))
        self.label_4.setObjectName("label_4")
        self.unissuedRadioButton = QtWidgets.QRadioButton(cardFrom)
        self.unissuedRadioButton.setGeometry(QtCore.QRect(409, 128, 59, 16))
        self.unissuedRadioButton.setObjectName("unissuedRadioButton")
        self.beginDateEdit = QtWidgets.QDateEdit(cardFrom)
        self.beginDateEdit.setGeometry(QtCore.QRect(250, 40, 88, 20))
        self.beginDateEdit.setCalendarPopup(True)
        self.beginDateEdit.setObjectName("beginDateEdit")

        self.retranslateUi(cardFrom)
        self.cardTypeComboBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(cardFrom)

    def retranslateUi(self, cardFrom):
        _translate = QtCore.QCoreApplication.translate
        cardFrom.setWindowTitle(_translate("cardFrom", "卡片信息管理"))
        self.addPushButton.setText(_translate("cardFrom", "添  加"))
        self.issuePushButton.setText(_translate("cardFrom", "发  行"))
        self.readPushButton.setText(_translate("cardFrom", "读  卡"))
        self.savePushButton.setText(_translate("cardFrom", "修  改"))
        self.deletePushButton.setText(_translate("cardFrom", "删  除"))
        self.cancelPushButton.setText(_translate("cardFrom", "取  消"))
        self.queryPushButton.setText(_translate("cardFrom", "查  询"))
        self.label_9.setText(_translate("cardFrom", "姓  名"))
        self.label_16.setText(_translate("cardFrom", "登记日期"))
        self.label_20.setText(_translate("cardFrom", "另  扣"))
        self.label_10.setText(_translate("cardFrom", "供货单位"))
        self.label_8.setText(_translate("cardFrom", "收货单位"))
        self.enrollDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))
        self.label_13.setText(_translate("cardFrom", "卡类型"))
        self.cardTypeComboBox.setItemText(0, _translate("cardFrom", "月卡"))
        self.cardTypeComboBox.setItemText(1, _translate("cardFrom", "临时卡"))
        self.cardTypeComboBox.setItemText(2, _translate("cardFrom", "免费卡"))
        self.label_14.setText(_translate("cardFrom", "证件号码"))
        self.label_7.setText(_translate("cardFrom", "车牌号"))
        self.label_18.setText(_translate("cardFrom", "货物名称"))
        self.label_12.setText(_translate("cardFrom", "性  别"))
        self.genderComboBox.setItemText(0, _translate("cardFrom", "男"))
        self.genderComboBox.setItemText(1, _translate("cardFrom", "女"))
        self.label_19.setText(_translate("cardFrom", "地  址"))
        self.label_15.setText(_translate("cardFrom", "有效期"))
        self.label_17.setText(_translate("cardFrom", "是否有效"))
        self.validDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))
        self.isValidComboBox.setItemText(0, _translate("cardFrom", "是"))
        self.isValidComboBox.setItemText(1, _translate("cardFrom", "否"))
        self.label_21.setText(_translate("cardFrom", "价  格"))
        self.label_11.setText(_translate("cardFrom", "联系电话"))
        self.issuedRadioButton.setText(_translate("cardFrom", "已发行"))
        self.endDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))
        self.label_5.setText(_translate("cardFrom", "供货单位"))
        self.label.setText(_translate("cardFrom", "姓  名"))
        self.label_2.setText(_translate("cardFrom", "起始日期"))
        self.label_3.setText(_translate("cardFrom", "结束日期"))
        self.label_6.setText(_translate("cardFrom", "收货单位"))
        self.label_4.setText(_translate("cardFrom", "车牌号"))
        self.unissuedRadioButton.setText(_translate("cardFrom", "未发行"))
        self.beginDateEdit.setDisplayFormat(_translate("cardFrom", "yyyy-M-d"))

