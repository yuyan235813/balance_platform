from PyQt5 import QtWidgets
from ui.poll_main import Ui_PollmainForm
from ui.poll_result import Ui_PollResultForm
from ui.balance_detail import Ui_balance_detailDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtCore import *
from utils.sqllite_util import EasySqlite
import xlwt
import subprocess
import datetime
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtGui import QTextDocument
from xlwt import *
import logging
import os


class pollmainForm(QtWidgets.QWidget, Ui_PollmainForm):
    """
    参数设置
    """
    def __init__(self):
        super(pollmainForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.begindateEdit.setDate(QDate.currentDate())
        self.enddateEdit.setDate(QDate.currentDate())
        self.QueryPushButton.clicked.connect(self.poll_data)
        self.cancelPushButton.clicked.connect(self.cancel_pollForm)
        self.pollresult = PollResultForm(self)
        self.update_combobox()

    def cancel_pollForm(self):
        """
        显示ui
        :return:
        """
        self.close()

    def update_combobox(self):
        """
        下拉列表数据
        :return:
        """
        cargo_query_sql = 'select name from t_cargo'
        cargo_list = self.db.query(cargo_query_sql)
        cargo_row_no = len(cargo_list)
        for row in range(cargo_row_no):
            values = list(cargo_list[row].values())[0]
            self.CargoNamecomboBox.addItem(values)
        self.CargoNamecomboBox.clearEditText()
        supply_query_sql = 'select supplier_name from t_supplier'
        supply_list = self.db.query(supply_query_sql)
        supply_row_no = len(supply_list)
        for row in range(supply_row_no):
            values = list(supply_list[row].values())[0]
            self.SupplyNamecomboBox.addItem(values)
        self.SupplyNamecomboBox.clearEditText()
        receiver_query_sql = 'select receiver_name from t_receiver'
        receiver_list = self.db.query(receiver_query_sql)
        receiver_row_no = len(receiver_list)
        for row in range(receiver_row_no):
            values = list(receiver_list[row].values())[0]
            self.ReceiverNamecomboBox.addItem(values)
        self.ReceiverNamecomboBox.clearEditText()

    def poll_data(self):
        """
        :return:
        """
        begin_date = self.begindateEdit.text()+' 00:00:00'
        begin_date = begin_date.replace("/" , "-")
        begin_date_zero=datetime.datetime.strptime(begin_date, "%Y-%m-%d %H:%M:%S")
        begin_date_zero =str(begin_date_zero)
        end_date = self.enddateEdit.text()+' 23:59:59'
        end_date = end_date.replace("/","-")
        end_date_24 = datetime.datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
        end_date_24 = str(end_date_24)
        carNo = self.CarNoLineEdit.text()
        receiver_name = self.ReceiverNamecomboBox.currentText()
        cargo_name = self.CargoNamecomboBox.currentText()
        supply_name = self.SupplyNamecomboBox.currentText()
        balance_Id = self.balanceNoLineEdit.text()
        condition = ' where'
        condition = condition + ' balance_time1 >= "' + begin_date_zero + '"  and  balance_time1' \
                                                                          ' <= "' + end_date_24 + '"  and'
        if carNo:
            condition = condition + ' car_no = "'+carNo+'"  and'
        if balance_Id:
            condition = condition + ' balance_id = "'+balance_Id+'" and'
        if cargo_name:
            condition = condition + ' goods_name = "' + cargo_name + '" and'
        if receiver_name:
            condition = condition + ' receiver = "'+receiver_name+'" and'
        if supply_name:
            condition = condition + ' supplier = "'+supply_name+'" and'
        condition = condition[:-3]
        query_sql = 'select balance_id,car_no,total_weight,leather_weight,actual_weight,balance_time1,' \
                    'balance_time2,goods_name,receiver,supplier,operator from t_balance'+condition
        logging.debug(query_sql)
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
        self.printPushButton.clicked.connect(self.printViaHtml)
        self.excelPushButton_2.clicked.connect(self.writeexcel)
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.Letter)
        self.table = QTableWidget()

    def writeexcel(self):
        book = Workbook(encoding='utf-8')
        sheet = book.add_sheet('Sheet1')  # 创建一个sheet
        # -----样式设置----------------
        alignment = xlwt.Alignment()  # 创建居中
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 可取值: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 可取值: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
        style = xlwt.XFStyle()  # 创建样式
        style.alignment = alignment  # 给样式添加文字居中属性
        style.font.height = 430  # 设置字体大小

        # ----------设置列宽高--------------
        col1 = sheet.col(0)  # 获取第0列
        col1.width = 380 * 20  # 设置第0列的宽为380，高为20
        query_sql = 'select * from t_system_params_conf'
        data_list = self.db.query(query_sql)
        company = list(data_list[0].values())[2]
        header = company+'报表'
        sheet.write_merge(0, 0, 0, 7, header, style)
        row_no = self.tableView.model().rowCount()
        sheet.write(1, 0, '单号')
        sheet.write(1, 1, '车号')
        sheet.write(1, 2, '毛重')
        sheet.write(1, 3, '皮重')
        sheet.write(1, 4, '净重')
        sheet.write(1, 5, '货物名称')
        sheet.write(1, 6, '供货单位')
        sheet.write(1, 7, '收货单位')
        for row in range(row_no):
            balance_id = self.tableView.model().index(row, 0).data()
            if self.tableView.model().index(row, 1).data() == None:
                car_No = ''
            else:
                car_No = self.tableView.model().index(row, 1).data()
            total_weight = self.tableView.model().index(row, 2).data()
            leather_weight = self.tableView.model().index(row, 3).data()
            actual_weight = self.tableView.model().index(row, 4).data()
            if self.tableView.model().index(row, 7).data() == None:
                goods_name = ''
            else:
                goods_name = self.tableView.model().index(row, 7).data()
            if self.tableView.model().index(row, 8).data() == None:
                supplier = ''
            else:
                supplier = self.tableView.model().index(row, 8).data()
            if self.tableView.model().index(row, 9).data() == None:
                receiver = ''
            else:
                receiver = self.tableView.model().index(row, 9).data()
            row=row+2
            sheet.write(row, 0, balance_id)
            sheet.write(row, 1, car_No)
            sheet.write(row, 2, total_weight)
            sheet.write(row, 3, leather_weight)
            sheet.write(row, 4, actual_weight)
            sheet.write(row, 5, goods_name)
            sheet.write(row, 6, supplier)
            sheet.write(row, 7, receiver)
        today_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = "d:/balance_plat"
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)
        if book.save('d:/balance_plat/报表'+str(today_date)+'.xls'):
            QtWidgets.QMessageBox.warning(self, '本程序', "导出失败！", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "导出成功！", QtWidgets.QMessageBox.Ok)

    def printViaHtml(self):
        htmltext = ""
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        query_sql = 'select * from t_system_params_conf'
        data_list = self.db.query(query_sql)
        company = list(data_list[0].values())[2]
        htmltext += (
                   "<p align=center ><font size=65>{0}报表</font></p>"
                   "</p><p> </p><p>  <p align=right>{1}</p>"
                   "<table  align=center cellpadding=0  border=0.5 cellspacing=0 width=100%> "
                   "<thead><tr><th>单号</th><th>车号</th>"
                   "<th>毛重</th><th>皮重</th>"
                   "<th>净重</th><th>货物名称</th>"
                   "<th>供货单位</th><th>收货单位</th></tr></thead>".format(company, date)
               )
        row_no = self.tableView.model().rowCount()
        for row in range(row_no):
            balance_id = self.tableView.model().index(row, 0).data()
            if self.tableView.model().index(row, 1).data() ==None:
                car_No =''
            else:
                car_No = self.tableView.model().index(row, 1).data()
            total_weight = self.tableView.model().index(row, 2).data()
            leather_weight = self.tableView.model().index(row, 3).data()
            actual_weight = self.tableView.model().index(row, 4).data()
            if self.tableView.model().index(row, 7).data()==None:
                goods_name = ''
            else:
                goods_name = self.tableView.model().index(row, 7).data()
            if self.tableView.model().index(row, 8).data()==None:
                supplier =''
            else:
                supplier = self.tableView.model().index(row, 8).data()
            if self.tableView.model().index(row, 9).data()==None:
                receiver =''
            else:
                receiver=self.tableView.model().index(row, 9).data()
            # balance_id = self.tableView.model().index(row, 8).data()
            htmltext += ("<tr><td align=center>{0}</td>"
                         "<td align=center>{1}</td>"
                         "<td align=center>{2}</td>"
                         "<td align=center>{3}</td>"
                         "<td align=center>{4}</td>"
                         "<td align=center>{5}</td>"
                         "<td align=center>{6}</td>"
                         "<td align=center>{7}</td>"
                         "</tr>".format(
                      balance_id,car_No,total_weight,leather_weight,actual_weight,goods_name,supplier,receiver))

        htmltext += (
                    "</table>")

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(htmltext)
            document.print_(self.printer)

    def print_data(self):
        QtWidgets.QMessageBox.information(self, u'本程序', u'打印成功!', QtWidgets.QMessageBox.Ok)

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(PollResultForm, self).show()
        header = ['单号', '车牌号', '毛重', '皮重', '净重', '称重时间1',  '称重时间2', '货物名', '收货单位',  '供货单位',
                  '操作员']
        row_no, col_no = len(column), len(header)
        model = QStandardItemModel(row_no, col_no)
        model.setHorizontalHeaderLabels(header)
        totalweight = 0.0
        leatherweight = 0.0
        actualweight = 0.0
        for row in range(row_no):
            values = list(column[row].values())
            totalweight = float(totalweight) + float(str(values[2]))
            leatherweight = float(leatherweight) + float(str(values[3]))
            actualweight = float(actualweight) + float(str(values[4]))
            for col in range(col_no):
                item = QStandardItem(str(values[col]))
                model.setItem(row, col, item)
        model.setItem(int(row_no), 0, QStandardItem('总计'))
        model.setItem(int(row_no), 2, QStandardItem(str(totalweight)))
        model.setItem(int(row_no), 3, QStandardItem(str(leatherweight)))
        model.setItem(int(row_no), 4, QStandardItem(str(actualweight)))
        self.tableView.setModel(model)
        # self.tableView.doubleClicked.connect(lambda x: self.display_data(column[int(x.row())]))
        self.tableView.doubleClicked.connect(self.__display_data)

    def __display_data(self, index):
        """
               返显数据
               :param index:
               :return:
               """
        if index:
            if self.tableView.model().index(index.row(), 0).data()!="总计":
                id = int(self.tableView.model().index(index.row(), 0).data())
                # self.balance_detail.my_signal.connect(self.set_table_view)
                self.balance_detail.show(id)

        else:
            QtWidgets.QMessageBox.question(self,
                                           '本程序')



    def display_data(self, data):
        print("121212")
        if data:
            id = int(data.get('balance_id', '1'))
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
        self.printPushButton.clicked.connect(self.print_data)
        self.rmf_path = os.path.join(os.getcwd(), r'rmf\rmf')
        self.report_file = os.path.join(os.getcwd(), r'rmf\RMReport.exe')

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(Balance_detailDialog, self).show()
        self.receiverComboBox.clear()
        self.supplierComboBox.clear()
        query_sql = 'select balance_id,car_no,total_weight,leather_weight,actual_weight,balance_time1,' \
                    'balance_time2,goods_name,receiver,supplier,operator from t_balance  ' \
                    'where balance_id = %s' % (column)
        data_list = self.db.query(query_sql)
        supply_query_sql = 'select supplier_name from t_supplier'
        supply_list = self.db.query(supply_query_sql)
        supply_row_no = len(supply_list)
        logging.debug(supply_row_no)
        for row in range(supply_row_no):
            values = list(supply_list[row].values())[0]
            self.supplierComboBox.addItem(values)
        self.supplierComboBox.clearEditText()
        receiver_query_sql = 'select receiver_name from t_receiver'
        receiver_list = self.db.query(receiver_query_sql)
        receiver_row_no = len(receiver_list)
        for row in range(receiver_row_no):
            values = list(receiver_list[row].values())[0]
            self.receiverComboBox.addItem(values)
        self.receiverComboBox.clearEditText()
        self.balanceNoLineEdit.setMaxLength(16)
        self.balanceNoLineEdit.setText(str(list(data_list[0].values())[0]))
        logging.debug(self.balanceNoLineEdit.text())
        self.carNoLineEdit.setText(str(list(data_list[0].values())[1]))
        self.totalWeightLineEdit.setText(str(list(data_list[0].values())[2]))
        self.leatherWeightLineEdit.setText(str(list(data_list[0].values())[3]))
        self.actualWeightLineEdit.setText(str(list(data_list[0].values())[4]))
        self.leatherWeighttimeLineEdit.setText(str(list(data_list[0].values())[5]))
        self.totalWeighttimeLineEdit.setText(str(list(data_list[0].values())[6]))
        self.cargoNameLineEdit.setText(str(list(data_list[0].values())[7]))
        self.receiverComboBox.setCurrentText(str(list(data_list[0].values())[8]))
        self.supplierComboBox.setCurrentText(str(list(data_list[0].values())[9]))
        self.operatorLineEdit_4.setText(str(list(data_list[0].values())[10]))

    def save_detail(self, warning=True):
        """
        保存item
        :return:
        """
        carNo = self.carNoLineEdit.text()
        totalWeight = self.totalWeightLineEdit.text()
        leatherWeight = self.leatherWeightLineEdit.text()
        goodnNmes = self.cargoNameLineEdit.text()
        receiverName = self.receiverComboBox.currentText()
        supplyName = self.supplierComboBox.currentText()
        operator = self.operatorLineEdit_4.text()
        balance_No = self.balanceNoLineEdit.text()
        insert_sql = 'update  t_balance set car_no=?,total_weight=?,leather_weight=?,goods_name=?,receiver=?,' \
                     'supplier=?,operator=? '  'where  balance_id = ?'
        logging.debug(insert_sql)
        ret = self.db.update(insert_sql, [carNo, totalWeight, leatherWeight, goodnNmes, receiverName,
                                          supplyName, operator, int(balance_No)])
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.receiverComboBox.clear()
            self.supplierComboBox.clear()
            self.close()
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)

    def cancel_detail(self):
        """
        取消更改
        :return:
        """
        self.receiverComboBox.clear()
        self.supplierComboBox.clear()
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
            self.receiverComboBox.clear()
            self.supplierComboBox.clear()
            self.close()
            self.my_signal.emit(self.table)

    def print_data(self):
        """
        打印
        :return:
        """
        balance_id = int(self.balanceNoLineEdit.text())
        self.save_detail(warning=False)
        sql = 'select default_rmf from t_rmf'
        ret = self.db.query(sql)
        logging.debug(self.balanceNoLineEdit.text())

        default_rmf = ret[0].get('default_rmf', u'过称单(标准式).rmf')
        cmd_str = self.report_file + u' -d "balance.db" -s "db1:select t_balance.* from t_balance where  balance_id=\'%s\'" -r "%s" -a 1' % (balance_id, default_rmf)
        # cmd_str = self.report_file + u' -d "balance.db" -s "db1:select t_balance.*,t_supplier.* from t_balance,t_supplier where  t_balance.supplier = t_supplier.supplier_name and balance_id=\'%s\'" -r "%s" -a 1' % (balance_id, default_rmf)
        logging.debug(cmd_str)
        logging.debug(cmd_str)
        self.p = subprocess.Popen(cmd_str)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = pollmainForm()
    myshow.show()
    sys.exit(app.exec_())
