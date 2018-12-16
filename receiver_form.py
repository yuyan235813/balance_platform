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
    def __init__(self, parent):
        super(receiverForm, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.savePushButton.clicked.connect(self.clear_data)
        self.cancelPushButton.clicked.connect(self.cancel_ReceiveForm)
        self.receiver_dialog = ReceiverDialog(self)
        self.savePushButton_3.clicked.connect(self.delete_data)
        self.savePushButton_2.clicked.connect(self.save_data)
        self.savePushButton_4.clicked.connect(self.update_data)
        self.autoMe = 0

    def show(self):
        """
        显示ui
        :return:
        """
        super(receiverForm, self).show()
        self.set_table_view()

    def update_data(self):
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
        receiver_id = self.ReceiverIDLineEdit.text()
        if len(receiver_id.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要修改的记录！", QtWidgets.QMessageBox.Ok)
            return
        if len(receiver_name.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "名称不能为空！", QtWidgets.QMessageBox.Ok)
            return
        insert_sql = 'update  t_receiver set receiver_name=?,receiver_contact=?,receiver_tel=?,receiver_address=?,receiver_bank=?,receiver_account=?,receiver_duty=? ' \
                     'where  receiver_id = ?'
        ret = self.db.update(insert_sql, [receiver_name, receiver_contact, receiver_phone, receiver_address, receiver_bank,
                                          receiver_count, receiver_duty,int(receiver_id)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.set_table_view()
            self.clear_data()
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)

    def delete_data(self):
        """
        删除item
        :return:
        """
        receiver_id = self.ReceiverIDLineEdit.text()
        if len(receiver_id.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的记录！", QtWidgets.QMessageBox.Ok)
            return
        delete_sql = 'delete from t_receiver where  receiver_id = ?'
        ret = self.db.update(delete_sql, [int(receiver_id)])
        # self.autoMe = self.autoMe + 1
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'删除成功!', QtWidgets.QMessageBox.Ok)
            self.set_table_view()
            self.clear_data()
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'删除失败:\n', QtWidgets.QMessageBox.Ok)

    def cancel_ReceiveForm(self):
        """
        显示ui
        :return:
        """
        self.close()

    def clear_data(self):
        """
        显示ui
        :return:
        """
        self.ReceiverNameLineEdit.clear()
        self.ReceiverContactLineEdit.clear()
        self.ReceiverPhoneLineEdit.clear()
        self.ReceiverAddressLineEdit.clear()
        self.ReceiverBankLineEdit.clear()
        self.ReceiverCountLineEdit.clear()
        self.ReceiverDutyLineEdit.clear()
        self.ReceiverIDLineEdit.clear()

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
        self.tableView.doubleClicked.connect(self.__display_data)
        # self.tableView.doubleClicked.connect(lambda x: self.display_data(data_list[x.row()-self.autoMe]) if x.row()-self.autoMe>0 else self.display_data0(data_list[x.row()]))

    def __display_data(self, index):
        """
               返显数据
               :param index:
               :return:
               """
        self.ReceiverNameLineEdit.setText(str(self.tableView.model().index(index.row(), 1).data()))
        self.ReceiverContactLineEdit.setText( self.tableView.model().index(index.row(), 2).data())
        self.ReceiverPhoneLineEdit.setText( self.tableView.model().index(index.row(), 3).data())
        self.ReceiverAddressLineEdit.setText( self.tableView.model().index(index.row(), 4).data())
        self.ReceiverBankLineEdit.setText( self.tableView.model().index(index.row(), 5).data())
        self.ReceiverCountLineEdit.setText( self.tableView.model().index(index.row(), 6).data())
        self.ReceiverDutyLineEdit.setText( self.tableView.model().index(index.row(), 7).data())
        self.ReceiverIDLineEdit.setText(str( self.tableView.model().index(index.row(), 0).data()))

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
            query_sql = 'select * from t_receiver'
            data_list = self.db.query(query_sql)
            for i in range(len(data_list)):
                if data.get('receiver_id', '0') == data_list[i].get('receiver_id', '0'):
                    data_find = data_list[i+self.autoMe]
                    break
            self.receiver_dialog.my_signal.connect(self.set_table_view)
            self.receiver_dialog.show(int(data_find.get('receiver_id', '0')))
        else:
            QtWidgets.QMessageBox.question(self,'本程序')

    def display_data0(self, data):

        if data:
            self.receiver_dialog.my_signal.connect(self.set_table_view)
            self.receiver_dialog.show(int(data.get('receiver_id', '0')))
        else:
            QtWidgets.QMessageBox.question(self,'本程序')

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
        if len(receiver_name.strip()) == 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "名称不能为空！", QtWidgets.QMessageBox.Ok)
            return
        repeat = False
        row_count = self.tableView.model().rowCount()
        for i in range(row_count):
            if receiver_name == self.tableView.model().index(i, 1).data():
                repeat = True
                break
        if repeat:
            QtWidgets.QMessageBox.warning(self, '本程序', "单位已经存在！", QtWidgets.QMessageBox.Ok)
            return
        if receiver_name:
            insert_sql = 'insert into t_receiver(receiver_name,receiver_contact,receiver_tel,receiver_address,receiver_bank,receiver_account,receiver_duty) values (?,?,?,?,?,?,?)'
            ret = self.db.update(insert_sql, [receiver_name, receiver_contact, receiver_phone, receiver_address,
                                              receiver_bank, receiver_count, receiver_duty])
            # self.autoMe = self.autoMe + 1

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
                self.ReceiverIDLineEdit.clear()
            else:
                QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序',
                                            "单位名称不能为空",
                                           QtWidgets.QMessageBox.Yes)

    def closeEvent(self, event):
        """
        关闭事件
        :param event:
        :return:
        """
        self.parent.update_combobox()
        self.close()


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
