# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'permission_setup.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_permissionSetupForm(object):
    def setupUi(self, permissionSetupForm):
        permissionSetupForm.setObjectName("permissionSetupForm")
        permissionSetupForm.resize(663, 575)
        self.permissionTabWidget = QtWidgets.QTabWidget(permissionSetupForm)
        self.permissionTabWidget.setGeometry(QtCore.QRect(340, 50, 280, 391))
        self.permissionTabWidget.setObjectName("permissionTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.optionTableWidget = QtWidgets.QTableWidget(self.tab)
        self.optionTableWidget.setObjectName("optionTableWidget")
        self.optionTableWidget.setColumnCount(0)
        self.optionTableWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.optionTableWidget)
        self.permissionTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.permissionTableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.permissionTableWidget.setObjectName("permissionTableWidget")
        self.permissionTableWidget.setColumnCount(0)
        self.permissionTableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.permissionTableWidget)
        self.permissionTabWidget.addTab(self.tab_2, "")
        self.userRoleQTabWidget = QtWidgets.QTabWidget(permissionSetupForm)
        self.userRoleQTabWidget.setGeometry(QtCore.QRect(20, 60, 251, 371))
        self.userRoleQTabWidget.setObjectName("userRoleQTabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.userListWidget = QtWidgets.QListWidget(self.tab_3)
        self.userListWidget.setObjectName("userListWidget")
        self.verticalLayout_2.addWidget(self.userListWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addUserPushButton = QtWidgets.QPushButton(self.tab_3)
        self.addUserPushButton.setObjectName("addUserPushButton")
        self.horizontalLayout_2.addWidget(self.addUserPushButton)
        self.deleteUserPushButton = QtWidgets.QPushButton(self.tab_3)
        self.deleteUserPushButton.setObjectName("deleteUserPushButton")
        self.horizontalLayout_2.addWidget(self.deleteUserPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.userRoleQTabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.roleListWidget = QtWidgets.QListWidget(self.tab_4)
        self.roleListWidget.setObjectName("roleListWidget")
        self.verticalLayout.addWidget(self.roleListWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addRolePushButton = QtWidgets.QPushButton(self.tab_4)
        self.addRolePushButton.setObjectName("addRolePushButton")
        self.horizontalLayout.addWidget(self.addRolePushButton)
        self.deleteRolePushButton = QtWidgets.QPushButton(self.tab_4)
        self.deleteRolePushButton.setObjectName("deleteRolePushButton")
        self.horizontalLayout.addWidget(self.deleteRolePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.userRoleQTabWidget.addTab(self.tab_4, "")
        self.savePushButton = QtWidgets.QPushButton(permissionSetupForm)
        self.savePushButton.setGeometry(QtCore.QRect(240, 500, 75, 23))
        self.savePushButton.setObjectName("savePushButton")
        self.cancelPushButton = QtWidgets.QPushButton(permissionSetupForm)
        self.cancelPushButton.setGeometry(QtCore.QRect(330, 500, 75, 23))
        self.cancelPushButton.setObjectName("cancelPushButton")

        self.retranslateUi(permissionSetupForm)
        self.permissionTabWidget.setCurrentIndex(1)
        self.userRoleQTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(permissionSetupForm)

    def retranslateUi(self, permissionSetupForm):
        _translate = QtCore.QCoreApplication.translate
        permissionSetupForm.setWindowTitle(_translate("permissionSetupForm", "Form"))
        self.permissionTabWidget.setTabText(self.permissionTabWidget.indexOf(self.tab), _translate("permissionSetupForm", "功能设置"))
        self.permissionTabWidget.setTabText(self.permissionTabWidget.indexOf(self.tab_2), _translate("permissionSetupForm", "权限设置"))
        self.addUserPushButton.setText(_translate("permissionSetupForm", "添加"))
        self.deleteUserPushButton.setText(_translate("permissionSetupForm", "删除"))
        self.userRoleQTabWidget.setTabText(self.userRoleQTabWidget.indexOf(self.tab_3), _translate("permissionSetupForm", "用户"))
        self.addRolePushButton.setText(_translate("permissionSetupForm", "添加"))
        self.deleteRolePushButton.setText(_translate("permissionSetupForm", "删除"))
        self.userRoleQTabWidget.setTabText(self.userRoleQTabWidget.indexOf(self.tab_4), _translate("permissionSetupForm", "角色"))
        self.savePushButton.setText(_translate("permissionSetupForm", "保存"))
        self.cancelPushButton.setText(_translate("permissionSetupForm", "取消"))

