# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car_manage_change.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 90)
        dialog.setMinimumSize(QtCore.QSize(400, 90))
        dialog.setMaximumSize(QtCore.QSize(400, 90))
        dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        dialog.setWhatsThis("")
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.carNoLineEdit = QtWidgets.QLineEdit(dialog)
        self.carNoLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.carNoLineEdit.setObjectName("carNoLineEdit")
        self.horizontalLayout.addWidget(self.carNoLineEdit)
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(dialog)
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(123131, 30))
        self.doubleSpinBox.setMaximum(9999999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okPushButton = QtWidgets.QPushButton(dialog)
        self.okPushButton.setObjectName("okPushButton")
        self.horizontalLayout_2.addWidget(self.okPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(dialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_2.addWidget(self.cancelPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "车辆管理-修改"))
        self.label.setText(_translate("dialog", "车号："))
        self.pushButton.setText(_translate("dialog", "……"))
        self.label_2.setText(_translate("dialog", "皮重："))
        self.okPushButton.setText(_translate("dialog", "确定"))
        self.cancelPushButton.setText(_translate("dialog", "取消"))

