from PyQt5 import QtWidgets
from ui.receiver_manage import Ui_receiverManageForm
from ui.receiver_dialog import Ui_Receiver_Dialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
from utils import normal_utils
from utils.sqllite_util import EasySqlite
from functools import partial
import os
import subprocess
from utils.log_utils import Logger as logger


class receiverForm(QtWidgets.QWidget, Ui_receiverManageForm):
    """
    参数设置
    """
    def __init__(self):
        super(receiverForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.savePushButton.clicked.connect(self.save_data)
        self.cancelPushButton.clicked.connect(self.cancel_ReceiveForm)
        self.receiver_dialog = ReceiverDialog(self)

    def show(self):
        """
        显示ui
        :return:
        """
        super(receiverForm, self).show()
        self.set_table_view()

    def cancel_ReceiveForm(self):
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
        query_sql = 'select * from t_receiver'
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
        query_sql = 'select %s from %s where receiver_id = %s' % ("", table, )
        self.supply_dialog.my_signal.connect(self.set_data)
        self.params_dialog.show(table)

    def display_data(self, data):
        if data:
            id=int(data.get('receiver_id', '0'))
            self.receiver_dialog.my_signal.connect(self.set_table_view)
            self.receiver_dialog.show(id)
        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序')

    def save_data(self):
        """

        :return:
        """
        receiver_name = self.ReceiverNameLineEdit.text()
        receiver_contact = self.ReceiverContactLineEdit.text()
        receiver_phone = self.ReceiverPhoneLineEdit.text()
        receiver_address = self.ReceiverAddressLineEdit.text()
        receiver_bank = self.ReceiverBankLineEdit.text()
        receiver_count = self.ReceiverCountLineEdit.text()
        receiver_duty = self.ReceiverDutyLineEdit.text()
        if receiver_name:
            insert_sql = 'insert into t_receiver(receiver_name,receiver_contact,receiver_tel,receiver_address,receiver_bank,receiver_account,receiver_duty) values (?,?,?,?,?,?,?)'
            ret = self.db.update(insert_sql, [receiver_name, receiver_contact, receiver_phone, receiver_address,
                                              receiver_bank, receiver_count, receiver_duty])
            if ret:
                QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
                self.set_table_view()
                self.ReceiverNameLineEdit.clear()
                self.ReceiverContactLineEdit.clear()
                self.ReceiverPhoneLineEdit.clear()
                self.ReceiverAddressLineEdit.clear()
                self.ReceiverCountLineEdit.clear()
                self.ReceiverBankLineEdit.clear()
                self.ReceiverDutyLineEdit.clear()
            else:
                QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序',
                                            "单位名称不能为空",
                                           QtWidgets.QMessageBox.Yes)


class ReceiverDialog(QtWidgets.QDialog, Ui_Receiver_Dialog):
    """
    参数修改
    """
    my_signal = pyqtSignal(str)

    def __init__(self, parent):
        super(ReceiverDialog, self).__init__()
        self.setupUi(self)
        # 自定义信号
        self.table = ''
        self.column = ''
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.setWindowModality(Qt.ApplicationModal)
        self.deletePushButton.clicked.connect(self.delete_receiver)
        self.savePushButton.clicked.connect(self.save_receiver)
        self.cancelPushButton.clicked.connect(self.cancel_receiver)

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(ReceiverDialog, self).show()

        query_sql = 'select receiver_name,receiver_contact,receiver_tel,receiver_address,receiver_bank,receiver_account,receiver_duty,receiver_id from t_receiver  ' \
                    'where receiver_id = %s' % (column)
        data_list = self.db.query(query_sql)
        self.ReceiverNameLineEdit.setText(str(list(data_list[0].values())[0]))
        self.ReceiverContactLineEdit.setText(str(list(data_list[0].values())[1]))
        self.ReceiverPhoneLineEdit.setText(str(list(data_list[0].values())[2]))
        self.ReceiverAddressLineEdit.setText(str(list(data_list[0].values())[3]))
        self.ReceiverBankLineEdit.setText(str(list(data_list[0].values())[4]))
        self.ReceiverCountLineEdit.setText(str(list(data_list[0].values())[5]))
        self.ReceiverDutyLineEdit.setText(str(list(data_list[0].values())[6]))
        self.ReceiverIdLineEdit.setText(str(list(data_list[0].values())[7]))

    def save_receiver(self):
        """
        保存item
        :return:
        """
        receiver_name = self.ReceiverNameLineEdit.text()
        receiver_contact = self.ReceiverContactLineEdit.text()
        receiver_phone = self.ReceiverPhoneLineEdit.text()
        receiver_address = self.ReceiverAddressLineEdit.text()
        receiver_bank = self.ReceiverBankLineEdit.text()
        receiver_count = self.ReceiverCountLineEdit.text()
        receiver_duty = self.ReceiverDutyLineEdit.text()
        receiver_id = self.ReceiverIdLineEdit.text()
        insert_sql = 'update  t_receiver set receiver_name=?,receiver_contact=?,receiver_tel=?,receiver_address=?,receiver_bank=?,receiver_account=?,receiver_duty=? ' \
                     'where  receiver_id = ?'
        ret = self.db.update(insert_sql, [receiver_name, receiver_contact, receiver_phone, receiver_address,
                                              receiver_bank, receiver_count, receiver_duty, int(receiver_id)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)

    def cancel_receiver(self):
        """
        取消更改
        :return:
        """
        self.close()

    def delete_receiver(self):
        """
        删除item
        :return:
        """
        receiver_id = self.ReceiverIdLineEdit.text()
        delete_sql = 'delete from t_receiver where  receiver_id = ?'
        ret = self.db.update(delete_sql, [int(receiver_id)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'删除成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'删除失败:\n', QtWidgets.QMessageBox.Ok)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = receiverForm()
    myshow.show()
    sys.exit(app.exec_())
