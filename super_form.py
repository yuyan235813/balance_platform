#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtSql
from ui.super_form import Ui_superForm
import logging


class SuperForm(QtWidgets.QWidget, Ui_superForm):
    """
    超级管理界面
    """
    def __init__(self):
        super(SuperForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        if QtSql.QSqlDatabase.contains("qt_sql_default_connection"):
            self.db = QtSql.QSqlDatabase.database("qt_sql_default_connection")
        else:
            self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("rmf/db/balance.db")
        self.queryPushButton.clicked.connect(self.__query_data)
        self.addPushButton.clicked.connect(self.__add_data)
        self.savePushButton.clicked.connect(self.__save_data)
        self.deletePushButton.clicked.connect(self.__delete_data)
        self.cancelPushButton.clicked.connect(self.close)
        self.tableComboBox.currentTextChanged.connect(self.__set_column)
        self.db_model = QtSql.QSqlTableModel()

    def show(self):
        super().show()
        self.__init_data()

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        self.tableView.setModel(None)
        self.tableComboBox.clear()
        if self.db.open():
            tables = self.db.tables()
            tables = [table for table in tables if table.startswith("t_")]
            self.tableComboBox.addItems(tables)
        self.whereLineEdit.clear()
        self.sortComboBox1.clear()
        self.tableView.setItemDelegateForColumn(0, ReadonlyDelegate(self))

    def __set_column(self, table):
        """
        设置字段
        :param table:
        :return:
        """
        self.sortComboBox1.clear()
        if self.db.open():
            self.db_model.setTable(table)
            column_count = self.db_model.columnCount()
            for idx in range(column_count):
                header = self.db_model.headerData(idx, Qt.Horizontal)
                self.sortComboBox1.addItem(header)

    def __query_data(self):
        """
        查询数据
        :return:
        """
        table = self.tableComboBox.currentText()
        filter = self.whereLineEdit.text()
        order = self.sortComboBox1.currentText()
        order_type = Qt.DescendingOrder if self.sortComboBox2.currentText() == '降序' else Qt.AscendingOrder
        logging.info("table: %s; filter: %s; order: %s" % (table, filter, order))
        if self.db.open():
            self.db_model.setTable(table)
            self.db_model.setFilter(filter)
            idx = self.db_model.fieldIndex(order)
            self.db_model.setSort(idx, order_type)
            self.db_model.select()
            self.tableView.setModel(self.db_model)

    def __add_data(self):
        """
        添加数据
        :return:
        """
        logging.info('add data')
        self.db_model.insertRow(self.db_model.rowCount())

    def __save_data(self, without_info=False):
        """
        保存数据
        :return:
        """
        if self.db_model.submitAll():
            if not without_info:
                QtWidgets.QMessageBox.information(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
            self.__query_data()
        else:
            if not without_info:
                QtWidgets.QMessageBox.information(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)

    def __delete_data(self):
        """
        删除数据
        :return:
        """
        current_row = self.tableView.currentIndex().row()
        if current_row != -1:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '本程序',
                                                   "是否要删除记录 id = %s？" % self.db_model.index(current_row, 0).data(),
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                logging.info("delete id = %s" % self.db_model.index(current_row, 0).data())
                self.db_model.removeRow(current_row)
                self.__save_data(True)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的记录！", QtWidgets.QMessageBox.Ok)

    def closeEvent(self, a0):
        """
        关闭事件
        :param a0:
        :return:
        """
        super(SuperForm, self).closeEvent(a0)
        self.tableView.setModel(None)


class ReadonlyDelegate(QtWidgets.QItemDelegate):
    """
    性别列
    """
    def __init__(self, parent):
        super(ReadonlyDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        return None


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = SuperForm()
    myshow.show()
    sys.exit(app.exec_())