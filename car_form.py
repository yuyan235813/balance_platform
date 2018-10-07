#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.car_manage import Ui_carManageForm
from car_no_dialog_form import CarNoDialogForm
from utils.sqllite_util import EasySqlite
from utils.normal_utils import get_cur_time


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
        self.tableView.doubleClicked.connect(self.__display_data)

    def __display_data(self, index):
        """
        返显数据
        :param index:
        :return:
        """
        car_no = self.tableView.model().index(index.row(), 0).data()
        leather_weight = self.tableView.model().index(index.row(), 1).data()
        self.carNoLineEdit.setText(str(car_no))
        self.doubleSpinBox.setValue(float(leather_weight))

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
        car_no = self.carNoLineEdit.text()
        leather_weight = self.doubleSpinBox.value()
        if len(car_no.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "车牌号不能为空！", QtWidgets.QMessageBox.Ok)
            return
        if leather_weight <= 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "重量必须为正数！", QtWidgets.QMessageBox.Ok)
            return
        repeat = False
        row_count = self.tableView.model().rowCount()
        for i in range(row_count):
            if car_no == self.tableView.model().index(i, 0).data():
                repeat = True
                break
        if repeat:
            QtWidgets.QMessageBox.warning(self, '本程序', "车牌号已经存在！", QtWidgets.QMessageBox.Ok)
            return
        cur_time = get_cur_time()
        items = (QStandardItem(car_no),
                 QStandardItem(str(round(leather_weight, 2))),
                 QStandardItem(cur_time))
        self.tableView.model().insertRow(0, items)

    def __delete_data(self):
        """
        删除数据
        :return:
        """
        current_row = self.tableView.currentIndex().row()
        status = self.tableView.model().removeRow(current_row)
        print(self.tableView.model().rowCount())
        if not status:
            QtWidgets.QMessageBox.warning(self, '本程序', "删除失败！", QtWidgets.QMessageBox.Ok)
            return

    def __save_data(self):
        """
        保存数据
        :return:
        """
        data = []
        model = self.tableView.model()
        for row_iter in range(model.rowCount()):
            car_no = model.index(row_iter, 0).data()
            leather_weight = model.index(row_iter, 1).data()
            add_time = model.index(row_iter, 2).data()
            data.append((car_no, leather_weight, add_time))
        delete_sql = 'delete from t_car'
        self.db.update(delete_sql)
        update_sql = 'replace into t_car(car_no, leather_weight, add_time) values (?,?,?)'
        ret = self.db.update(update_sql, data)
        if ret:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = CarManageForm()
    myshow.show()
    sys.exit(app.exec_())