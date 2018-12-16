# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poll_result.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PollResultForm(object):
    def setupUi(self, PollResultForm):
        PollResultForm.setObjectName("PollResultForm")
        PollResultForm.resize(827, 459)
        self.tableView = QtWidgets.QTableView(PollResultForm)
        self.tableView.setGeometry(QtCore.QRect(70, 80, 721, 192))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.printPushButton = QtWidgets.QPushButton(PollResultForm)
        self.printPushButton.setGeometry(QtCore.QRect(450, 300, 75, 23))
        font = QtGui.QFont()
        font.setKerning(True)
        self.printPushButton.setFont(font)
        self.printPushButton.setObjectName("printPushButton")
        self.excelPushButton_2 = QtWidgets.QPushButton(PollResultForm)
        self.excelPushButton_2.setGeometry(QtCore.QRect(360, 300, 75, 23))
        font = QtGui.QFont()
        font.setKerning(True)
        self.excelPushButton_2.setFont(font)
        self.excelPushButton_2.setObjectName("excelPushButton_2")

        self.retranslateUi(PollResultForm)
        QtCore.QMetaObject.connectSlotsByName(PollResultForm)

    def retranslateUi(self, PollResultForm):
        _translate = QtCore.QCoreApplication.translate
        PollResultForm.setWindowTitle(_translate("PollResultForm", "Form"))
        self.printPushButton.setText(_translate("PollResultForm", "打印"))
        self.excelPushButton_2.setText(_translate("PollResultForm", "导出"))

