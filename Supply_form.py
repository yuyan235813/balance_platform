from PyQt5 import QtWidgets
from ui.Supply_manage import Ui_supplyManageForm
from ui.supply_dialog import Ui_Supply_Dialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
from utils import normal_utils
from utils.sqllite_util import EasySqlite
from functools import partial
import os
import subprocess
from utils.log_utils import Logger as logger


class SupplyForm(QtWidgets.QWidget, Ui_supplyManageForm):
    """
    参数设置
    """
    def __init__(self):
        super(SupplyForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.savePushButton.clicked.connect(self.save_data)
        self.cancelPushButton.clicked.connect(self.cancel_SupplyForm)
        self.supply_dialog = SupplyDialog(self)

    def show(self):
        """
        显示ui
        :return:
        """
        super(SupplyForm, self).show()
        self.set_table_view()

    def cancel_SupplyForm(self):
        """
        显示ui
        :return:
        """
        self.close()

    def set_table_view(self):
        """
        :return:
        """
        header = ['序号',  '供货单位', '联系人', '联系电话', '地址',
                  '开户行', '账号', '税号',  '备用1', '备用2', '备用3', '备用4']
        query_sql = 'select * from t_supplier'
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

    def supply_dialog_show(self, table):
        """
        参数配置对话框
        :return:
        """
        # self.balanceNoBlael.setText(str(data.get('balance_id', '0')))
        query_sql = 'select %s from %s where supplier_id = %s' % ("", table, )
        self.supply_dialog.my_signal.connect(self.set_data)
        self.params_dialog.show(table)

    def display_data(self, data):
        if data:
            id=int(data.get('supplier_id', '0'))
            self.supply_dialog.my_signal.connect(self.set_table_view)
            self.supply_dialog.show(id)
        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序')

    def save_data(self):
        """

        :return:
        """
        supply_name = self.SupplyNameLineEdit.text()
        supply_contact = self.SupplyContactLineEdit.text()
        supply_phone = self.SupplyPhoneLineEdit.text()
        supply_address = self.SupplyAddressLineEdit.text()
        supply_bank = self.SupplyBankLineEdit.text()
        supply_count = self.SupplyCountLineEdit.text()
        supply_duty = self.SupplyDutyLineEdit.text()
        if supply_name:
            insert_sql = 'insert into t_supplier(name,contact,tel,address,bank,account,duty) values (?,?,?,?,?,?,?)'
            ret = self.db.update(insert_sql, [supply_name, supply_contact, supply_phone, supply_address, supply_bank,
                                          supply_count, supply_duty])
            if ret:
               QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
            else:
               QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
               self.set_table_view()
               self.SupplyNameLineEdit.clear()
               self.SupplyContactLineEdit.clear()
               self.SupplyPhoneLineEdit.clear()
               self.SupplyAddressLineEdit.clear()
               self.SupplyBankLineEdit.clear()
               self.SupplyCountLineEdit.clear()
               self.SupplyDutyLineEdit.clear()
        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序',
                                            "单位名称不能为空",
                                           QtWidgets.QMessageBox.Yes)


class SupplyDialog(QtWidgets.QDialog, Ui_Supply_Dialog):
    """
    参数修改
    """
    my_signal = pyqtSignal(str)

    def __init__(self, parent):
        super(SupplyDialog, self).__init__()
        self.setupUi(self)
        # 自定义信号
        self.table = ''
        self.column = ''
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.setWindowModality(Qt.ApplicationModal)
        self.deletePushButton.clicked.connect(self.delete_supply)
        self.savePushButton.clicked.connect(self.save_supply)
        self.cancelPushButton.clicked.connect(self.cancel_supply)

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(SupplyDialog, self).show()

        query_sql = 'select name,contact,tel,address,bank,account,duty,supplier_id from t_supplier  ' \
                    'where supplier_id = %s' % (column)
        data_list = self.db.query(query_sql)
        self.SupplyNameLineEdit.setText(str(list(data_list[0].values())[0]))
        self.SupplyContactLineEdit.setText(str(list(data_list[0].values())[1]))
        self.SupplyPhoneLineEdit.setText(str(list(data_list[0].values())[2]))
        self.SupplyAddressLineEdit.setText(str(list(data_list[0].values())[3]))
        self.SupplyBankLineEdit.setText(str(list(data_list[0].values())[4]))
        self.SupplyCountLineEdit.setText(str(list(data_list[0].values())[5]))
        self.SupplyDutyLineEdit.setText(str(list(data_list[0].values())[6]))
        self.SupplyIdLineEdit.setText(str(list(data_list[0].values())[7]))

    def save_supply(self):
        """
        保存item
        :return:
        """
        supply_name = self.SupplyNameLineEdit.text()
        supply_contact = self.SupplyContactLineEdit.text()
        supply_phone = self.SupplyPhoneLineEdit.text()
        supply_address = self.SupplyAddressLineEdit.text()
        supply_bank = self.SupplyBankLineEdit.text()
        supply_count = self.SupplyCountLineEdit.text()
        supply_duty = self.SupplyDutyLineEdit.text()
        supply_id = self.SupplyIdLineEdit.text()
        insert_sql = 'update  t_supplier set name=?,contact=?,tel=?,address=?,bank=?,account=?,duty=? ' \
                     'where  supplier_id = ?'
        ret = self.db.update(insert_sql, [supply_name, supply_contact, supply_phone, supply_address, supply_bank,
                                          supply_count, supply_duty,int(supply_id)])
        if ret:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)

    def cancel_supply(self):
        """
        取消更改
        :return:
        """
        self.close()

    def delete_supply(self):
        """
        删除item
        :return:
        """
        supply_id = self.SupplyIdLineEdit.text()
        delete_sql = 'delete from t_supplier where  supplier_id = ?'
        ret = self.db.update(delete_sql, [int(supply_id)])
        if ret:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'删除失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, u'本程序', u'删除成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = SupplyForm()
    myshow.show()
    sys.exit(app.exec_())
