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
        self.cancelPushButton_2.clicked.connect(self.clear_SupplyForm)
        self.savePushButton_2.clicked.connect(self.update_SupplyForm)
        self.savePushButton_3.clicked.connect(self.delete_SupplyForm)
        self.supply_dialog = SupplyDialog(self)
        self.autoMe = 0

    def show(self):
        """
        显示ui
        :return:
        """
        super(SupplyForm, self).show()
        self.set_table_view()

    def update_SupplyForm(self):
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
        supply_id = self.SupplyIDLineEdit.text()
        if len(supply_id.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要修改的记录！", QtWidgets.QMessageBox.Ok)
            return
        if len(supply_name.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "名称不能为空！", QtWidgets.QMessageBox.Ok)
            return
        insert_sql = 'update  t_supplier set supplier_name=?,supplier_contact=?,supplier_tel=?,supplier_address=?,supplier_bank=?,supplier_account=?,supplier_duty=? ' \
                     'where  supplier_id = ?'
        ret = self.db.update(insert_sql, [supply_name, supply_contact, supply_phone, supply_address, supply_bank,
                                          supply_count, supply_duty,int(supply_id)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.show()
            self.clear_SupplyForm()
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)

    def delete_SupplyForm(self):
        """
        删除item
        :return:
        """
        supply_id = self.SupplyIDLineEdit.text()
        if len(supply_id.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的记录！", QtWidgets.QMessageBox.Ok)
            return
        delete_sql = 'delete from t_supplier where  supplier_id = ?'
        ret = self.db.update(delete_sql, [int(supply_id)])
        # self.autoMe = self.autoMe + 1
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'删除成功!', QtWidgets.QMessageBox.Ok)
            self.show()
            self.clear_SupplyForm()
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'删除失败:\n', QtWidgets.QMessageBox.Ok)

    def cancel_SupplyForm(self):
        """
        显示ui
        :return:
        """
        self.close()

    def clear_SupplyForm(self):
        """
        显示ui
        :return:
        """
        self.SupplyNameLineEdit.clear()
        self.SupplyContactLineEdit.clear()
        self.SupplyPhoneLineEdit.clear()
        self.SupplyAddressLineEdit.clear()
        self.SupplyBankLineEdit.clear()
        self.SupplyCountLineEdit.clear()
        self.SupplyDutyLineEdit.clear()
        self.SupplyIDLineEdit.clear()

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
        # self.tableView.clicked.connect(lambda x: self.display_data0(data_list[int(x.row())]))
        self.tableView.doubleClicked.connect(self.__display_data)
        # self.tableView.clicked.connect(lambda x: self.display_data0(data_list[int(self.tableView.currentIndex().row())]))
        # self.tableView.doubleClicked.connect(lambda x: self.display_data(
        #    data_list[x.row() - self.autoMe]) if x.row() - self.autoMe > 0 else self.display_data0(data_list[x.row()]))

    def __display_data(self, index):
        """
               返显数据
               :param index:
               :return:
               """
        self.SupplyNameLineEdit.setText(str(self.tableView.model().index(index.row(), 1).data()))
        self.SupplyContactLineEdit.setText( self.tableView.model().index(index.row(), 2).data())
        self.SupplyPhoneLineEdit.setText( self.tableView.model().index(index.row(), 3).data())
        self.SupplyAddressLineEdit.setText( self.tableView.model().index(index.row(), 4).data())
        self.SupplyBankLineEdit.setText(self.tableView.model().index(index.row(), 5).data())
        self.SupplyCountLineEdit.setText( self.tableView.model().index(index.row(), 6).data())
        self.SupplyDutyLineEdit.setText( self.tableView.model().index(index.row(), 7).data())
        self.SupplyIDLineEdit.setText(str( self.tableView.model().index(index.row(), 0).data()))

    def supply_dialog_show(self, table):
        """
        参数配置对话框
        :return:
        """
        # self.balanceNoBlael.setText(str(data.get('balance_id', '0')))
        query_sql = 'select %s from %s where receiver_id = %s' % ("", table,)
        self.supply_dialog.my_signal.connect(self.set_data)
        self.params_dialog.show(table)

    def display_data(self, data):
        if data:
            query_sql = 'select * from t_supplier'
            data_list = self.db.query(query_sql)
            print(str(data.get('supplier_id', '0')))
            for i in range(len(data_list)):
                if data.get('supplier_id', '0') == data_list[i].get('supplier_id', '0'):
                    data_find = data_list[i + self.autoMe]

            self.SupplyIDLineEdit.setText(str(data_find.get('supplier_id', '0')))
            self.SupplyNameLineEdit.setText(str(data_find.get('supplier_name', '0')))
            self.SupplyContactLineEdit.setText(data_find.get('supplier_contact', 0))
            self.SupplyPhoneLineEdit.setText(data_find.get('supplier_tel', 0))
            self.SupplyAddressLineEdit.setText(data_find.get('supplier_address', 0))
            self.SupplyCountLineEdit.setText(data_find.get('supplier_account', 0.))
            self.SupplyBankLineEdit.setText(data_find.get('supplier_bank', 0.))

    def display_data0(self, data):
        if data:
            self.SupplyNameLineEdit.setText(str(data.get('supplier_name', '0')))
            self.SupplyContactLineEdit.setText(data.get('supplier_contact', 0))
            self.SupplyPhoneLineEdit.setText(data.get('supplier_tel', 0))
            self.SupplyAddressLineEdit.setText(data.get('supplier_address', 0))
            self.SupplyCountLineEdit.setText(data.get('supplier_account', 0.))
            self.SupplyBankLineEdit.setText(data.get('supplier_bank', 0.))
            self.SupplyDutyLineEdit.setText(data.get('supplier_duty', ''))
            self.SupplyIDLineEdit.setText(str(data.get('supplier_id', '0')))

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
        if len(supply_name.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "名称不能为空！", QtWidgets.QMessageBox.Ok)
            return
        repeat = False
        row_count = self.tableView.model().rowCount()
        for i in range(row_count):
            if supply_name == self.tableView.model().index(i, 1).data():
                repeat = True
                break
        if repeat:
            QtWidgets.QMessageBox.warning(self, '本程序', "单位已经存在！", QtWidgets.QMessageBox.Ok)
            return

        if supply_name:
            insert_sql = 'insert into t_supplier(supplier_name,supplier_contact,supplier_tel,supplier_address,supplier_bank,supplier_account,supplier_duty) values (?,?,?,?,?,?,?)'
            ret = self.db.update(insert_sql, [supply_name, supply_contact, supply_phone, supply_address, supply_bank,
                                          supply_count, supply_duty])
            #self.autoMe = self.autoMe + 1
            # self.tableView.model().insertRow(row_count, items)
            if ret:
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
                QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
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

        query_sql = 'select supplier_name,supplier_contact,supplier_tel,supplier_address,supplier_bank,supplier_account,supplier_duty,supplier_id from t_supplier  ' \
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
        insert_sql = 'update  t_supplier set supplier_name=?,supplier_contact=?,supplier_tel=?,supplier_address=?,supplier_bank=?,supplier_account=?,supplier_duty=? ' \
                     'where  supplier_id = ?'
        ret = self.db.update(insert_sql, [supply_name, supply_contact, supply_phone, supply_address, supply_bank,
                                          supply_count, supply_duty,int(supply_id)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)


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
            QtWidgets.QMessageBox.information(self, u'本程序', u'删除成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'删除失败:\n', QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = SupplyForm()
    myshow.show()
    sys.exit(app.exec_())
