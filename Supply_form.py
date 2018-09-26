from PyQt5 import QtWidgets
from ui.Supply_manage import Ui_supplyManageForm
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.params_dialog import Ui_dialog
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

    def show(self):
        """
        显示ui
        :return:
        """
        super(SupplyForm, self).show()
        self.set_table_view()


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