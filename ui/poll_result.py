# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poll_result.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PollResultForm(object):
    def setupUi(self, PollResultForm):
        PollResultForm.setObjectName("Form")
        PollResultForm.resize(827, 459)
        self.tableView = QtWidgets.QTableView(PollResultForm)
        self.tableView.setGeometry(QtCore.QRect(70, 80, 721, 192))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(PollResultForm)
        QtCore.QMetaObject.connectSlotsByName(PollResultForm)

    def retranslateUi(self, PollResultForm):
        _translate = QtCore.QCoreApplication.translate
        PollResultForm.setWindowTitle(_translate("PollResultForm", "查询结果"))

