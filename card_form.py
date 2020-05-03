#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDate, QModelIndex, QDateTime
from PyQt5 import QtSql
from ui.card_form import Ui_cardFrom
from car_no_dialog_form import CarNoDialogForm
from all_in_one_test import AIODll
from functools import partial
import time
import logging
import datetime
import normal_utils


class CardForm(QtWidgets.QWidget, Ui_cardFrom):
    """
    超级管理界面
    """
    def __init__(self):
        super(CardForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        if QtSql.QSqlDatabase.contains("qt_sql_default_connection"):
            self.db = QtSql.QSqlDatabase.database("qt_sql_default_connection")
        else:
            self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("rmf/db/balance.db")
        self.queryPushButton.clicked.connect(self.__query_data)
        self.addPushButton.clicked.connect(self.__add_data)
        self.savePushButton.clicked.connect(self.__change_data)
        self.deletePushButton.clicked.connect(self.__delete_data)
        self.cancelPushButton.clicked.connect(self.close)
        self.issuePushButton.clicked.connect(self.__issue_card)
        self.readPushButton.clicked.connect(self.__read_card)
        self.dialog = CarNoDialogForm()
        self.carNoPushButton.clicked.connect(partial(self.__show_dialog, self.carNoLineEdit))
        self.carNoPushButton_2.clicked.connect(partial(self.__show_dialog, self.carNoLineEdit_2))
        self.table = 't_card_info'
        self.db_model = QtSql.QSqlTableModel()
        self.tableView.verticalHeader().hide()
        self.tableView.setItemDelegate(CardInfoDelegate(self.tableView))
        self.tableView.setColumnHidden(0, True)
        self.tableView.doubleClicked.connect(self.__display_data)
        self.read_card_no = 0
        self.row = -1
        # self.__init_data()

    def show(self):
        super().show()
        self.__init_data()

    def __show_dialog(self, carNoLineEdit:QtWidgets.QLineEdit):
        self.dialog.my_signal.connect(carNoLineEdit.setText)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.show()
        window_point = self.pos()
        point = carNoLineEdit.pos()
        point.setX(point.x() + window_point.x())
        point.setY(point.y() + window_point.y() + 65)
        self.dialog.move(point)

    def update_combobox(self):
        """
        下拉列表数据
        :return:
        """
        cargo_query_sql = 'select name from t_cargo'
        cargo_list = self.db.exec(cargo_query_sql)
        self.cargocomboBox.clear()
        while (cargo_list.next()):
            self.cargocomboBox.addItem(cargo_list.value(0))
        self.cargocomboBox.clearEditText()
        supply_query_sql = 'select supplier_name from t_supplier'
        supply_list = self.db.exec(supply_query_sql)
        self.suppliercomboBox.clear()
        while (supply_list.next()):
            self.suppliercomboBox.addItem(supply_list.value(0))
        self.suppliercomboBox.clearEditText()
        receiver_query_sql = 'select receiver_name from t_receiver'
        receiver_list = self.db.exec(receiver_query_sql)
        self.receivercomboBox.clear()
        while (receiver_list.next()):
            self.receivercomboBox.addItem(receiver_list.value(0))
        self.receivercomboBox.clearEditText()

    def __init_data(self):
        """
        初始化数据
        :return:
        """
        self.beginDateEdit.setDate(QDate.currentDate())
        self.endDateEdit.setDate(QDate.currentDate())
        self.validDateEdit.setDate(datetime.date.today()+ datetime.timedelta(days=366))
        self.enrollDateEdit.setDate(QDate.currentDate())
        self.__query_data()
        self.update_combobox()

    def __issue_card(self):
        """
        发行卡片
        :return:
        """
        row = self.tableView.currentIndex().row()
        if row < 0:
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要发行的记录！", QtWidgets.QMessageBox.Ok)
            return
        record = self.db_model.record(row)
        card_no = record.value(4)
        valid_date = record.value(6)
        anti_back = False
        card_type = record.value(3)
        is_use = True
        res = self.db.exec("select issue_com from t_com_auto where id = 1")
        port = int(res.value(0)) if res.next() else -1
        if port == -1:
            QtWidgets.QMessageBox.warning(self, '本程序', "获取发卡器配置失败！", QtWidgets.QMessageBox.Ok)
            return
        dll = AIODll()
        is_open = dll.open_com(port)
        if not is_open:
            QtWidgets.QMessageBox.information(self, '本程序', "连接发卡器失败！", QtWidgets.QMessageBox.Ok)
            return
        res = dll.issue_card(card_no, valid_date, anti_back, card_type, is_use)
        if not res:
            print("发行成功！")
            record.setValue(19, 1)
            success = self.db_model.setRecord(row, record)
            ret = self.db_model.submitAll()
            if ret and success:
                QtWidgets.QMessageBox.information(self, '本程序', "发行成功！", QtWidgets.QMessageBox.Ok)
                self.__query_data(2)
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "发行失败，请重试！", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "发行失败，请重试！", QtWidgets.QMessageBox.Ok)
            print("发行失败！！！！")
        dll.close_com()

    def __read_card(self):
        """
        读取卡片
        :return:
        """
        res = self.db.exec("select issue_com from t_com_auto where id = 1")
        port = int(res.value(0)) if res.next() else -1
        if port == -1:
            QtWidgets.QMessageBox.warning(self, '本程序', "获取发卡器配置失败！", QtWidgets.QMessageBox.Ok)
            return
        dll = AIODll()
        is_open = dll.open_com(port)
        if not is_open:
            QtWidgets.QMessageBox.information(self, '本程序', "连接发卡器失败！", QtWidgets.QMessageBox.Ok)
            return
        data = dict()
        res = dll.read_user_card(data)
        if res or not 'card_no' in data:
            print(res)
            return
        card_no = data['card_no']
        self.read_card_no = card_no
        dll.close_com()
        self.__query_data()
        self.read_card_no = 0
        if self.db_model.rowCount() == 0:
            print("没有卡信息")
            return

    def __display_data(self, index: QModelIndex):
        """
        返显数据
        :param index:
        :return:
        """
        self.row = index.row()
        record = self.db_model.record(index.row())
        user_name = record.value(1)
        gender = '男' if record.value(2) == 1 else '女'
        card_type = "月卡"
        if record.value(3) == 2:
            card_type = "临时卡"
        elif record.value(3) == 3:
            card_type = "免费卡"
        enroll_date = record.value(5)
        valid_date = record.value(6)
        card_status = "有" if record.value(7) == 1 else "无"
        phone_number = record.value(8)
        cred_no = record.value(9)
        car_no = record.value(10)
        address = record.value(11)
        # operation_date = str(QDate.currentDate().toPyDate())
        supplier = record.value(14)
        receiver = record.value(15)
        cargo = record.value(16)
        extra = record.value(17)
        price = record.value(18)

        self.userNameLineEdit_2.setText(user_name)
        self.genderComboBox.setCurrentText(gender)
        self.cardTypeComboBox.setCurrentText(card_type)
        self.enrollDateEdit.setDate(QDate.fromString(enroll_date, "yyyy-MM-dd"))
        self.validDateEdit.setDate(QDate.fromString(valid_date, "yyyy-MM-dd"))
        self.isValidComboBox.setCurrentText(card_status)
        self.phoneNumberLineEdit.setText(phone_number)
        self.credNoLineEdit.setText(cred_no)
        self.carNoLineEdit_2.setText(car_no)
        self.addressLineEdit.setText(address)
        self.suppliercomboBox.setCurrentText(supplier)
        self.receivercomboBox.setCurrentText(receiver)
        self.cargocomboBox.setCurrentText(cargo)
        self.extraDoubleSpinBox.setValue(extra)
        self.priceDoubleSpinBox.setValue(price)

    def __query(self):
        """
        查询按钮
        :return:
        """
        self.read_card_no = 0
        self.__query_data()

    def __query_data(self, type = 0):
        """
        查询数据
        :param card_no:
        :return:
        """
        begin_date = str(self.beginDateEdit.date().toPyDate())
        end_date = str(self.endDateEdit.date().toPyDate())
        car_no = self.carNoLineEdit.text()
        user_name = self.userNameLineEdit.text()
        supplier = self.supplierLineEdit.text()
        receiver = self.receiverLineEdit.text()
        issued = 'status = 1' if self.issuedRadioButton.isChecked() else 'status = 0'
        if type == 1:
            issued = 'status = 0'
        elif type == 2:
            issued = 'status = 1'
        condition = 'enroll_date >= "' + begin_date + '" and enroll_date' \
                                                          ' <= "' + end_date + '" and '
        if car_no:
            condition += 'car_no = "%s" and ' % car_no
        if user_name:
            condition += 'user_name = "%s" and ' % user_name
        if supplier:
            condition += 'supplier like "%' + supplier + '%" and '
        if receiver:
            condition += 'receiver like "%' + supplier + '%" and '
        condition += issued
        if self.read_card_no:
            condition = 'card_no ="%s" and status = 1' % self.read_card_no
        if self.db.open():
            self.db_model.setTable(self.table)
            self.db_model.setFilter(condition)
            self.db_model.select()
            self.db_model.setHeaderData(0, Qt.Horizontal, '序号')
            self.db_model.setHeaderData(1, Qt.Horizontal, '用户姓名')
            self.db_model.setHeaderData(2, Qt.Horizontal, '性别')
            self.db_model.setHeaderData(3, Qt.Horizontal, '卡片类型')
            self.db_model.setHeaderData(4, Qt.Horizontal, '卡号')
            self.db_model.setHeaderData(5, Qt.Horizontal, '登记日期')
            self.db_model.setHeaderData(6, Qt.Horizontal, '有效期')
            self.db_model.setHeaderData(7, Qt.Horizontal, '卡片是否有效')
            self.db_model.setHeaderData(8, Qt.Horizontal, '电话号码')
            self.db_model.setHeaderData(9, Qt.Horizontal, '证件号码')
            self.db_model.setHeaderData(10, Qt.Horizontal, '车牌号')
            self.db_model.setHeaderData(11, Qt.Horizontal, '地址')
            self.db_model.setHeaderData(12, Qt.Horizontal, '操作员编号')
            self.db_model.setHeaderData(13, Qt.Horizontal, '操作日期')
            self.db_model.setHeaderData(14, Qt.Horizontal, '供货单位')
            self.db_model.setHeaderData(15, Qt.Horizontal, '收货单位')
            self.db_model.setHeaderData(16, Qt.Horizontal, '货物名称')
            self.db_model.setHeaderData(17, Qt.Horizontal, '另扣')
            self.db_model.setHeaderData(18, Qt.Horizontal, '价格')
            self.db_model.setHeaderData(19, Qt.Horizontal, '状态')
            self.db_model.setHeaderData(20, Qt.Horizontal, '扩展1')
            self.db_model.setHeaderData(21, Qt.Horizontal, '扩展2')
            self.db_model.setHeaderData(22, Qt.Horizontal, '扩展3')
            self.db_model.setHeaderData(23, Qt.Horizontal, '扩展4')
            print(condition)
            self.tableView.setModel(self.db_model)
            max_card_no_query = self.db.exec('select max(cast(card_no as int)) from t_card_info')
            ret = max_card_no_query.next()
            self.max_card_no = int(max_card_no_query.value(0)) if ret and max_card_no_query.value(0) != '' else -1
        self.tableView.setColumnHidden(0, True)

    def __change_data(self):
        """
        修改数据
        :return:
        """
        self.__add_data(True)
        self.row = -1

    def __add_data(self, change_data=False):
        """
        添加数据
        :return:
        """
        user_name = self.userNameLineEdit_2.text()
        if not user_name:
            QtWidgets.QMessageBox.warning(self, '本程序', "姓名不能为空！", QtWidgets.QMessageBox.Ok)
            return
        gender = self.genderComboBox.currentText()
        gender = 1 if gender == '男' else 0
        card_type = self.cardTypeComboBox.currentText()
        if card_type == '月卡':
            card_type = 1
        elif card_type == '临时卡':
            card_type = 2
        else:
            card_type = 3
        card_no = self.max_card_no + 1
        enroll_date = str(self.enrollDateEdit.date().toPyDate())
        valid_date = str(self.validDateEdit.date().toPyDate())
        card_status = self.isValidComboBox.currentText()
        card_status = 1 if card_status == '是' else 0
        phone_number = self.phoneNumberLineEdit.text()
        cred_no = self.credNoLineEdit.text()
        car_no = self.carNoLineEdit_2.text()
        if not car_no:
            QtWidgets.QMessageBox.warning(self, '本程序', "车牌号不能为空！", QtWidgets.QMessageBox.Ok)
            return
        if not change_data:
            query = self.db.exec('select car_no from t_card_info where status >= 0')
            while(query.next()):
                if car_no==query.value(0):
                    QtWidgets.QMessageBox.warning(self, '本程序', "车牌号不能重复！", QtWidgets.QMessageBox.Ok)
                    return
        address = self.addressLineEdit.text()
        operation_id = 0
        operation_date = str(QDateTime.currentDateTime().toPyDateTime())
        supplier = self.suppliercomboBox.currentText()
        receiver = self.receivercomboBox.currentText()
        cargo = self.cargocomboBox.currentText()
        extra = self.extraDoubleSpinBox.value()
        price = self.priceDoubleSpinBox.value()
        status = 0
        ext1 = ''
        ext2 = ''
        ext3 = ''
        ext4 = ''
        if not change_data:
            logging.info('add data')
            record = self.db_model.record()
            record.setGenerated('id', False)
            record.setValue(1, user_name)
            record.setValue(2, gender)
            record.setValue(3, card_type)
            record.setValue(4, card_no)
            record.setValue(5, enroll_date)
            record.setValue(6, valid_date)
            record.setValue(7, card_status)
            record.setValue(8, phone_number)
            record.setValue(9, cred_no)
            record.setValue(10, car_no)
            record.setValue(11, address)
            record.setValue(12, operation_id)
            record.setValue(13, operation_date)
            record.setValue(14, supplier)
            record.setValue(15, receiver)
            record.setValue(16, cargo)
            record.setValue(17, extra)
            record.setValue(18, price)
            record.setValue(19, status)
            record.setValue(20, ext1)
            record.setValue(21, ext2)
            record.setValue(22, ext3)
            record.setValue(23, ext4)
            success = self.db_model.insertRecord(self.db_model.rowCount(), record)
            ret = self.db_model.submitAll()
            if ret:
                QtWidgets.QMessageBox.information(self, '本程序', "添加成功！", QtWidgets.QMessageBox.Ok)
                self.__query_data(1)
                self.cleartext()
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "添加失败！", QtWidgets.QMessageBox.Ok)
        else:
            logging.info('change data')
            record = self.db_model.record(self.row)
            record.setValue(1, user_name)
            record.setValue(2, gender)
            record.setValue(3, card_type)
            record.setValue(5, enroll_date)
            record.setValue(6, valid_date)
            record.setValue(7, card_status)
            record.setValue(8, phone_number)
            record.setValue(9, cred_no)
            record.setValue(10, car_no)
            record.setValue(11, address)
            record.setValue(12, operation_id)
            record.setValue(13, str(QDateTime.currentDateTime().toPyDateTime()))
            record.setValue(14, supplier)
            record.setValue(15, receiver)
            record.setValue(16, cargo)
            record.setValue(17, extra)
            record.setValue(18, price)
            # record.setValue(19, status)
            # record.setValue(20, ext1)
            # record.setValue(21, ext2)
            # record.setValue(22, ext3)
            # record.setValue(23, ext4)
            success = self.db_model.setRecord(self.row, record)
            ret = self.db_model.submitAll()
            if ret:
                QtWidgets.QMessageBox.information(self, '本程序', "修改成功！", QtWidgets.QMessageBox.Ok)
                self.__query_data()
                self.cleartext()
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "修改失败！", QtWidgets.QMessageBox.Ok)
        # if success:
        #     self.max_card_no += 1

    def cleartext(self):
        self.carNoLineEdit_2.clear()
        self.userNameLineEdit_2.clear()
        self.genderComboBox.setCurrentIndex(0)
        self.suppliercomboBox.setCurrentText("")
        self.receivercomboBox.setCurrentText("")
        self.phoneNumberLineEdit.clear()
        self.credNoLineEdit.clear()
        self.cardTypeComboBox.setCurrentIndex(2)
        self.isValidComboBox.setCurrentIndex(0)
        self.addressLineEdit.clear()
        self.cargocomboBox.setCurrentText("")
        self.extraDoubleSpinBox.setValue(0.00)

    def __delete_data(self):
        """
        删除数据
        :return:
        """
        current_row = self.tableView.currentIndex().row()
        if current_row != -1:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '本程序',
                                                   "是否要删除记录姓名 = %s ？" % self.db_model.index(current_row, 1).data(),
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                logging.info("delete user_name = %s" % self.db_model.index(current_row, 0).data())
                record = self.db_model.record(current_row)
                record.setValue('status', -1)
                self.db_model.setRecord(current_row, record)
                self.db_model.submitAll()
                self.__query_data()
                self.cleartext()
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的记录！", QtWidgets.QMessageBox.Ok)

    def closeEvent(self, a0):
        """
        关闭事件
        :param a0:
        :return:
        """
        super(CardForm, self).closeEvent(a0)
        self.tableView.setModel(None)


class CardInfoDelegate(QtWidgets.QItemDelegate):
    """
    性别列
    """
    def __init__(self, parent):
        super(CardInfoDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        """
        渲染单元格
        :param painter:
        :param option:
        :param index:
        :return:
        """
        if index.column() == 2:
            text = "男" if self.parent().model().data(index) == 1 else "女"
        elif index.column() == 3:
            text = "月卡"
            if self.parent().model().data(index) == 2:
                text = "临时卡"
            elif self.parent().model().data(index) == 3:
                text = "免费卡"
        elif index.column() == 7:
            text = "有" if self.parent().model().data(index) == 1 else "无"
        elif index.column() == 19:
            text = "已发行" if self.parent().model().data(index) == 1 else "未发行"
        if index.column() in (2, 3, 7, 19):
            option.displayAlignment = Qt.AlignRight | Qt.AlignVCenter
            self.drawDisplay(painter, option, option.rect, str(text))
            self.drawFocus(painter, option, option.rect)
        else:
            super(CardInfoDelegate, self).paint(painter, option, index)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = CardForm()
    myshow.show()
    sys.exit(app.exec_())
    # print(QDateTime.currentDateTime().toPyDateTime())