#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from functools import partial
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.car_manage import Ui_carManageForm
from car_no_dialog_form import CarNoDialogForm
from utils.sqllite_util import EasySqlite


class CarManageForm(QtWidgets.QWidget, Ui_carManageForm):
    """
    车辆管理
    """
    def __init__(self):
        super(CarManageForm, self).__init__()
        self.setupUi(self)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.__init_data()
        self.cancelPushButton.clicked.connect(self.close)
        self.addPushButton.clicked.connect(self.__add_data)
        self.deletePushButton.clicked.connect(self.__delete_data)
        self.savePushButton.clicked.connect(self.__save_data)
        self.pushButton.clicked.connect(self.__show_dialog)
        self.dialog = CarNoDialogForm()
        self.dialog.my_signal.connect(self.carNoLineEdit.setText)

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        header = ('车牌号', '皮重', '修改时间')
        query_sql = 'select car_no, leather_weight, add_time from t_car order by add_time desc;'
        data_list = self.db.query(query_sql)
        row_no, col_no = len(data_list), len(header)
        model = QStandardItemModel(row_no, col_no)
        model.setHorizontalHeaderLabels(header)
        for row in range(row_no):
            values = list(data_list[row].values())
            for col in range(col_no):
                item = QStandardItem(str(values[col]))
                model.setItem(row, col, item)
        self.tableView.setModel(model)
        self.tableView.doubleClicked.connect(lambda x: self.__display_data(data_list[int(x.row())]))

    def __display_data(self, data):
        """
        返显数据
        :param data:
        :return:
        """
        self.carNoLineEdit.setText(str(data.get('car_no', '')))
        self.doubleSpinBox.setValue(data.get('leather_weight', 0.0))

    def __show_dialog(self):
        """
        显示车牌号键盘
        :return:
        """
        if self.dialog.isVisible():
            self.dialog.setVisible(False)
            return
        self.dialog.show()

    def moveEvent(self, a0):
        """
        移动窗口事件
        :param a0:
        :return:
        """
        super().moveEvent(a0)
        point = a0.pos()
        point.setX(point.x() + 50)
        point.setY(point.y() + 300)
        self.dialog.move(point)

    def __add_data(self):
        """
        添加数据
        :return:
        """
        pass

    def __delete_data(self):
        """
        删除数据
        :return:
        """
        pass

    def __save_data(self):
        """
        保存数据
        :return:
        """

    def closeEvent(self, event):
        self.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = CarManageForm()
    myshow.show()
    sys.exit(app.exec_())