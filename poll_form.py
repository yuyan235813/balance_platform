import datetime
import logging
import os
import subprocess

import xlwt
from PyQt5.QtCore import pyqtSignal, Qt, QDate
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QDialog, QApplication
from ui.balance_detail import Ui_balance_detailDialog
from ui.image_detail_dialog import Ui_imageDetailDialog
from ui.poll_main import Ui_PollmainForm
from utils import normal_utils
from utils.sqllite_util import EasySqlite
from utils.normal_utils import show_image, get_current_user_dir


class pollmainForm(QWidget, Ui_PollmainForm):
    """
    参数设置
    """
    def __init__(self, user_id):
        super(pollmainForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.user_id = user_id
        self.begindateEdit.setDate(QDate.currentDate())
        self.enddateEdit.setDate(QDate.currentDate())
        self.QueryPushButton.clicked.connect(self.poll_data)
        self.cancelPushButton.clicked.connect(self.cancel_pollForm)
        self.balance_detail = Balance_detailDialog(self)
        self.printPushButton.clicked.connect(self.printViaHtml)
        self.excelPushButton_2.clicked.connect(self.write_excel)
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.Letter)

    def show(self):
        """
        显示界面
        :return:
        """
        super().show()
        self.__init_data()

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        self.update_combobox()
        if self.tableView.model() and self.tableView.model().rowCount() > 1:
            self.printPushButton.setEnabled(True)
            self.excelPushButton_2.setEnabled(True)
        else:
            self.printPushButton.setEnabled(False)
            self.excelPushButton_2.setEnabled(False)

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
        self.CargoNamecomboBox.clear()
        for row in range(cargo_row_no):
            values = list(cargo_list[row].values())[0]
            self.CargoNamecomboBox.addItem(values)
        self.CargoNamecomboBox.clearEditText()
        supply_query_sql = 'select supplier_name from t_supplier'
        supply_list = self.db.query(supply_query_sql)
        supply_row_no = len(supply_list)
        self.SupplyNamecomboBox.clear()
        for row in range(supply_row_no):
            values = list(supply_list[row].values())[0]
            self.SupplyNamecomboBox.addItem(values)
        self.SupplyNamecomboBox.clearEditText()
        receiver_query_sql = 'select receiver_name from t_receiver'
        receiver_list = self.db.query(receiver_query_sql)
        receiver_row_no = len(receiver_list)
        self.ReceiverNamecomboBox.clear()
        for row in range(receiver_row_no):
            values = list(receiver_list[row].values())[0]
            self.ReceiverNamecomboBox.addItem(values)
        self.ReceiverNamecomboBox.clearEditText()

    def poll_data(self):
        """
        :return:
        """
        begin_date = str(self.begindateEdit.date().toPyDate())+' 00:00:00'
        end_date = str(self.enddateEdit.date().toPyDate())+' 23:59:59'
        carNo = self.CarNoLineEdit.text()
        receiver_name = self.ReceiverNamecomboBox.currentText()
        cargo_name = self.CargoNamecomboBox.currentText()
        supply_name = self.SupplyNamecomboBox.currentText()
        balance_Id = self.balanceNoLineEdit.text()
        condition = ' where'
        condition = condition + ' balance_time1 >= "' + begin_date + '"  and  balance_time1' \
                                                                          ' <= "' + end_date + '"  and'
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
        if self.CompleteradioButton.isChecked():
            condition = condition + ' status = 1'
        if self.UnCompleteradioButton.isChecked():
            condition = condition + ' status = 0'
        if self.AllradioButton.isChecked():
            condition = condition[:-3]
        # condition = condition[:-3]
        query_sql = 'select balance_id,car_no,total_weight,leather_weight,actual_weight,balance_time1,' \
                    'balance_time2,goods_name,receiver,supplier,operator from t_balance'+condition
        logging.debug(query_sql)
        data_list = self.db.query(query_sql)
        #self.show(data_list)
        header = ['单号', '车牌号', '毛重', '皮重', '净重', '毛重时间', '皮重时间', '货物名', '收货单位', '供货单位',
                  '操作员']
        row_no, col_no = len(data_list), len(header)
        model = QStandardItemModel(row_no, col_no)
        model.setHorizontalHeaderLabels(header)
        totalweight = 0.0
        leatherweight = 0.0
        actualweight = 0.0
        for row in range(row_no):
            values = list(data_list[row].values())
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
        if row_no > 0:
            self.printPushButton.setEnabled(True)
            self.excelPushButton_2.setEnabled(True)
        else:
            self.printPushButton.setEnabled(False)
            self.excelPushButton_2.setEnabled(False)

    def write_excel(self):
        """
        到处excel
        :return:
        """
        today_date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        dir = os.path.join(get_current_user_dir(), '报表_%s.xls' % str(today_date))
        file_name, file_type = QFileDialog.getSaveFileName(self,
                                                           "报表导出",
                                                           dir,
                                                           "EXCEL(*.xls)")
        if file_name == "":
            return
        book = xlwt.Workbook(encoding='utf-8')
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
        header = company + '报表'
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
            row = row + 2
            sheet.write(row, 0, balance_id)
            sheet.write(row, 1, car_No)
            sheet.write(row, 2, total_weight)
            sheet.write(row, 3, leather_weight)
            sheet.write(row, 4, actual_weight)
            sheet.write(row, 5, goods_name)
            sheet.write(row, 6, supplier)
            sheet.write(row, 7, receiver)
        if book.save(file_name):
            QMessageBox.warning(self, '本程序', "导出失败！", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, '本程序', "导出成功！", QMessageBox.Ok)

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
                balance_id, car_No, total_weight, leather_weight, actual_weight, goods_name, supplier, receiver))

        htmltext += (
            "</table>")

        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(htmltext)
            document.print_(self.printer)

    def print_data(self):
        QMessageBox.information(self, u'本程序', u'打印成功!', QMessageBox.Ok)

    # def show(self, column):
    #     """
    #     显示ui
    #     :return:
    #     """
    #     super(PollResultForm, self).show()
    #     header = ['单号', '车牌号', '毛重', '皮重', '净重', '毛重时间', '皮重时间', '货物名', '收货单位', '供货单位',
    #               '操作员']
    #     row_no, col_no = len(column), len(header)
    #     model = QStandardItemModel(row_no, col_no)
    #     model.setHorizontalHeaderLabels(header)
    #     totalweight = 0.0
    #     leatherweight = 0.0
    #     actualweight = 0.0
    #     for row in range(row_no):
    #         values = list(column[row].values())
    #         totalweight = float(totalweight) + float(str(values[2]))
    #         leatherweight = float(leatherweight) + float(str(values[3]))
    #         actualweight = float(actualweight) + float(str(values[4]))
    #         for col in range(col_no):
    #             item = QStandardItem(str(values[col]))
    #             model.setItem(row, col, item)
    #     model.setItem(int(row_no), 0, QStandardItem('总计'))
    #     model.setItem(int(row_no), 2, QStandardItem(str(totalweight)))
    #     model.setItem(int(row_no), 3, QStandardItem(str(leatherweight)))
    #     model.setItem(int(row_no), 4, QStandardItem(str(actualweight)))
    #     self.tableView.setModel(model)
    #     # self.tableView.doubleClicked.connect(lambda x: self.display_data(column[int(x.row())]))
    #     self.tableView.doubleClicked.connect(self.__display_data)

    def __display_data(self, index):
        """
               返显数据
               :param index:
               :return:
               """
        if index:
            if self.tableView.model().index(index.row(), 0).data() != "总计":
                id = int(self.tableView.model().index(index.row(), 0).data())
                # self.balance_detail.my_signal.connect(self.set_table_view)
                self.balance_detail.show(id)

        else:
            QMessageBox.question(self, '本程序')

    def display_data(self, data):
        if data:
            id = int(data.get('balance_id', '1'))
            # self.balance_detail.my_signal.connect(self.set_table_view)
            self.balance_detail.show(id)
        else:
            QMessageBox.question(self, '本程序')


# class PollResultForm(QWidget, Ui_PollResultForm):
#     """
#     参数修改
#     """
#     my_signal = pyqtSignal(str)
#
#     def __init__(self, parent):
#         super(PollResultForm, self).__init__()
#         self.setupUi(self)
#         # 自定义信号
#         self.table = ''
#         self.column = ''
#         self.db = EasySqlite(r'rmf/db/balance.db')
#         self.setWindowModality(Qt.ApplicationModal)
#         self.balance_detail = Balance_detailDialog(self)
#         self.printPushButton.clicked.connect(self.printViaHtml)
#         self.excelPushButton_2.clicked.connect(self.write_excel)
#         self.printer = QPrinter()
#         self.printer.setPageSize(QPrinter.Letter)
#         self.table = QTableWidget()
#
#     def write_excel(self):
#         """
#         到处excel
#         :return:
#         """
#         today_date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#         dir = os.path.join(get_current_user_dir(), '报表_%s.xls'% str(today_date))
#         file_name, file_type = QFileDialog.getSaveFileName(self,
#                                                            "报表导出",
#                                                            dir,
#                                                            "EXCEL(*.xls)")
#         if file_name == "":
#             return
#         book = xlwt.Workbook(encoding='utf-8')
#         sheet = book.add_sheet('Sheet1')  # 创建一个sheet
#         # -----样式设置----------------
#         alignment = xlwt.Alignment()  # 创建居中
#         alignment.horz = xlwt.Alignment.HORZ_CENTER  # 可取值: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
#         alignment.vert = xlwt.Alignment.VERT_CENTER  # 可取值: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
#         style = xlwt.XFStyle()  # 创建样式
#         style.alignment = alignment  # 给样式添加文字居中属性
#         style.font.height = 430  # 设置字体大小
#
#         # ----------设置列宽高--------------
#         col1 = sheet.col(0)  # 获取第0列
#         col1.width = 380 * 20  # 设置第0列的宽为380，高为20
#         query_sql = 'select * from t_system_params_conf'
#         data_list = self.db.query(query_sql)
#         company = list(data_list[0].values())[2]
#         header = company+'报表'
#         sheet.write_merge(0, 0, 0, 7, header, style)
#         row_no = self.tableView.model().rowCount()
#         sheet.write(1, 0, '单号')
#         sheet.write(1, 1, '车号')
#         sheet.write(1, 2, '毛重')
#         sheet.write(1, 3, '皮重')
#         sheet.write(1, 4, '净重')
#         sheet.write(1, 5, '货物名称')
#         sheet.write(1, 6, '供货单位')
#         sheet.write(1, 7, '收货单位')
#         for row in range(row_no):
#             balance_id = self.tableView.model().index(row, 0).data()
#             if self.tableView.model().index(row, 1).data() == None:
#                 car_No = ''
#             else:
#                 car_No = self.tableView.model().index(row, 1).data()
#             total_weight = self.tableView.model().index(row, 2).data()
#             leather_weight = self.tableView.model().index(row, 3).data()
#             actual_weight = self.tableView.model().index(row, 4).data()
#             if self.tableView.model().index(row, 7).data() == None:
#                 goods_name = ''
#             else:
#                 goods_name = self.tableView.model().index(row, 7).data()
#             if self.tableView.model().index(row, 8).data() == None:
#                 supplier = ''
#             else:
#                 supplier = self.tableView.model().index(row, 8).data()
#             if self.tableView.model().index(row, 9).data() == None:
#                 receiver = ''
#             else:
#                 receiver = self.tableView.model().index(row, 9).data()
#             row=row+2
#             sheet.write(row, 0, balance_id)
#             sheet.write(row, 1, car_No)
#             sheet.write(row, 2, total_weight)
#             sheet.write(row, 3, leather_weight)
#             sheet.write(row, 4, actual_weight)
#             sheet.write(row, 5, goods_name)
#             sheet.write(row, 6, supplier)
#             sheet.write(row, 7, receiver)
#         if book.save(file_name):
#             QMessageBox.warning(self, '本程序', "导出失败！", QMessageBox.Ok)
#         else:
#             QMessageBox.warning(self, '本程序', "导出成功！", QMessageBox.Ok)
#
#     def printViaHtml(self):
#         htmltext = ""
#         date = datetime.datetime.now().strftime('%Y-%m-%d')
#         query_sql = 'select * from t_system_params_conf'
#         data_list = self.db.query(query_sql)
#         company = list(data_list[0].values())[2]
#         htmltext += (
#                    "<p align=center ><font size=65>{0}报表</font></p>"
#                    "</p><p> </p><p>  <p align=right>{1}</p>"
#                    "<table  align=center cellpadding=0  border=0.5 cellspacing=0 width=100%> "
#                    "<thead><tr><th>单号</th><th>车号</th>"
#                    "<th>毛重</th><th>皮重</th>"
#                    "<th>净重</th><th>货物名称</th>"
#                    "<th>供货单位</th><th>收货单位</th></tr></thead>".format(company, date)
#                )
#         row_no = self.tableView.model().rowCount()
#         for row in range(row_no):
#             balance_id = self.tableView.model().index(row, 0).data()
#             if self.tableView.model().index(row, 1).data() ==None:
#                 car_No =''
#             else:
#                 car_No = self.tableView.model().index(row, 1).data()
#             total_weight = self.tableView.model().index(row, 2).data()
#             leather_weight = self.tableView.model().index(row, 3).data()
#             actual_weight = self.tableView.model().index(row, 4).data()
#             if self.tableView.model().index(row, 7).data()==None:
#                 goods_name = ''
#             else:
#                 goods_name = self.tableView.model().index(row, 7).data()
#             if self.tableView.model().index(row, 8).data()==None:
#                 supplier =''
#             else:
#                 supplier = self.tableView.model().index(row, 8).data()
#             if self.tableView.model().index(row, 9).data()==None:
#                 receiver =''
#             else:
#                 receiver=self.tableView.model().index(row, 9).data()
#             # balance_id = self.tableView.model().index(row, 8).data()
#             htmltext += ("<tr><td align=center>{0}</td>"
#                          "<td align=center>{1}</td>"
#                          "<td align=center>{2}</td>"
#                          "<td align=center>{3}</td>"
#                          "<td align=center>{4}</td>"
#                          "<td align=center>{5}</td>"
#                          "<td align=center>{6}</td>"
#                          "<td align=center>{7}</td>"
#                          "</tr>".format(
#                       balance_id,car_No,total_weight,leather_weight,actual_weight,goods_name,supplier,receiver))
#
#         htmltext += (
#                     "</table>")
#
#         dialog = QPrintDialog(self.printer, self)
#         if dialog.exec_():
#             document = QTextDocument()
#             document.setHtml(htmltext)
#             document.print_(self.printer)
#
#     def print_data(self):
#         QMessageBox.information(self, u'本程序', u'打印成功!', QMessageBox.Ok)
#
#     def show(self, column):
#         """
#         显示ui
#         :return:
#         """
#         super(PollResultForm, self).show()
#         header = ['单号', '车牌号', '毛重', '皮重', '净重', '毛重时间',  '皮重时间', '货物名', '收货单位',  '供货单位',
#                   '操作员']
#         row_no, col_no = len(column), len(header)
#         model = QStandardItemModel(row_no, col_no)
#         model.setHorizontalHeaderLabels(header)
#         totalweight = 0.0
#         leatherweight = 0.0
#         actualweight = 0.0
#         for row in range(row_no):
#             values = list(column[row].values())
#             totalweight = float(totalweight) + float(str(values[2]))
#             leatherweight = float(leatherweight) + float(str(values[3]))
#             actualweight = float(actualweight) + float(str(values[4]))
#             for col in range(col_no):
#                 item = QStandardItem(str(values[col]))
#                 model.setItem(row, col, item)
#         model.setItem(int(row_no), 0, QStandardItem('总计'))
#         model.setItem(int(row_no), 2, QStandardItem(str(totalweight)))
#         model.setItem(int(row_no), 3, QStandardItem(str(leatherweight)))
#         model.setItem(int(row_no), 4, QStandardItem(str(actualweight)))
#         self.tableView.setModel(model)
#         # self.tableView.doubleClicked.connect(lambda x: self.display_data(column[int(x.row())]))
#         self.tableView.doubleClicked.connect(self.__display_data)
#
#     def __display_data(self, index):
#         """
#                返显数据
#                :param index:
#                :return:
#                """
#         if index:
#             if self.tableView.model().index(index.row(), 0).data()!="总计":
#                 id = int(self.tableView.model().index(index.row(), 0).data())
#                 # self.balance_detail.my_signal.connect(self.set_table_view)
#                 self.balance_detail.show(id)
#
#         else:
#             QMessageBox.question(self, '本程序')
#
#
#
#     def display_data(self, data):
#         if data:
#             id = int(data.get('balance_id', '1'))
#             # self.balance_detail.my_signal.connect(self.set_table_view)
#             self.balance_detail.show(id)
#         else:
#             QMessageBox.question(self, '本程序')


class Balance_detailDialog(QDialog, Ui_balance_detailDialog):
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
        self.image_detail_dialog = ImageDetailDialog()
        self.graphicsView_1.doubleClicked.connect(self.image_detail_dialog.show)
        self.graphicsView_2.doubleClicked.connect(self.image_detail_dialog.show)
        self.graphicsView_3.doubleClicked.connect(self.image_detail_dialog.show)
        self.graphicsView_4.doubleClicked.connect(self.image_detail_dialog.show)
        self.graphicsView_5.doubleClicked.connect(self.image_detail_dialog.show)
        self.graphicsView_6.doubleClicked.connect(self.image_detail_dialog.show)
        self.graphicsView_7.doubleClicked.connect(self.image_detail_dialog.show)
        self.graphicsView_8.doubleClicked.connect(self.image_detail_dialog.show)
        self.parent=parent

    def show(self, column):
        """
        显示ui
        :return:
        """
        super(Balance_detailDialog, self).show()
        self.__init_permissions()
        self.receiverComboBox.clear()
        self.supplierComboBox.clear()
        query_sql = 'select balance_id,car_no,total_weight,leather_weight,actual_weight,balance_time2,' \
                    'balance_time1,goods_name,receiver,supplier,operator,ext1,ext2 from t_balance  ' \
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
        count = 0
        while (count < 4):
            count = count + 1
            path1 = str(list(data_list[0].values())[11])+'0'+str(count)+'.png'
            path2 = str(list(data_list[0].values())[12]) + '0' + str(count) + '.png'
            if os.path.isfile(path1):
                if count==1:
                    show_image(path1, self.graphicsView_1)
                if count == 2:
                    show_image(path1, self.graphicsView_2)
                if count == 3:
                    show_image(path1, self.graphicsView_3)
                if count == 4:
                    show_image(path1, self.graphicsView_4)
            if os.path.isfile(path2):
                if count==1:
                    show_image(path2, self.graphicsView_5)
                if count == 2:
                    show_image(path2, self.graphicsView_6)
                if count == 3:
                    show_image(path2, self.graphicsView_7)
                if count == 4:
                    show_image(path2, self.graphicsView_8)

    def __init_permissions(self):
        """
        初始化权限
        :return:
        """
        perminsion_dict = dict(
            {
                'poll_form_change': self.savePushButton,
                'poll_form_delete': self.deletePushButton
            }
        )
        for k, v in perminsion_dict.items():
            v.setEnabled(False)
        user_permission = normal_utils.get_user_permission(self.parent.user_id)
        for item in user_permission:
            if item in perminsion_dict.keys():
                perminsion_dict.get(item).setEnabled(True)

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
            # QMessageBox.information(self, u'本程序', u'保存成功!', QMessageBox.Ok)
            self.receiverComboBox.clear()
            self.supplierComboBox.clear()
            self.close()
            self.parent.poll_data()
        else:
            QMessageBox.warning(self, u'本程序', u'保存失败:\n', QMessageBox.Ok)

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
        query_sql =  'select ext1,ext2  from t_balance where  balance_id = ?'
        delete_sql = 'delete from t_balance where  balance_id = ?'
        ret_query = self.db.update
        data_list = self.db.query(query_sql, [int(balance_id)])
        count = 0
        while (count < 4):
            count = count + 1
            path1 = str(list(data_list[0].values())[0]) + '0' + str(count) + '.png'
            path2 = str(list(data_list[0].values())[1]) + '0' + str(count) + '.png'
            if os.path.isfile(path1):
                if count == 1:
                    if os.path.exists(path1):
                        os.remove(path1)
                if count == 2:
                    if os.path.exists(path1):
                        os.remove(path1)
                if count == 3:
                    if os.path.exists(path1):
                        os.remove(path1)
                if count == 4:
                    if os.path.exists(path1):
                        os.remove(path1)
            if os.path.isfile(path2):
                if count == 1:
                    if os.path.exists(path2):
                        os.remove(path2)
                if count == 2:
                    if os.path.exists(path2):
                        os.remove(path2)
                if count == 3:
                    if os.path.exists(path2):
                        os.remove(path2)
                if count == 4:
                    if os.path.exists(path2):
                        os.remove(path2)
        ret = self.db.update(delete_sql, [int(balance_id)])
        if ret:
            QMessageBox.information(self, u'本程序', u'删除成功!', QMessageBox.Ok)
            self.receiverComboBox.clear()
            self.supplierComboBox.clear()
            self.close()
            self.parent.poll_data()
            #self.my_signal.emit(self.pollmain)
            #self.my_signal.connect(self.)
        else:
            QMessageBox.warning(self, u'本程序', u'删除失败:\n', QMessageBox.Ok)

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


class ImageDetailDialog(QDialog, Ui_imageDetailDialog):
    """
    图片查看
    """
    def __init__(self):
        super(ImageDetailDialog, self).__init__()
        self.setupUi(self)
        self.desktop = QApplication.desktop()
        self.setFixedSize(self.desktop.width(), self.desktop.height());
        self.setWindowModality(Qt.ApplicationModal)

    def show(self, path):
        """
        显示界面
        :param path:
        :return:
        """
        if os.path.exists(path):
            super(ImageDetailDialog, self).show()
            show_image(path, self.graphicsView_1, True)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myshow = pollmainForm()
    myshow.show()
    sys.exit(app.exec_())
