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
        ComSetupForm.resize(320, 200)
        ComSetupForm.setMinimumSize(QtCore.QSize(320, 200))
        ComSetupForm.setMaximumSize(QtCore.QSize(320, 200))
        self.horizontalLayout = QtWidgets.QHBoxLayout(ComSetupForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(ComSetupForm)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.issueComboBox = QtWidgets.QComboBox(self.groupBox)
        self.issueComboBox.setEditable(False)
        self.issueComboBox.setObjectName("issueComboBox")
        self.gridLayout.addWidget(self.issueComboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.readComboBox1 = QtWidgets.QComboBox(self.groupBox)
        self.readComboBox1.setObjectName("readComboBox1")
        self.gridLayout.addWidget(self.readComboBox1, 1, 1, 1, 1)
        self.readCheckBox1 = QtWidgets.QCheckBox(self.groupBox)
        self.readCheckBox1.setObjectName("readCheckBox1")
        self.gridLayout.addWidget(self.readCheckBox1, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.readComboBox2 = QtWidgets.QComboBox(self.groupBox)
        self.readComboBox2.setObjectName("readComboBox2")
        self.gridLayout.addWidget(self.readComboBox2, 2, 1, 1, 1)
        self.readCheckBox2 = QtWidgets.QCheckBox(self.groupBox)
        self.readCheckBox2.setObjectName("readCheckBox2")
        self.gridLayout.addWidget(self.readCheckBox2, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.barrierComboBox = QtWidgets.QComboBox(self.groupBox)
        self.barrierComboBox.setObjectName("barrierComboBox")
        self.gridLayout.addWidget(self.barrierComboBox, 3, 1, 1, 1)
        self.savePushButton = QtWidgets.QPushButton(self.groupBox)
        self.savePushButton.setObjectName("savePushButton")
        self.gridLayout.addWidget(self.savePushButton, 4, 0, 1, 1)
        self.cancelPushButton = QtWidgets.QPushButton(self.groupBox)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.gridLayout.addWidget(self.cancelPushButton, 4, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(ComSetupForm)
        QtCore.QMetaObject.connectSlotsByName(ComSetupForm)

    def retranslateUi(self, ComSetupForm):
        _translate = QtCore.QCoreApplication.translate
        ComSetupForm.setWindowTitle(_translate("ComSetupForm", "无人值守设置"))
        self.groupBox.setTitle(_translate("ComSetupForm", "串口设置"))
        self.label.setText(_translate("ComSetupForm", "发卡器 端口号"))
        self.label_2.setText(_translate("ComSetupForm", "读卡器1端口号"))
        self.readCheckBox1.setText(_translate("ComSetupForm", "是否启用"))
        self.label_4.setText(_translate("ComSetupForm", "读卡器2端口号"))
        self.readCheckBox2.setText(_translate("ComSetupForm", "是否启用"))
        self.label_3.setText(_translate("ComSetupForm", "道闸 端口号"))
        self.savePushButton.setText(_translate("ComSetupForm", "保  存"))
        self.cancelPushButton.setText(_translate("ComSetupForm", "取  消"))

