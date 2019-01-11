#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import datetime

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from ui.balance import Ui_mainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage
from utils import com_interface_utils
from utils.sqllite_util import EasySqlite
from utils import normal_utils
from conf.constant import NormalParam
from setup_form import SetupForm
from params_form import ParamsForm
from system_params_form import SystemParamsForm
from car_form import CarManageForm
from car_no_dialog_form import CarNoDialogForm
from Supply_form import SupplyForm
from receiver_form import receiverForm
from cargo_form import cargoForm
from poll_form import pollmainForm
from permission_form import PermissionSetupForm
from functools import partial
import subprocess
import sys
import serial
import time
import logging
import os
import cv2


class MainForm(QtWidgets.QMainWindow, Ui_mainWindow):
    u"""
    mainform
    """
    def __init__(self, user_id=''):
        super(MainForm, self).__init__()
        self.user_id = user_id if user_id else 'admin'
        self.setupUi(self)
        self.weightLcdNumber.display(0)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.init_data()
        self.dialog = CarNoDialogForm()
        self.dialog.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.pushButton.clicked.connect(self.show_dialog)
        self.dialog.my_signal.connect(self.CarComboBox.setCurrentText)
        self.params_form = ParamsForm(self)
        self.actionParameterSetup.triggered.connect(self.params_form.show)
        self.setup_form = SetupForm()
        self.actionBalanceFormSetup.triggered.connect(self.setup_form.show)
        self.system_params_form = SystemParamsForm()
        self.actionSystemParameterSetup.triggered.connect(self.system_params_form.show)
        self.car_form = CarManageForm()
        self.actionCarInfo.triggered.connect(self.car_form.show)
        self.Supply_form = SupplyForm(self)
        self.actionSupplier.triggered.connect(self.Supply_form.show)
        self.receiver_form = receiverForm(self)
        self.actionReceiving.triggered.connect(self.receiver_form.show)
        self.cargo_form = cargoForm(self)
        self.actionGoodsName.triggered.connect(self.cargo_form.show)
        self.poll_form = pollmainForm()
        self.actionBalanceQuery.triggered.connect(self.poll_form.show)
        self.permission_form = PermissionSetupForm()
        self.actionUserPermission.triggered.connect(self.permission_form.show)
        self.pickBalanceButton.clicked.connect(self.choose_weight)
        self.savePushButton.clicked.connect(partial(self.save_data, True))
        self.clearPushButton.clicked.connect(self.clear_data)
        self.saveLeatherPushButton.clicked.connect(self.save_leather)
        self.printPushButton.clicked.connect(self.print_data)
        self.CarComboBox.editTextChanged.connect(self.update_weight)
        self.rmf_path = os.path.join(os.getcwd(), r'rmf\rmf')
        self.report_file = os.path.join(os.getcwd(), r'rmf\RMReport.exe')
        self.weightLcdNumber.display(120)
        self.balance_status = 0
        self.ischange = 0
        self.isexist = 0
        self.thread_dict = dict()
        self.active_video()

    def getUserName(self):
        sql = "select user_name from t_user where user_id = '%s'" % self.user_id
        ret = self.db.query(sql)
        return ret[0].get('user_name')

    def show(self):
        """
        显示界面
        :return:
        """
        super().show()
        self.set_table_view()
        self.update_combobox()
        self.__init_permission()

    def show_supplier(self):
        supply_query_sql = 'select supplier_name from t_supplier'
        supply_list = self.db.query(supply_query_sql)
        supply_row_no = len(supply_list)
        for row in range(supply_row_no):
            values = list(supply_list[row].values())[0]
            self.supplierComboBox.addItem(values)
        self.supplierComboBox.clearEditText()

    def __init_permission(self):
        """
        初始化权限
        :return:
        """
        perminsion_dict = {
            'system_params_form': self.actionSystemParameterSetup,
            'setup_form': self.actionBalanceFormSetup,
            'permission_form': self.actionUserPermission,
            'params_form': self.actionParameterSetup,
            'car_form': self.actionCarInfo,
            'Supply_form': self.actionSupplier,
            'receiver_form': self.actionReceiving,
            'cargo_form': self.actionGoodsName,
            'poll_form': self.actionBalanceQuery,
        }
        for k, v in perminsion_dict.items():
            v.setEnabled(False)
        user_permission = normal_utils.get_user_permission(self.user_id)
        for item in user_permission:
            if item in perminsion_dict.keys():
                perminsion_dict.get(item).setEnabled(True)

    def active_video(self):
        """
        开启摄像头
        :return:
        """
        sql = """select user_id, password, ip_addr, camera_no from t_camera where is_active = 1"""
        ret = self.db.query(sql)
        if ret:
            for k in self.thread_dict.keys():
                self.thread_dict[k].stop()
            self.video_label_1.clear()
            self.video_label_2.clear()
            self.video_label_3.clear()
            self.video_label_4.clear()
            for item in ret:
                url = "rtsp://%s:%s@%s" % (item['user_id'], item['password'], item['ip_addr'])
                camera_no = item['camera_no']
                self.thread_dict[str(camera_no)] = VideoThread(camera_no, url)
                # 注册信号处理函数
                self.thread_dict[str(camera_no)].breakSignal.connect(self.show_camera)
                # 启动线程
                # self.shotPushButton.clicked.connect(self.shot_change)
                self.thread_dict[str(camera_no)].shortImage.connect(self.shot_info)
                self.thread_dict[str(camera_no)].start()

    def shot_info(self, flag):
        """
        接收截图信息
        :param flag:
        :return:
        """
        # if flag:
        #     QtWidgets.QMessageBox.information(self, '本程序', "保存图片成功！")
        return flag

    def shot_change(self,path):
        """
        截图
        :return:
        """

        sql = """select  camera_no from t_camera where is_active = 1"""
        ret = self.db.query(sql)
        for item in ret:
            camera_no = item['camera_no']
            if camera_no == 1:
                path1 = path+'01.png'
                self.thread_dict['1'].shot_image(path1)
                continue
            if camera_no == 2:
                path2 = path + '02.png'
                self.thread_dict['2'].shot_image(path2)
                continue
            if camera_no == 3:
                path3 = path + '03.png'
                self.thread_dict['3'].shot_image(path3)
                continue
            if camera_no == 4:
                path4 = path + '04.png'
                self.thread_dict['4'].shot_image(path4)
                continue

    def show_camera(self, camera_no, qpixmap):
        """
        读取摄像头
        :param qpixmap:
        :return:
        """
        if camera_no == '1':
            self.video_label_1.setPixmap(qpixmap)
        elif camera_no == '2':
            self.video_label_2.setPixmap(qpixmap)
        elif camera_no == '3':
            self.video_label_3.setPixmap(qpixmap)
        elif camera_no == '4':
            self.video_label_4.setPixmap(qpixmap)

    def init_data(self):
        u"""
        初始化数据和定时器
        :return:
        """
        self._is_open = False
        self._com_worker = COMThread()
        self._com_worker.start()
        self._weight = {}
        self._timer = QTimer(self)  # 新建一个定时器
        # 关联timeout信号和showTime函数，每当定时器过了指定时间间隔，就会调用showTime函数
        self._com_worker.trigger.connect(self.show_lcd)
        self._timer.timeout.connect(self.check_weight_state)
        self._timer.start(NormalParam.COM_READ_DURATION)  # 设置定时间隔为1000ms即1s，并启动定时器

    def show_lcd(self, is_open, weight):
        u"""
        显示数据
        :return:
        """
        if is_open:
            self._is_open = True
            self.weightLcdNumber.display(weight)
            now = int(time.time() * 1000)
            self._weight[now] = weight
            del_keys = [k for k in self._weight.keys() if now - k > (NormalParam.STABLES_DURATION + 1) * 1000]
            [self._weight.pop(k) for k in del_keys]

    def check_weight_state(self):
        u"""
        获取停止读取标志
        :return:
        """
        if self._is_open:
            now = int(time.time() * 1000)
            first = min(self._weight.keys())
            if first + NormalParam.STABLES_DURATION * 1000 < now:
                weights = [v for k, v in self._weight.items() if now - k <= NormalParam.STABLES_DURATION * 1000]
                if normal_utils.stdev(weights) <= NormalParam.STABLES_ERROR:
                    self.stateLabel.setText(u'稳定')
                    self.stateLabel.setStyleSheet('color:green')
                    self.pickBalanceButton.setEnabled(True)
                else:
                    self.stateLabel.setText(u'读取中……')
                    self.stateLabel.setStyleSheet('color:black')
                    self.pickBalanceButton.setEnabled(False)
            else:
                self.stateLabel.setText(u'读取中……')
                self.stateLabel.setStyleSheet('color:black')
                self.pickBalanceButton.setEnabled(False)
        else:
            self.stateLabel.setText(u'称重仪表未连接！')
            self.stateLabel.setStyleSheet('color:red')
            # self.pickBalanceButton.setEnabled(False)

    def closeEvent(self, event):
        """
        点击X号退出事件
        :param event:
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            # sys.exit(app.exec_())
            self.close()
        else:
            event.ignore()

    def update_combobox(self):
        """
        下拉列表数据
        :return:
        """
        cargo_query_sql = 'select name from t_cargo'
        cargo_list = self.db.query(cargo_query_sql)
        cargo_row_no = len(cargo_list)
        self.goodsComboBox.clear()
        for row in range(cargo_row_no):
            values = list(cargo_list[row].values())[0]
            self.goodsComboBox.addItem(values)
        self.goodsComboBox.clearEditText()
        supply_query_sql = 'select supplier_name from t_supplier'
        supply_list = self.db.query(supply_query_sql)
        supply_row_no = len(supply_list)
        self.supplierComboBox.clear()
        for row in range(supply_row_no):
            values = list(supply_list[row].values())[0]
            self.supplierComboBox.addItem(values)
        self.supplierComboBox.clearEditText()
        receiver_query_sql = 'select receiver_name from t_receiver'
        receiver_list = self.db.query(receiver_query_sql)
        receiver_row_no = len(receiver_list)
        self.receiverComboBox.clear()
        for row in range(receiver_row_no):
            values = list(receiver_list[row].values())[0]
            self.receiverComboBox.addItem(values)
        self.receiverComboBox.clearEditText()
        car_query_sql = 'select car_no from t_car order by add_time desc'
        car_list = self.db.query(car_query_sql)
        car_row_no = len(car_list)
        for row in range(car_row_no):
            values = list(car_list[row].values())[0]
            self.CarComboBox.addItem(values)
        self.CarComboBox.clearEditText()
        self.operatorComboBox.setCurrentText(self.getUserName())

    def set_table_view(self):
        """
        :return:
        """
        header = ['单号', '车牌号', '毛重', '皮重', '净重', '货物名', '供货单位', '收货单位', '包装物重', '另扣',
                  '杂志', '水分', '单价', '金额', '含油', '结算重量', '规格', '驾驶员', '计划单号', '运货单位', '称重时间1',
                  '称重日期', '称重时间2', '操作员', '是否完成', '备注', '备用1', '备用2', '备用3', '备用4']
        query_sql = 'select * from t_balance'
        data_list = self.db.query(query_sql)
        row_no, col_no = len(data_list), len(header)
        model = QStandardItemModel(row_no, col_no)
        model.setHorizontalHeaderLabels(header)
        for row in range(row_no):
            values = list(data_list[row].values())
            for col in range(1, col_no):
                item = QStandardItem(str(values[col]))
                model.setItem(row, col-1, item)
        self.tableView.setModel(model)
        # self.tableView.doubleClicked.connect(lambda x: self.display_data(data_list[int(x.row())]))
        self.tableView.doubleClicked.connect(self.__display_data)

    def __display_data(self, index):
        if index:
            self.balanceNoBlael.setText(str(self.tableView.model().index(index.row(), 0).data()))
            self.totalWeightLcdNumber.display(self.tableView.model().index(index.row(), 2).data())
            self.leatherWeightLcdNumber.display(self.tableView.model().index(index.row(), 3).data())
            self.actualWeightLcdNumber.display(self.tableView.model().index(index.row(), 4).data())

            self.priceSpinBox.setValue(float(self.tableView.model().index(index.row(), 12).data()))
            self.amountSpinBox.setValue(float(self.tableView.model().index(index.row(), 13).data()))

            self.CarComboBox.setCurrentText(self.tableView.model().index(index.row(), 1).data())
            self.supplierComboBox.setCurrentText(self.tableView.model().index(index.row(), 6).data())
            self.receiverComboBox.setCurrentText(self.tableView.model().index(index.row(), 7).data())
            self.goodsComboBox.setCurrentText(self.tableView.model().index(index.row(), 5).data())
            self.operatorComboBox.setCurrentText(str(self.tableView.model().index(index.row(), 23).data()))
        else:
            self.totalWeightLcdNumber.display(self.weightLcdNumber.value())

    def display_data(self, data):
        if data:
            self.balanceNoBlael.setText(str(data.get('balance_id', '0')))
            self.totalWeightLcdNumber.display(data.get('total_weight', 0))
            self.leatherWeightLcdNumber.display(data.get('leather_weight', 0))
            self.actualWeightLcdNumber.display(data.get('actual_weight', 0))
            self.priceSpinBox.setValue(data.get('price', 0.))
            self.amountSpinBox.setValue(data.get('amount', 0.))
            self.CarComboBox.setCurrentText(data.get('car_no', ''))
            self.supplierComboBox.setCurrentText(data.get('supplier', ''))
            self.receiverComboBox.setCurrentText(data.get('receiver', ''))
            self.goodsComboBox.setCurrentText(data.get('goods_name', ''))
            self.operatorComboBox.setCurrentText(data.get('operator', ''))
            self.balance_status = data.get('status', '')
        else:
            self.totalWeightLcdNumber.display(self.weightLcdNumber.value())

    def update_weight(self, car_no):
        """
        更行重量
        :return:
        """
        if len(car_no) != 7:
            self.leatherWeightLcdNumber.display(0)
            return
        if self.balanceNoBlael.text():
            return
        self.balanceNoBlael.setText('')
        self.totalWeightLcdNumber.display(0)
        self.leatherWeightLcdNumber.display(0)
        self.actualWeightLcdNumber.display(0)
        self.priceSpinBox.setValue(0)
        self.amountSpinBox.setValue(0)
        self.supplierComboBox.setCurrentText('')
        self.receiverComboBox.setCurrentText('')
        self.goodsComboBox.setCurrentText('')
        self.operatorComboBox.setCurrentText('')
        car_query = """select car_no, leather_weight from t_car where car_no='%s'""" % car_no
        ret = self.db.query(car_query)
        if ret:
            leather_weight = ret[0].get("leather_weight", 0)
            self.leatherWeightLcdNumber.display(leather_weight)

    def save_data(self, warning=True):
        """
        保存数据
        :return:
        """
        if not self.balanceNoBlael.text():
            QtWidgets.QMessageBox.warning(self, '本程序', "单号不能为空！", QtWidgets.QMessageBox.Ok)
            return
        balance_id = int(self.balanceNoBlael.text())
        total_weight = float(self.totalWeightLcdNumber.value())
        leather_weight = float(self.leatherWeightLcdNumber.value())
        actual_weight = float(self.actualWeightLcdNumber.value())
        extra_value = float(self.extraWeightSpinBox.value())
        price = float(self.priceSpinBox.value())
        amount = float(self.amountSpinBox.value())
        car_no = self.CarComboBox.currentText()
        if not car_no:
            QtWidgets.QMessageBox.warning(self, '本程序', "车号不能为空！", QtWidgets.QMessageBox.Ok)
        supplier = self.supplierComboBox.currentText()
        receiver = self.receiverComboBox.currentText()
        goods_name = self.goodsComboBox.currentText()
        operator = self.getUserName()
        print(operator)
        # operator = u'系统管理员'
        today_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.abspath('.') + '\shot'
        today_month = datetime.datetime.now().strftime("%Y%m")
        path = path + '\\' + str(today_month)
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)
        path = path + '\\' + str(today_date)
        self.shot_change(path)
        data = ''
        balance_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # balance_time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.balance_status:
            if self.ischange:
                insert_sql = '''update t_balance set total_weight= ?, leather_weight= ?, actual_weight= ?,
                                     extra= ?, price = ?, amount= ?, car_no = ?, supplier = ?, receiver = ?, 
                                     goods_name = ?, balance_time1=?,operator = ?, status= ?,ext2=? 
                                     where balance_id = ?'''
                data = (total_weight, leather_weight, actual_weight, extra_value, price, amount, car_no,
                        supplier, receiver, goods_name, balance_time, operator, self.balance_status, path, int(balance_id))
            else:
                insert_sql = '''update t_balance set total_weight= ?, leather_weight= ?, actual_weight= ?,
                                     extra= ?, price = ?, amount= ?, car_no = ?, supplier = ?, receiver = ?, 
                                     goods_name = ?, balance_time2 = ?,operator = ?, status= ?,ext2= ? 
                                     where balance_id = ? '''
                data = (total_weight, leather_weight, actual_weight, extra_value, price, amount, car_no,
                        supplier, receiver, goods_name, balance_time, operator, self.balance_status, path, int(balance_id))
        else:
            insert_sql = '''replace into t_balance(balance_id, total_weight, leather_weight, actual_weight,
                                extra, price, amount, car_no, supplier, receiver, goods_name,balance_time1,
                                balance_time2, operator, status,ext1) 
                                values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            data = (balance_id, total_weight, leather_weight, actual_weight, extra_value, price, amount, car_no,
                supplier, receiver, goods_name, balance_time, balance_time, operator, self.balance_status, path)
        ret = self.db.update(insert_sql, args=data)
        if warning:
            if ret:
                QtWidgets.QMessageBox.warning(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)
        if ret:
            self.set_table_view()
            self.clear_data()

    def clear_data(self):
        """
        清空数据
        :return:
        """
        self.balanceNoBlael.setText('')
        self.totalWeightLcdNumber.display(0)
        self.leatherWeightLcdNumber.display(0)
        self.actualWeightLcdNumber.display(0)
        self.priceSpinBox.setValue(0)
        self.amountSpinBox.setValue(0)
        self.CarComboBox.setCurrentText('')
        self.supplierComboBox.setCurrentText('')
        self.receiverComboBox.setCurrentText('')
        self.goodsComboBox.setCurrentText('')
        self.operatorComboBox.setCurrentText('')
        self.balance_status = 0

    def save_leather(self):
        """
        去皮
        :return:
        """

        car_no = self.CarComboBox.currentText()
        if not car_no:
            QtWidgets.QMessageBox.warning(self, '本程序', "车号不能为空！", QtWidgets.QMessageBox.Ok)
            return
        car_query = """select car_no, leather_weight from t_car where car_no = '%s'""" % car_no
        ret = self.db.query(car_query)
        if ret:
            QtWidgets.QMessageBox.warning(self, '本程序', "车号：%s 已有存皮！" % car_no, QtWidgets.QMessageBox.Ok)
            return
        total_weight = self.totalWeightLcdNumber.value()
        if float(total_weight) <= 0.0:
            QtWidgets.QMessageBox.warning(self, '本程序', "皮重必须是正数！", QtWidgets.QMessageBox.Ok)
            return
        leather_weight = self.leatherWeightLcdNumber.value()
        if float(leather_weight) > 0.0:
            QtWidgets.QMessageBox.warning(self, '本程序', "皮重将会被覆盖！", QtWidgets.QMessageBox.Ok)
            return

        car_update = """insert into t_car(car_no, leather_weight) values(?,?)"""
        logging.info((car_no, float(total_weight)))
        self.db.update(car_update, args=(car_no, total_weight))

    def print_data(self):
        """
        打印
        :return:
        """
        if not self.balanceNoBlael.text():
            if self.stateLabel.text() != u'稳定':
                QtWidgets.QMessageBox.warning(self, '本程序', "状态未稳定！", QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.warning(self, '本程序', "请选择要打印的磅单！", QtWidgets.QMessageBox.Ok)
            return
        balance_id = int(self.balanceNoBlael.text())
        self.save_data(warning=False)
        sql = 'select default_rmf from t_rmf'
        ret = self.db.query(sql)
        default_rmf = ret[0].get('default_rmf', u'过称单(标准式).rmf')
        cmd_str = self.report_file + u' -d "balance.db" -s "db1:select t_balance.* from t_balance where  balance_id=\'%s\'" -r "%s" -a 1' % (balance_id, default_rmf)
        # cmd_str = self.report_file + u' -d "balance.db" -s "db1:select t_balance.*,t_supplier.* from t_balance,t_supplier where  t_balance.supplier = t_supplier.supplier_name and balance_id=\'%s\'" -r "%s" -a 1' % (balance_id, default_rmf)
        logging.debug(cmd_str)
        self.p = subprocess.Popen(cmd_str)

    def choose_weight(self):
        """
        取重量
        :return:
        """
        current_weight = self.weightLcdNumber.value()
        car_no = self.CarComboBox.currentText()
        if not car_no:
            QtWidgets.QMessageBox.warning(self, '本程序', "请先设置车号！", QtWidgets.QMessageBox.Ok)
            return
        balance_query = """select * from t_balance where car_no = '%s' and status=0""" % car_no
        print(balance_query)
        ret = self.db.query(balance_query)
        if ret:
            QtWidgets.QMessageBox.warning(self, '本程序', "此车 %s 有未完成的磅单，正在进行完成操作!" % car_no, QtWidgets.QMessageBox.Ok)
            data_db = ret[0]
            self.display_data(data_db)
            total_weight_db = data_db.get('total_weight', 0)
            actual_weight = abs(current_weight - total_weight_db)
            leather_weight = current_weight if total_weight_db > current_weight else total_weight_db
            if current_weight - total_weight_db > 0:
                self.ischange = 1
            total_weight = leather_weight + actual_weight
            self.totalWeightLcdNumber.display(total_weight)
            self.leatherWeightLcdNumber.display(leather_weight)
            self.actualWeightLcdNumber.display(actual_weight)
            self.balance_status = 1
        else:
            balance_id = normal_utils.generate_balance_id()
            self.balanceNoBlael.setText(balance_id)
            car_query = """select car_no, leather_weight from t_car where car_no='%s'""" % car_no
            ret = self.db.query(car_query)
            if not ret:
                # 没有存皮的情况
                QtWidgets.QMessageBox.warning(self, '本程序', "该车 %s 没有存皮，将生成未完成磅单！" % car_no, QtWidgets.QMessageBox.Ok)
                self.balance_status = 0
            else:
                # 有存皮
                QtWidgets.QMessageBox.warning(self, '本程序', "该车 %s 已有存皮，将自动生成磅单！" % car_no, QtWidgets.QMessageBox.Ok)
                leather_weight_db = ret[0].get('leather_weight', 0)
                actual_weight = current_weight - leather_weight_db
                self.leatherWeightLcdNumber.display(leather_weight_db)
                self.actualWeightLcdNumber.display(actual_weight)
                self.balance_status = 1
            self.totalWeightLcdNumber.display(self.weightLcdNumber.value())

    def show_dialog(self):
        """
        显示车牌号键盘
        :return:
        """
        if self.dialog.isVisible():
            self.dialog.setVisible(False)
            return
        self.dialog.show()

    def moveEvent(self, a0):
        """
        移动窗口事件
        :param a0:
        :return:
        """
        super().moveEvent(a0)
        point = a0.pos()
        point1 = self.pushButton.pos()
        if point1.x() == 0:
            point.setX(point.x() + 300)
            point.setY(point.y() + 260)
        elif point.x() == 0:
            point.setX(point1.x() - 400)
            point.setY(point.y() + point1.y() + 190)
        else:
            point.setX(point.x() + point1.x() - 300)
            point.setY(point.y() + point1.y() + 180)
        self.dialog.move(point)

    def resizeEvent(self, a0):
        """
        重置窗口大小事件
        :param a0:
        :return:
        """
        super().resizeEvent(a0)
        if self.dialog.isVisible():
            self.dialog.setVisible(False)
            return
        width = self.video_label_1.size().width()
        height = self.video_label_1.size().height()
        # self.thread_dict[].set_size(width, height)


class COMThread(QThread):
    """
    串口读取线程
    """
    trigger = pyqtSignal(int, float)

    def __init__(self):
        self._is_conn = False
        super().__init__()
        self.db = EasySqlite(r'rmf/db/balance.db')

    def init_serial(self):
        u"""
        :return:
        """
        query_sql_com1 = 'select * from t_com where is_default = 1'
        ret = self.db.query(query_sql_com1)[0]
        COM_INTERFACE = ret['com_no']
        COM_BAUD_RATE = ret['baud_rate']
        self._serial = serial.Serial(COM_INTERFACE, COM_BAUD_RATE, timeout=0.5)
        if self._serial.isOpen():
            logging.info("open success")
        else:
            logging.error("open failed")
            raise Exception(u'%s 串口打开失败！' % 'COM5')

    def run(self):
        """
        读取串口信息
        :return:
        """
        DEBUG = False
        query_sql_com1 = 'select * from t_com where is_default = 1'
        ret = self.db.query(query_sql_com1)[0]
        COM_INTERFACE = ret['com_no']

        if DEBUG:
            while True:
                weight = 100
                self.trigger.emit(1, weight)
                time.sleep(NormalParam.COM_READ_DURATION / 2 / 1000)
        else:
            while not self._is_conn:
                try:
                    self.init_serial()
                    self._is_conn = True
                except serial.serialutil.SerialException as e:
                    logging.error(e)
                    logging.info(u'%s 接口未连接！' % COM_INTERFACE)
                    time.sleep(NormalParam.COM_CHECK_CONN_DURATION)
                except Exception as e:
                    logging.error(e)
                    time.sleep(NormalParam.COM_OPEN_DURATION)
            while True:
                is_open = 1
                weight = com_interface_utils.read_com_interface(self._serial)
                self.trigger.emit(is_open, weight)
                time.sleep(NormalParam.COM_READ_DURATION / 2 / 1000)


class VideoThread(QThread):
    """
    读取摄像头
    """
    # 定义信号
    breakSignal = pyqtSignal(str, QPixmap)
    # 定义参数为str类型
    shortImage = pyqtSignal(str)

    def __init__(self, camera_no, url):
        super().__init__()
        self.stoped = False
        self.camera_no = camera_no
        self.url = url
        self.video_width = 360
        self.video_height = 270
        self.mutex = QMutex()
        self.shot_flag = False

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped= False
        cap = cv2.VideoCapture(self.url)
        if cap.isOpened():
            logging.info('camera open success.')
        else:
            return
        while cap.isOpened():
            if self.stoped:
                return
            ret, frame = cap.read()
            frame_mini = cv2.resize(frame, (self.video_width, self.video_height))
            height, width, bytesPerComponent = frame_mini.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame_mini)
            image = QImage(frame_mini.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.breakSignal.emit(str(self.camera_no), QPixmap.fromImage(image))
            if self.shot_flag:
                logging.info('shot')
                # todo 截图地址
                cv2.imwrite(self.path, frame)
                self.shot_flag = False
                self.shortImage.emit(self.path)
            # 40毫秒发送一次信号
            time.sleep(0.04)

    def set_size(self, width, height):
        """
        设置视频大小
        :param width:
        :param height:
        :return:
        """
        self.video_width = width
        self.video_height = height

    def shot_image(self,path):
        """
        截图操作
        :return:
        """
        self.shot_flag = True
        self.path =path

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped= True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())