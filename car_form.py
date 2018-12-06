#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.car_manage import Ui_carManageForm
from ui.car_manage_change import Ui_dialog
from car_no_dialog_form import CarNoDialogForm
from utils.sqllite_util import EasySqlite
from utils.normal_utils import get_cur_time
from utils.log_utils import Logger as logger


class CarManageForm(QtWidgets.QWidget, Ui_carManageForm):
    """
    车辆管理
    """
    def __init__(self):
        super(CarManageForm, self).__init__()
        self.setupUi(self)
        self.db = EasySqlite(r'rmf/db/balance.db')
        #self.pushButton.clicked.connect(self.__show_dialog)
        self.cancelPushButton.clicked.connect(self.close)
        # self.addPushButton.clicked.connect(self.__add_data)
        self.deletePushButton.clicked.connect(self.__delete_data)
        self.savePushButton.clicked.connect(self.__save_data)
        self.dialog = CarNoDialogForm()
        # self.dialog.my_signal.connect(self.carNoLineEdit.setText)
        self.car_dialog = CarManageChangeForm(self)

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
        self.car_dialog.show(car_no, leather_weight, index.row())

    def update_data(self, data):
        """
        修改数据
        :param data:
        :return:
        """
        if len(data) == 3:
            print(data)
            car_no = data[0]
            leather_weight = data[1]
            index = data[2]
            model = self.tableView.model()
            model.setData(model.index(index, 0), car_no)
            model.setData(model.index(index, 1), leather_weight)

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
        self.carNoLineEdit.clear()
        self.doubleSpinBox.clear()


    def __delete_data(self):
        """
        删除数据
        :return:
        """
        current_row = self.tableView.currentIndex().row()
        status = self.tableView.model().removeRow(current_row)
        if not status:
            QtWidgets.QMessageBox.warning(self, '本程序', "删除失败！", QtWidgets.QMessageBox.Ok)
            return

    def __save_data(self):
        """
        保存数据
        :return:
        """
        ret = 1
        data = []
        cur_car_no = []
        model = self.tableView.model()
        for row_iter in range(model.rowCount()):
            car_no = model.index(row_iter, 0).data()
            leather_weight = model.index(row_iter, 1).data()
            add_time = model.index(row_iter, 2).data()
            data.append((car_no, leather_weight, add_time))
            cur_car_no.append(car_no)
        query_sql = 'select car_no from t_car'
        query_ret = self.db.query(query_sql, result_dict=False)
        db_car_no = list(list(zip(*query_ret))[0])
        del_car_no = [car_no for car_no in db_car_no if car_no not in cur_car_no]
        if del_car_no:
            logger.info(del_car_no)
            del_sql = 'delete from t_car where car_no=?'
            ret1 = self.db.update(del_sql, args=del_car_no)
            ret = ret and ret1
        if cur_car_no:
            logger.info(cur_car_no)
            update_sql = 'replace into t_car(car_no, leather_weight, add_time) values (?,?,?)'
            ret2 = self.db.update(update_sql, data)
            ret = ret and ret2
        if ret:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)

    def show(self):
        """
        显示
        :return:
        """
        super().show()
        self.__init_data()


class CarManageChangeForm(QtWidgets.QDialog, Ui_dialog):
    """
    修改车辆信息
    """
    def __init__(self, parent):
        super(CarManageChangeForm, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.index = 0
        self.dialog = CarNoDialogForm()
        self.dialog.my_signal.connect(self.carNoLineEdit.setText)
        self.setWindowModality(Qt.ApplicationModal)
        self.pushButton.clicked.connect(self.__show_dialog)
        self.dialog = CarNoDialogForm()
        self.dialog.my_signal.connect(self.carNoLineEdit.setText)
        self.cancelPushButton.clicked.connect(self.close)
        self.okPushButton.clicked.connect(self.__update_data)

    def show(self, car_no, leather_weight, index):
        """
        显示对话框
        :param car_no:
        :param leather_weight:
        :return:
        """
        super().show()
        self.carNoLineEdit.setText(car_no)
        self.doubleSpinBox.setValue(float(leather_weight))
        self.index = index

    def __update_data(self):
        """
        更新数据
        :return:
        """
        car_no = self.carNoLineEdit.text()
        leather_weight = self.doubleSpinBox.value()
        self.parent.update_data((car_no, leather_weight, self.index))
        self.close()

    def __show_dialog(self):
        """
        显示车牌号键盘
        :return:
        """
        if self.dialog.isVisible():
            self.dialog.setVisible(False)
            return
        self.dialog.setWindowModality(Qt.ApplicationModal)
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
        point.setY(point.y() + 40)
        self.dialog.move(point)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = CarManageForm()
    myshow.show()
    sys.exit(app.exec_())