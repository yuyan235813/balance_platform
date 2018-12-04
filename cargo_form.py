from PyQt5 import QtWidgets
from ui.cargo_manage import Ui_cargo_ManageForm
from ui.cargo_dialog import Ui_Cargo_Dialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
from utils import normal_utils
from utils.sqllite_util import EasySqlite
from functools import partial
import os
import subprocess
from utils.log_utils import Logger as logger


class cargoForm(QtWidgets.QWidget, Ui_cargo_ManageForm):
    """
    参数设置
    """
    def __init__(self):
        super(cargoForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.savePushButton.clicked.connect(self.save_data)
        self.cancelPushButton.clicked.connect(self.cancel_cargoForm)
        self.cargo_dialog = CargoDialog(self)

    def show(self):
        """
        显示ui
        :return:
        """
        super(cargoForm, self).show()
        self.set_table_view()

    def cancel_cargoForm(self):
        """
        显示ui
        :return:
        """
        self.close()

    def set_table_view(self):
        """
        :return:
        """
        header = ['序号',  '货物名称', '单价',  '备用1', '备用2', '备用3', '备用4']
        query_sql = 'select * from t_cargo'
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
        self.tableView.doubleClicked.connect(lambda x: self.display_data(data_list[int(x.row())]))
        # self.tableView.doubleClicked.connect(partial(self.supply_dialog_show, 't_supplier'))

    def display_data(self, data):
        if data:
            id=int(data.get('cargo_id', '0'))
            self.cargo_dialog.my_signal.connect(self.set_table_view)
            self.cargo_dialog.show(id)
        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序')

    def save_data(self):
        """

        :return:
        """
        cargo_name = self.CargoNameLineEdit.text()
        cargo_price = self.CargopriceLineEdit.text()
        if cargo_name:
            insert_sql = 'insert into t_cargo(name,price) values (?,?)'
            ret = self.db.update(insert_sql, [cargo_name, cargo_price])
            if ret:
                QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
                self.set_table_view()
                self.CargoNameLineEdit.clear()
                self.CargopriceLineEdit.clear()
            else:
                QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)

        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序',
                                            "货物名称不能为空",
                                           QtWidgets.QMessageBox.Yes)


class CargoDialog(QtWidgets.QDialog, Ui_Cargo_Dialog):
    """
    参数修改
    """
    my_signal = pyqtSignal(str)

    def __init__(self, parent):
        super(CargoDialog, self).__init__()
        self.setupUi(self)
        # 自定义信号
        self.table = ''
        self.column = ''
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.setWindowModality(Qt.ApplicationModal)
        self.deletePushButton.clicked.connect(self.delete_cargo)
        self.savePushButton.clicked.connect(self.save_cargo)
        self.cancelPushButton.clicked.connect(self.cancel_cargo)

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(CargoDialog, self).show()

        query_sql = 'select name,price,cargo_id from t_cargo  ' \
                    'where cargo_id = %s' % (column)
        data_list = self.db.query(query_sql)
        self.CargoNameLineEdit.setText(str(list(data_list[0].values())[0]))
        self.CargopriceLineEdit.setText(str(list(data_list[0].values())[1]))
        self.CargoIdLineEdit.setText(str(list(data_list[0].values())[2]))

    def save_cargo(self):
        """
        保存item
        :return:
        """
        cargo_name = self.CargoNameLineEdit.text()
        cargo_price = self.CargopriceLineEdit.text()
        cargo_id = self.CargoIdLineEdit.text()
        insert_sql = 'update  t_cargo set name=?,price=? ' \
                     'where  cargo_id = ?'
        ret = self.db.update(insert_sql, [cargo_name, cargo_price, int(cargo_id)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)

    def cancel_cargo(self):
        """
        取消更改
        :return:
        """
        self.close()

    def delete_cargo(self):
        """
        删除item
        :return:
        """
        cargo_id = self.CargoIdLineEdit.text()
        delete_sql = 'delete from t_cargo where  cargo_id = ?'
        ret = self.db.update(delete_sql, [int(cargo_id)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'删除成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'删除失败:\n', QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = cargoForm()
    myshow.show()
    sys.exit(app.exec_())
