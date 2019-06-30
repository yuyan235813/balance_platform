# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'com_setup_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ComSetupForm(object):
    def setupUi(self, ComSetupForm):
        ComSetupForm.setObjectName("ComSetupForm")
        ComSetupForm.resize(300, 180)
        ComSetupForm.setMinimumSize(QtCore.QSize(300, 180))
        ComSetupForm.setMaximumSize(QtCore.QSize(300, 180))
        self.horizontalLayout = QtWidgets.QHBoxLayout(ComSetupForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(ComSetupForm)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.issueComboBox = QtWidgets.QComboBox(self.groupBox)
        self.issueComboBox.setEditable(False)
        self.issueComboBox.setObjectName("issueComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.issueComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.readComboBox = QtWidgets.QComboBox(self.groupBox)
        self.readComboBox.setObjectName("readComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.readComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.barrierComboBox = QtWidgets.QComboBox(self.groupBox)
        self.barrierComboBox.setObjectName("barrierComboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.barrierComboBox)
        self.savePushButton = QtWidgets.QPushButton(self.groupBox)
        self.savePushButton.setObjectName("savePushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.savePushButton)
        self.cancelPushButton = QtWidgets.QPushButton(self.groupBox)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cancelPushButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(ComSetupForm)
        QtCore.QMetaObject.connectSlotsByName(ComSetupForm)

    def retranslateUi(self, ComSetupForm):
        _translate = QtCore.QCoreApplication.translate
        ComSetupForm.setWindowTitle(_translate("ComSetupForm", "无人值守设置"))
        self.groupBox.setTitle(_translate("ComSetupForm", "串口设置"))
        self.label.setText(_translate("ComSetupForm", "发卡器端口号"))
        self.label_2.setText(_translate("ComSetupForm", "读卡器端口号"))
        self.label_3.setText(_translate("ComSetupForm", "道闸端口号"))
        self.savePushButton.setText(_translate("ComSetupForm", "保  存"))
        self.cancelPushButton.setText(_translate("ComSetupForm", "取  消"))

