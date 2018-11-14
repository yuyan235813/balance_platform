# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'role_manage.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_roleForm(object):
    def setupUi(self, roleForm):
        roleForm.setObjectName("roleForm")
        roleForm.resize(300, 160)
        roleForm.setMinimumSize(QtCore.QSize(300, 160))
        roleForm.setMaximumSize(QtCore.QSize(300, 250))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(roleForm)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(roleForm)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.roleLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.roleLineEdit.setObjectName("roleLineEdit")
        self.horizontalLayout_4.addWidget(self.roleLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.savePushButton = QtWidgets.QPushButton(self.groupBox)
        self.savePushButton.setObjectName("savePushButton")
        self.horizontalLayout.addWidget(self.savePushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelPushButton = QtWidgets.QPushButton(self.groupBox)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addWidget(self.groupBox)

        self.retranslateUi(roleForm)
        QtCore.QMetaObject.connectSlotsByName(roleForm)

    def retranslateUi(self, roleForm):
        _translate = QtCore.QCoreApplication.translate
        roleForm.setWindowTitle(_translate("roleForm", "角色管理"))
        self.label.setText(_translate("roleForm", "角    色："))
        self.savePushButton.setText(_translate("roleForm", "保  存"))
        self.cancelPushButton.setText(_translate("roleForm", "取  消"))

