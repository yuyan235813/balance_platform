from PyQt5 import QtWidgets
from ui.poll_main import Ui_PollmainForm
from ui.poll_result import Ui_PollResultForm
from ui.balance_detail import Ui_balance_detailDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import *
from utils import normal_utils
from utils.sqllite_util import EasySqlite
from functools import partial
import os
import subprocess
from utils.log_utils import Logger as logger
import datetime


class pollmainForm(QtWidgets.QWidget, Ui_PollmainForm):
    """
    参数设置
    """
    def __init__(self):
        super(pollmainForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.QueryPushButton.clicked.connect(self.poll_data)
        self.cancelPushButton.clicked.connect(self.cancel_pollForm)
        self.pollresult = PollResultForm(self)

    def cancel_pollForm(self):
        """
        显示ui
        :return:
        """
        self.close()

    def poll_data(self):
        """
        :return:
        """
        begin_date = self.begindateEdit.text()+' 00:00:00'
        begin_date_zero=datetime.datetime.strptime(begin_date, "%Y-%m-%d %H:%M:%S")
        print(datetime.datetime.strptime(begin_date, "%Y-%m-%d %H:%M:%S"))
        end_date=self.enddateEdit.text()+' 23:59:59'
        end_date_24 = datetime.datetime.strptime(begin_date, "%Y-%m-%d %H:%M:%S")
        carNo= self.CarNoLineEdit.text()
        receiver_name = self.ReceiverNameLineEdit.text()
        cargo_name = self.CargoNameLineEdit.text()
        supply_name = self.SupplyNameLineEdit.text()
        balance_Id = self.balanceNoLineEdit.text()
        condition = ' where'
        if carNo:
            condition = condition + ' car_id = "'+carNo+'"  and'
        if balance_Id:
            condition = condition + ' balance_id = "'+balance_Id+'" and'
        if cargo_name:
            condition = condition + ' goods_name = "' + cargo_name + '" and'
        if receiver_name:
            condition = condition + ' receiver = "'+receiver_name+'" and'
        if supply_name:
            condition = condition + ' supplier = "'+supply_name+'" and'
        condition = condition[:-3]
        query_sql = 'select * from t_balance'+condition
        print(query_sql)
        data_list = self.db.query(query_sql)
        self.pollresult.show(data_list)


class PollResultForm(QtWidgets.QWidget, Ui_PollResultForm):
    """
    参数修改
    """
    my_signal = pyqtSignal(str)

    def __init__(self, parent):
        super(PollResultForm, self).__init__()
        self.setupUi(self)
        # 自定义信号
        self.table = ''
        self.column = ''
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.setWindowModality(Qt.ApplicationModal)
        self.balance_detail = Balance_detailDialog(self)

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(PollResultForm, self).show()
        header = ['单号', '车牌号', '毛重', '皮重', '净重', '货物名', '供货单位', '收货单位', '包装物重', '另扣',
                  '杂志', '水分', '单价', '金额', '含油', '结算重量', '规格', '驾驶员', '计划单号', '称重时间1', '称重日期',
                  '称重时间2', '操作员', '备注', '备用1', '备用2', '备用3', '备用4']
        row_no, col_no = len(column), len(header)
        model = QStandardItemModel(row_no, col_no)
        model.setHorizontalHeaderLabels(header)
        for row in range(row_no):
            values = list(column[row].values())
            for col in range(col_no):
                item = QStandardItem(str(values[col]))
                model.setItem(row, col, item)
        self.tableView.setModel(model)
        self.tableView.doubleClicked.connect(lambda x: self.display_data(column[int(x.row())]))

    def display_data(self, data):
        if data:
            id=int(data.get('balance_id', '0'))
            # self.balance_detail.my_signal.connect(self.set_table_view)
            self.balance_detail.show(id)
        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序')


class Balance_detailDialog(QtWidgets.QDialog, Ui_balance_detailDialog):
    """
    参数修改
    """
    my_signal = pyqtSignal(str)

    def __init__(self, parent):
        super(Balance_detailDialog, self).__init__()
        self.setupUi(self)
        # 自定义信号
        self.table = ''
        self.column = ''
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.setWindowModality(Qt.ApplicationModal)
        self.deletePushButton.clicked.connect(self.delete_detail)
        self.savePushButton.clicked.connect(self.save_detail)
        self.cancelPushButton.clicked.connect(self.cancel_detail)

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(Balance_detailDialog, self).show()

        query_sql = 'select balance_id,car_id,total_weight,leather_weight,actual_weight,balance_time1,' \
                    'balance_time2,goods_name,receiver,supplier,operator from t_balance  ' \
                    'where balance_id = %s' % (column)
        data_list = self.db.query(query_sql)
        self.balanceNoLineEdit.setText(str(list(data_list[0].values())[0]))
        self.carNoLineEdit.setText(str(list(data_list[0].values())[1]))
        self.totalWeightLineEdit.setText(str(list(data_list[0].values())[2]))
        self.leatherWeightLineEdit.setText(str(list(data_list[0].values())[3]))
        self.actualWeightLineEdit.setText(str(list(data_list[0].values())[4]))
        self.leatherWeighttimeLineEdit.setText(str(list(data_list[0].values())[5]))
        self.totalWeighttimeLineEdit.setText(str(list(data_list[0].values())[6]))
        self.cargoNameLineEdit.setText(str(list(data_list[0].values())[7]))
        self.receiverNameLineEdit_3.setText(str(list(data_list[0].values())[8]))
        self.supplyNameLineEdit_2.setText(str(list(data_list[0].values())[9]))
        self.operatorLineEdit_4.setText(str(list(data_list[0].values())[10]))

    def save_detail(self):
        """
        保存item
        :return:
        """
        carNo = self.carNoLineEdit.text()
        totalWeight = self.totalWeightLineEdit.text()
        leatherWeight = self.leatherWeightLineEdit.text()
        goodnNmes = self.cargoNameLineEdit.text()
        receiverName = self.receiverNameLineEdit_3.text()
        supplyName = self.supplyNameLineEdit_2.text()
        operator = self.operatorLineEdit_4.text()
        balance_No = self.balanceNoLineEdit.text()
        insert_sql = 'update  t_balance set car_id=?,total_weight=?,leather_weight=?,goods_name=?,receiver=?,' \
                     'supplier=?,operator=? '  'where  balance_id = ?'
        ret = self.db.update(insert_sql, [carNo, totalWeight, leatherWeight, goodnNmes, receiverName,
                                          supplyName, operator, int(balance_No)])
        if ret:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)

    def cancel_detail(self):
        """
        取消更改
        :return:
        """
        self.close()

    def delete_detail(self):
        """
        删除item
        :return:
        """
        balance_id = self.balanceNoLineEdit.text()
        delete_sql = 'delete from t_balance where  balance_id = ?'
        ret = self.db.update(delete_sql, [int(balance_id)])
        if ret:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'删除失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, u'本程序', u'删除成功!', QtWidgets.QMessageBox.Ok)
            self.close()
            self.my_signal.emit(self.table)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = pollmainForm()
    myshow.show()
    sys.exit(app.exec_())
