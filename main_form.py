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
from ui.about_dialog import Ui_AboutDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, QTimer, pyqtSignal, QMutexLocker, QMutex, Qt
from PyQt5.QtGui import QPixmap, QImage
from utils import com_interface_utils
from utils.sqllite_util import EasySqlite
from utils import normal_utils
from utils.constant import NormalParam
from setup_form import SetupForm
from params_form import ParamsForm
from system_params_form import SystemParamsForm
from car_form import CarManageForm
from car_no_dialog_form import CarNoDialogForm
from supply_form import SupplyForm
from receiver_form import receiverForm
from cargo_form import cargoForm
from poll_form import pollmainForm
from permission_form import PermissionSetupForm
from card_form import CardForm
from com_setup_form import ComSetupForm
from functools import partial
import subprocess
import sys
import serial
import time
import logging
import os
import cv2
from datetime import timedelta
from datetime import datetime
import comtypes.client
import comtypes


class MainForm(QtWidgets.QMainWindow, Ui_mainWindow):
    u"""
    mainform
    """
    def __init__(self, parent=''):
        super(MainForm, self).__init__()
        self.user_id = parent.user_id if parent else 'admin'
        self.user_name = parent.user_name if parent else '系统管理员'
        self.company = parent.company if parent else '泰安市泰山区柒点信息科技有限公司'
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle(u'飞然称重系统--%s--当前用户：%s' % (self.company, self.user_name))
        self.db = EasySqlite(r'rmf/db/balance.db')
        self._com_worker = None
        self._barrier_worker1 = None
        self._barrier_worker2 = None
        self.speaker = None
        self.card_no = -1
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
        self.actionChangeUser.triggered.connect(self.switch_user)
        self.actionExit.triggered.connect(self.close)
        self.car_form = CarManageForm(self)
        self.actionCarInfo.triggered.connect(self.car_form.show)
        self.Supply_form = SupplyForm(self)
        self.actionSupplier.triggered.connect(self.Supply_form.show)
        self.receiver_form = receiverForm(self)
        self.actionReceiving.triggered.connect(self.receiver_form.show)
        self.cargo_form = cargoForm(self)
        self.actionGoodsName.triggered.connect(self.cargo_form.show)
        self.poll_form = pollmainForm(self.user_id)
        self.actionBalanceQuery.triggered.connect(self.poll_form.show)
        self.permission_form = PermissionSetupForm(self)
        self.permission_form.permission_changed.connect(self.__init_permission)
        self.actionUserPermission.triggered.connect(self.permission_form.show)
        self.com_setup_form = ComSetupForm(self)
        self.actionComSetup.triggered.connect(self.com_setup_form.show)
        self.card_form = CardForm()
        self.cardInfoAction.triggered.connect(self.card_form.show)
        self.pickBalanceButton.clicked.connect(self.choose_weight)
        self.actionHelp.triggered.connect(self.open_help)
        self.about_dialog = AboutDialog()
        self.actionAbout.triggered.connect(self.about_dialog.show)
        self.extraWeightSpinBox.setValue(0)
        self.settlementLcdNumber.display(0)
        self.savePushButton.clicked.connect(partial(self.save_data, True))
        self.clearPushButton.clicked.connect(self.clear_data)
        self.saveLeatherPushButton.clicked.connect(self.save_leather)
        self.printPushButton.clicked.connect(self.print_data)
        self.CarComboBox.editTextChanged.connect(self.update_weight)
        self.extraWeightSpinBox.valueChanged.connect(self.calculate)
        self.barrier1PushButton.clicked.connect(partial(self.__set_barrier1, -1))
        self.barrier2PushButton.clicked.connect(partial(self.__set_barrier2, -1))
        self.rmf_path = os.path.join(os.getcwd(), r'rmf\rmf')
        self.report_file = os.path.join(os.getcwd(), r'rmf\RMReport.exe')
        self.weightLcdNumber.display(0)
        self.balance_status = 0
        self.ischange = 0
        self.isexist = 0
        # 1：新建未完成磅单； 2：修改已完成订单；0：其他状态
        self.balance_opt_status = 0
        # 是否需要退出确认
        self.close_confirm = True
        # 无人值守是否正在称重，如果为 1，车在榜上并已稳定，如果为 0，榜上没有东西
        self.weight_working = 0
        # 判断进出口, 1 为gate1进，2为gate2进
        self.gate_type = 1
        # 监控摄像头线程
        self.thread_dict = dict()
        # 跟车判断
        self.carfollow = 0

    def show(self):
        """
        显示界面
        :return:
        """
        super().show()
        self.init_data()
        self.set_table_view()
        self.update_combobox()
        self.__init_permission()
        self.setStatusTip("启动完毕！")

    def open_help(self):
        """
        显示帮助手册
        :return:
        """
        import webbrowser
        webbrowser.open(u"conf/helpme.pdf")

    def show_supplier(self):
        supply_query_sql = 'select supplier_name from t_supplier'
        supply_list = self.db.query(supply_query_sql)
        supply_row_no = len(supply_list)
        for row in range(supply_row_no):
            values = list(supply_list[row].values())[0]
            self.supplierComboBox.addItem(values)
        self.supplierComboBox.clearEditText()

    def __set_barrier(self, gate, operate):
        """
        设置道闸
        :param gate:
        :param operate:
        :return:
        """
        if gate == 1:
            return self.__set_barrier1(operate)
        elif gate == 2:
            return self.__set_barrier2(operate)

    def __set_barrier1(self, operate=-1):
        """
        设置道闸1
        :return:
        """
        res = False
        if operate == -1:
            state = normal_utils.get_barrier_state(1)
            if state == 0:
                if normal_utils.open_barrier_gate(1):
                    res = True
            elif state == 1:
                if normal_utils.close_barrier_gate(1):
                    res = True
        elif operate == 0:
            if normal_utils.close_barrier_gate(1):
                res = True
        elif operate == 1:
            if normal_utils.open_barrier_gate(1):
                res = True
        return res

    def __set_barrier2(self, operate=-1):
        """
        设置道闸2
        :return:
        """
        res = False
        if operate == -1:
            state = normal_utils.get_barrier_state(2)
            if state == 0:
                if normal_utils.open_barrier_gate(2):
                    res = True
            elif state == 1:
                if normal_utils.close_barrier_gate(2):
                    res = True
        elif operate == 0:
            if normal_utils.close_barrier_gate(2):
                res = True
        elif operate == 1:
            if normal_utils.open_barrier_gate(2):
                res = True
        return res

    def calculate(self):
        if self.balanceNoBlael.text() == "":
            QtWidgets.QMessageBox.warning(self, '本程序', "请先取重量！", QtWidgets.QMessageBox.Ok)
            self.extraWeightSpinBox.clear()
            self.settlementLcdNumber.display(0)
            return
        if self.extraWeightSpinBox.value() != 0:
            sell = float(self.actualWeightLcdNumber.value())-float(self.extraWeightSpinBox.value())
            self.settlementLcdNumber.display(sell)
        else:
            self.settlementLcdNumber.display(0)

    def switch_user(self):
        """
        切换用户
        :return:
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "将要切换用户？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.close_confirm = False
            self.close()
            self.parent.show()

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
            'com_setup_form': self.actionComSetup,
            'card_form': self.cardInfoAction,
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
        for k in self.thread_dict.keys():
            self.thread_dict[k].stop()
        time.sleep(0.05)
        if ret:
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

    def shot_change(self, path):
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
        if self._barrier_worker1:
            self._barrier_worker1.stop()
            while not self._barrier_worker1.isStoped():
                time.sleep(0.02)
            self._barrier_worker1 = None
        if self._barrier_worker2:
            self._barrier_worker2.stop()
            while not self._barrier_worker2.isStoped():
                time.sleep(0.02)
            self._barrier_worker2 = None
        query = """select read_com_switch1, read_com_switch2 from t_com_auto"""
        ret = self.db.query(query)
        if ret:
            if ret[0]['read_com_switch1'] == 1:
                self._read_com_switch1 = True
                self._barrier_worker1 = CardThread(1)
                self._barrier_worker1.start()
                self._barrier_worker1.trigger.connect(self.check_card_no)
            else:
                self._read_com_switch1 = False
            if ret[0]['read_com_switch2'] == 1:
                self._read_com_switch2 = True
                self._barrier_worker2 = CardThread(2)
                self._barrier_worker2.start()
                self._barrier_worker2.trigger.connect(self.check_card_no)
            else:
                self._read_com_switch2 = False
        self._is_open = False
        if self._com_worker:
            self._com_worker.stop()
            while not self._com_worker.isStoped():
                time.sleep(0.02)
        self._com_worker = COMThread()
        self._com_worker.start()
        self._weight = {}
        self._timer = QTimer(self)
        # 检测是否稳定时间间隔 ms
        self._com_worker.trigger.connect(self.show_lcd)
        self._timer.timeout.connect(self.check_weight_state)
        self._timer.start(NormalParam.CHECK_WEIGHT_STATE)
        self.active_video()
        # 语音播报线程
        if self.speaker:
            self.speaker.stop()
        self.speaker = SpeakerThread()
        self.speaker.start()

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
        else:
            self._is_open = False
            self.weightLcdNumber.display(weight)

    def check_card_no(self, args):
        u"""
        判断卡号
        :return:
        """
        read_no = args[0]
        is_open = args[1]
        card_no = args[2]
        # print("check_card_no")
        # print("read_no = %s and card_no = %s" % (read_no, card_no))
        if card_no == str(-1):
            return
        if self.weightLcdNumber.value() > NormalParam.BALANCE_LOW:
            self.setStatusTip("正在称重请稍候!")
            return
        if self.weight_working == 1 and card_no == self.card_no:
            return
        self.gate_type = read_no
        query = """select car_no from t_card_info where card_no = '%s' and card_status = 1 and status = 1""" % card_no
        ret = self.db.query(query)
        if self.carfollow==0:
            if ret:
                self.carfollow = 1
                # print("card_no = %s -- car_no = %s." % (card_no, ret[0]['car_no']))
                self.CarComboBox.setCurrentText(ret[0]['car_no'])
                if self.__set_barrier(self.gate_type, 1):
                    print("道闸%s打开成功" % self.gate_type)
                    try:
                        str1 = """请上磅"""
                        self.speaker.speak(str1)
                    except Exception as e:
                        logging.error(e)
                    self.weight_working = 1
                    self.card_no = card_no
                else:
                    logging.error("道闸%s打开失败" % self.gate_type)
            else:
                try:
                    str1 = """卡片无效"""
                    self.speaker.speak(str1)
                except Exception as e:
                    logging.error(e)
                logging.warning("read_no = %s and card_no = %s 没有记录" % (read_no, card_no))

    def check_weight_state(self):
        u"""
        获取停止读取标志
        :return:
        """
        if self._is_open:
            now = int(time.time() * 1000)
            first = now if len(self._weight) == 0 else min(self._weight.keys())
            if first + NormalParam.STABLES_DURATION * 1000 < now:
                weights = [v for k, v in self._weight.items() if now - k <= NormalParam.STABLES_DURATION * 1000]
                if normal_utils.stdev(weights, self.weightLcdNumber.value()) <= NormalParam.STABLES_ERROR and self.weightLcdNumber.value() > NormalParam.BALANCE_LOW:
                    self.stateLabel.setText(u'稳定')
                    self.stateLabel.setStyleSheet('color:green')
                    self.pickBalanceButton.setEnabled(True)
                    if self.weight_working == 1:
                        if normal_utils.get_barrier_state(-2 - self.gate_type) == 1:
                            start = time.time() * 1000
                            self.choose_weight()
                            self.save_data()
                            self.weight_working = 0
                            self.__set_barrier(3 - self.gate_type, 1)
                            logging.info("=========保存数据耗时: %s 毫秒" % str(time.time() * 1000 - start))
                        else:
                            try:
                                self._weight.clear()
                                str1 = """请注意，未完全上榜"""
                                self.speaker.speak(str1)
                            except Exception as e:
                                logging.error(e)
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
            self.pickBalanceButton.setEnabled(False)

    def closeEvent(self, event):
        """
        点击X号退出事件
        :param event:
        :param confirm:
        :return:
        """
        if self.close_confirm:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '本程序',
                                                   "是否要退出程序？",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                if self._barrier_worker1:
                    self._barrier_worker1.stop()
                    while not self._barrier_worker1.isStoped():
                        time.sleep(0.02)
                    self._barrier_worker1 = None
                if self._barrier_worker1:
                    self._barrier_worker1.stop()
                    while not self._barrier_worker1.isStoped():
                        time.sleep(0.02)
                    self._barrier_worker2 = None
                if self._com_worker:
                    self._com_worker.stop()
                    while not self._com_worker.isStoped():
                        time.sleep(0.02)
                for thread in self.thread_dict.values():
                    thread.stop()
                event.accept()
            else:
                event.ignore()
        else:
            if self._barrier_worker1:
                self._barrier_worker1.stop()
                while not self._barrier_worker1.isStoped():
                    time.sleep(0.02)
                self._barrier_worker1 = None
            if self._barrier_worker1:
                self._barrier_worker1.stop()
                while not self._barrier_worker1.isStoped():
                    time.sleep(0.02)
                self._barrier_worker2 = None
            if self._com_worker:
                self._com_worker.stop()
                while not self._com_worker.isStoped():
                    time.sleep(0.02)
            for thread in self.thread_dict.values():
                thread.stop()
            event.accept()

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
        self.CarComboBox.clear()
        for row in range(car_row_no):
            values = list(car_list[row].values())[0]
            self.CarComboBox.addItem(values)
        self.CarComboBox.clearEditText()
        self.operatorComboBox.setCurrentText(self.user_name)

    def set_table_view(self):
        """
        :return:
        """
        header = ['单号', '车牌号', '毛重', '皮重', '净重', '货物名', '供货单位', '收货单位', '包装物重', '另扣',
                  '杂志', '水分', '单价', '金额', '含油', '结算重量', '规格', '驾驶员', '计划单号', '运货单位', '称重时间1',
                  '称重日期', '称重时间2', '操作员', '是否完成', '备注', '备用1', '备用2', '备用3', '备用4']
        weekday = (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d %H:%M:%S')
        query_sql = """select * from t_balance where balance_time1>'%s' and status=0 and (ext3 != '1' or ext3 is null) order by balance_time1 desc""" %weekday
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
            self.settlementLcdNumber.display(self.tableView.model().index(index.row(), 15).data())
            self.extraWeightSpinBox.setValue(float(self.tableView.model().index(index.row(), 9).data()))
            self.priceSpinBox.setValue(float(self.tableView.model().index(index.row(), 12).data()))
            self.amountSpinBox.setValue(float(self.tableView.model().index(index.row(), 13).data()))

            self.CarComboBox.setCurrentText(self.tableView.model().index(index.row(), 1).data())
            self.supplierComboBox.setCurrentText(self.tableView.model().index(index.row(), 6).data())
            self.receiverComboBox.setCurrentText(self.tableView.model().index(index.row(), 7).data())
            self.goodsComboBox.setCurrentText(self.tableView.model().index(index.row(), 5).data())
            self.operatorComboBox.setCurrentText(str(self.tableView.model().index(index.row(), 23).data()))
            self.balance_status = str(self.tableView.model().index(index.row(), 24).data())
            self.balance_opt_status = 0
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
        更新重量
        :return:
        """
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
            # QtWidgets.QMessageBox.warning(self, '本程序', "磅单号不能为空！", QtWidgets.QMessageBox.Ok)
            logging.warning("磅单号不能为空！")
            return False
        balance_id = int(self.balanceNoBlael.text())
        total_weight = float(self.totalWeightLcdNumber.value())
        leather_weight = float(self.leatherWeightLcdNumber.value())
        actual_weight = float(self.actualWeightLcdNumber.value())
        extra_value = self.extraWeightSpinBox.value()
        settle = float(self.settlementLcdNumber.value())
        price = float(self.priceSpinBox.value())
        amount = float(self.amountSpinBox.value())
        car_no = self.CarComboBox.currentText()
        if not car_no:
            QtWidgets.QMessageBox.warning(self, '本程序', "车号不能为空！", QtWidgets.QMessageBox.Ok)
            logging.warning("车号不能为空！")
            return False
        supplier = self.supplierComboBox.currentText()
        receiver = self.receiverComboBox.currentText()
        goods_name = self.goodsComboBox.currentText()
        operator = self.user_name
        balance_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if self.balance_opt_status:
            today_date = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = 'shot'
            today_month = datetime.now().strftime("%Y%m")
            path = path + '\\' + str(today_month)
            abs_path = os.path.join(os.path.abspath('.'), path)
            folder = os.path.exists(abs_path)
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(abs_path)
            path = path + '\\' + str(balance_id)+str(today_date)
            self.shot_change(path)
            if self.balance_opt_status == 1 or(self.balance_opt_status ==2 and self.balance_status ==1):
                sql = '''replace into t_balance(balance_id, total_weight, leather_weight, actual_weight,
                                extra, price, amount, car_no, supplier, receiver, goods_name,balance_time1,
                                balance_time, balance_time2, operator, status,ext1,sweight) 
                                values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
                data = (balance_id, total_weight, leather_weight, actual_weight, extra_value, price, amount, car_no,
                        supplier, receiver, goods_name, balance_time, balance_time, balance_time, operator,
                        self.balance_status, path, settle)
            else:
                if self.ischange:
                    sql = '''update t_balance set total_weight= ?, leather_weight= ?, actual_weight= ?,
                                 extra= ?, price = ?, amount= ?, car_no = ?, supplier = ?, receiver = ?, 
                                 goods_name = ?, balance_time1 = ?,operator = ?, status= ?,ext2= ?,sweight=?,
                                 balance_time = ? where balance_id = ? '''
                    data = (total_weight, leather_weight, actual_weight, extra_value, price, amount, car_no,
                            supplier, receiver, goods_name, balance_time, operator, self.balance_status, path, settle,
                            balance_time, int(balance_id))
                else:
                    sql = '''update t_balance set total_weight= ?, leather_weight= ?, actual_weight= ?,
                                         extra= ?, price = ?, amount= ?, car_no = ?, supplier = ?, receiver = ?,
                                         goods_name = ?, balance_time2 = ?,operator = ?, status= ?,ext2= ?,sweight=?,
                                         balance_time = ? where balance_id = ? '''
                    data = (total_weight, leather_weight, actual_weight, extra_value, price, amount, car_no,
                            supplier, receiver, goods_name, balance_time, operator, self.balance_status, path, settle,
                            balance_time, int(balance_id))

        else:
            sql = """update t_balance set total_weight= ?, leather_weight= ?, actual_weight= ?,
                                     extra= ?, price = ?, amount= ?, car_no = ?, supplier = ?, receiver = ?, 
                                     goods_name = ?, operator = ?, status= ?,sweight=?, balance_time = ?
                                     where balance_id = ?"""
            data = (total_weight, leather_weight, actual_weight, extra_value, price, amount, car_no,
                    supplier, receiver, goods_name, operator, self.balance_status, settle, balance_time, int(balance_id))
        ret = self.db.update(sql, args=data)
        if warning:
            if ret:
                # QtWidgets.QMessageBox.warning(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
                logging.info("保存成功！")
                str1 = """过磅已完成，请下磅"""
                auto_query =" select auto_print from t_rmf where id=1"
                status = self.db.query(auto_query)
                if status[0].get('auto_print')==2:
                    if self.balance_opt_status == 2:
                        self.print_data()
                        str1 = """过磅已完成，请领取打印单"""
                self.carfollow=0
                try:
                    self.speaker.speak(str1)
                except Exception as e:
                    logging.error(e)
            else:
                # QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)
                logging.warning("保存失败！")
        if ret:
            self.set_table_view()
            self.clear_data()
            return True

    def clear_data(self):
        """
        清空数据
        :return:
        """
        self.balanceNoBlael.setText('')
        self.totalWeightLcdNumber.display(0)
        self.leatherWeightLcdNumber.display(0)
        self.actualWeightLcdNumber.display(0)
        # self.extraWeightSpinBox.setValue(0)
        self.settlementLcdNumber.display(0)
        self.priceSpinBox.setValue(0)
        self.amountSpinBox.setValue(0)
        self.CarComboBox.setCurrentText('')
        self.supplierComboBox.setCurrentText('')
        self.receiverComboBox.setCurrentText('')
        self.goodsComboBox.setCurrentText('')
        self.operatorComboBox.setCurrentText(self.user_name)
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
        ret = self.db.update(car_update, args=(car_no, total_weight))
        if ret:
            QtWidgets.QMessageBox.warning(self, '本程序', "存皮成功！", QtWidgets.QMessageBox.Ok)
            self.update_combobox()

    def print_data(self):
        """
        打印
        :return:
        """
        if not self.balanceNoBlael.text():
            if self.stateLabel.text() != u'稳定':
                # QtWidgets.QMessageBox.warning(self, '本程序', "状态未稳定！", QtWidgets.QMessageBox.Ok)
                logging.error("状态未稳定！")
            else:
                # QtWidgets.QMessageBox.warning(self, '本程序', "请选择要打印的磅单！", QtWidgets.QMessageBox.Ok)
                logging.error("没有要打印的磅单！")
            return
        balance_id = int(self.balanceNoBlael.text())
        if self.save_data(warning=False):
            sql = 'select default_rmf, auto_print from t_rmf'
            ret = self.db.query(sql)
            default_rmf = ret[0].get('default_rmf', u'过称单(标准式).rmf')
            action = 3 if ret[0].get('auto_print', 0) else 1
            cmd_str = self.report_file + u' -d "balance.db" -s "db1:select t_balance.* from t_balance where  balance_id=\'%s\'" -r "%s" -a %s' % (
                balance_id, default_rmf, action)
            # cmd_str = self.report_file + u' -d "balance.db" -s "db1:select t_balance.*,t_supplier.* from t_balance,t_supplier where  t_balance.supplier = t_supplier.supplier_name and balance_id=\'%s\'" -r "%s" -a 1' % (balance_id, default_rmf)
            logging.debug(cmd_str)
            self.p = subprocess.Popen(cmd_str)

    def choose_weight(self):
        """
        取重量
        :return:
        """
        # print("choose_weight")
        current_weight = self.weightLcdNumber.value()
        car_no = self.CarComboBox.currentText()
        if not car_no:
            QtWidgets.QMessageBox.warning(self, '本程序', "请先设置车号！", QtWidgets.QMessageBox.Ok)
            return
        # nowdate = datetime.datetime.now().strftime('%Y-%m-%d')
        weekday = (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d %H:%M:%S')
        balance_query = """select * from t_balance where balance_time1> '%s' and car_no = '%s' and (ext3 != '1' or ext3 is null) and status=0 order by balance_time1 DESC """ % (weekday,car_no)
        # print(balance_query)
        ret = self.db.query(balance_query)
        if ret:
            #QtWidgets.QMessageBox.warning(self, '本程序', "此车 %s 有未完成的磅单，正在进行完成操作!" % car_no, QtWidgets.QMessageBox.Ok)
            logging.info("此车 %s 有未完成的磅单，正在进行完成操作!" % car_no)
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
            self.balance_opt_status = 2
        else:
            balance_id = normal_utils.generate_balance_id()
            self.balanceNoBlael.setText(balance_id)
            car_query = """select car_no, leather_weight from t_car where car_no='%s'""" % car_no
            ret = self.db.query(car_query)
            if not ret:
                # 没有存皮的情况
                #QtWidgets.QMessageBox.warning(self, '本程序', "该车 %s 没有存皮，将生成未完成磅单！" % car_no, QtWidgets.QMessageBox.Ok)
                logging.info("该车 %s 没有存皮，将生成未完成磅单！" % car_no)
                self.actualWeightLcdNumber.display(current_weight)
                self.balance_status = 0
                balance_query = """select * from t_card_info where car_no = '%s'  and card_status=1  """ % car_no
                ret = self.db.query(balance_query)
                data = ret[0]
                self.balance_opt_status = 1
                if data:
                    self.priceSpinBox.setValue(data.get('price', 0.))
                    self.amountSpinBox.setValue(data.get('amount', 0.))
                    self.supplierComboBox.setCurrentText(data.get('supplier', ''))
                    self.receiverComboBox.setCurrentText(data.get('receiver', ''))
                    self.goodsComboBox.setCurrentText(data.get('cargo', ''))
                    self.extraWeightSpinBox.setValue(data.get('extra', 0.))
                    #self.operatorComboBox.setCurrentText(data.get('operator', ''))
                    #self.balance_status = data.get('status', '')
                else:
                    self.totalWeightLcdNumber.display(self.weightLcdNumber.value())
            else:
                # 有存皮
                # QtWidgets.QMessageBox.warning(self, '本程序', "该车 %s 已有存皮，将自动生成磅单！" % car_no, QtWidgets.QMessageBox.Ok)
                logging.warning("该车 %s 已有存皮，将自动生成磅单！" % car_no)
                leather_weight_db = ret[0].get('leather_weight', 0)
                actual_weight = current_weight - leather_weight_db
                self.leatherWeightLcdNumber.display(leather_weight_db)
                self.actualWeightLcdNumber.display(actual_weight)
                self.balance_status = 1
                self.balance_opt_status = 2
                balance_query = """select * from t_card_info where car_no = '%s'  and card_status=1  """ % car_no
                ret = self.db.query(balance_query)
                data = ret[0]
                if data:
                    self.priceSpinBox.setValue(data.get('price', 0.))
                    self.amountSpinBox.setValue(data.get('amount', 0.))
                    self.supplierComboBox.setCurrentText(data.get('supplier', ''))
                    self.receiverComboBox.setCurrentText(data.get('receiver', ''))
                    self.goodsComboBox.setCurrentText(data.get('cargo', ''))
                    self.extraWeightSpinBox.setValue(data.get('extra', 0.))
                    #self.operatorComboBox.setCurrentText(data.get('operator', ''))
                    #self.balance_status = data.get('status', '')
                else:
                    self.totalWeightLcdNumber.display(self.weightLcdNumber.value())
            self.totalWeightLcdNumber.display(current_weight)

        self.calculate()

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


class CardThread(QThread):
    """
    串口读取线程
    """
    trigger = pyqtSignal(tuple)

    def __init__(self, read_no):
        self._is_conn = False
        self._serial = None
        self._is_running = True
        super().__init__()
        self.stoped = False
        self.read_no = read_no
        self.mutex = QMutex()
        self.com_interface = None
        self.com_baud_rate = None
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.init_data()

    def init_data(self):
        """
        初始化端口数据
        :return:
        """
        query_sql_com1 = 'select * from t_com_auto where id = 1'
        ret = self.db.query(query_sql_com1)[0]
        self.com_interface = 'COM%s' % (ret['read_com1'] if self.read_no == 1 else ret['read_com2'])
        self.com_baud_rate = 9600

    def init_serial(self):
        u"""
        :return:
        """
        if self._serial:
            if self.com_interface != self._serial.portstr or self.com_baud_rate != self._serial.baudrate:
                self._serial = serial.Serial(self.com_interface, self.com_baud_rate, timeout=0.5)
            if not self._serial.is_open:
                self._serial.open()
        else:
            self._serial = serial.Serial(self.com_interface, self.com_baud_rate, timeout=0.5)
        if self._serial.isOpen():
            logging.info("CardThread open success %s" % self.read_no)
        else:
            logging.error("CardThread open failed")
            raise Exception(u'%s 串口打开失败！' % self.com_interface)

    def run(self):
        """
        读取串口信息
        :return:
        """
        with QMutexLocker(self.mutex):
            self.stoped= False
        while not self.stoped:
            while not self._is_conn and not self.stoped:
                try:
                    self.init_serial()
                    self._is_conn = True if self._serial.isOpen() else False
                except serial.serialutil.SerialException as e:
                    logging.error(e)
                    logging.info(u'%s 接口未连接！' % self.com_interface)
                    time.sleep(NormalParam.COM_CHECK_CONN_DURATION)
                except Exception as e:
                    logging.warning(self.com_interface)
                    logging.error(e)
                    time.sleep(NormalParam.COM_OPEN_DURATION)
            while not self.stoped and self._serial.is_open:
                is_open = 1
                try:
                    card_no = com_interface_utils.read_card_no(self._serial)
                    if card_no == NormalParam.ERROR_CARD_NO:
                        time.sleep(NormalParam.COM_OPEN_DURATION)
                        continue
                    self.trigger.emit((self.read_no, is_open, str(card_no)))
                    time.sleep(NormalParam.CARD_READ_DURATION / 1000)
                except Exception as e:
                    logging.error(e)
            self.trigger.emit((self.read_no, 0, str(NormalParam.ERROR_CARD_NO)))
            self._is_conn = False
        try:
            self._serial.close()
        except Exception as e:
            logging.error(e)
        self._is_running = False

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped= True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped and not self._is_running


class COMThread(QThread):
    """
    串口读取线程
    """
    trigger = pyqtSignal(int, float)

    def __init__(self):
        self._is_conn = False
        self._serial = None
        self._is_running = True
        super().__init__()
        self.stoped = False
        self.mutex = QMutex()
        self.com_interface = None
        self.com_baud_rate = None
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.init_data()

    def init_data(self):
        """
        初始化端口数据
        :return:
        """
        query_sql_com1 = 'select * from t_com where is_default = 1'
        ret = self.db.query(query_sql_com1)[0]
        self.com_interface = ret['com_no']
        self.com_baud_rate = ret['baud_rate']

    def init_serial(self):
        u"""
        :return:
        """
        if self._serial:
            if self.com_interface != self._serial.portstr or self.com_baud_rate != self._serial.baudrate:
                self._serial = serial.Serial(self.com_interface, self.com_baud_rate, timeout=0.5)
            if not self._serial.is_open:
                self._serial.open()
        else:
            self._serial = serial.Serial(self.com_interface, self.com_baud_rate, timeout=0.5)
        if self._serial.isOpen():
            logging.info("open success")
        else:
            logging.error("open failed")
            raise Exception(u'%s 串口打开失败！' % self.com_interface)

    def run(self):
        """
        读取串口信息
        :return:
        """
        with QMutexLocker(self.mutex):
            self.stoped= False
        DEBUG = False
        while not self.stoped:
            if DEBUG:
                while not self.stoped:
                    weight = 100
                    self.trigger.emit(1, weight)
                    time.sleep(NormalParam.COM_READ_DURATION / 1000)
                self.trigger.emit(0, 0)
            else:
                while not self._is_conn and not self.stoped:
                    try:
                        self.init_serial()
                        self._is_conn = True if self._serial.isOpen() else False
                    except serial.serialutil.SerialException as e:
                        logging.error(e)
                        logging.info(u'%s 接口未连接！' % self.com_interface)
                        time.sleep(NormalParam.COM_CHECK_CONN_DURATION)
                    except Exception as e:
                        logging.error(e)
                        time.sleep(NormalParam.COM_OPEN_DURATION)
                while not self.stoped and self._serial.is_open:
                    is_open = 1
                    try:
                        weight = com_interface_utils.read_com_interface(self._serial)
                        if weight == NormalParam.ERROR_WEIGHT:
                            time.sleep(NormalParam.COM_OPEN_DURATION)
                            break
                        self.trigger.emit(is_open, weight)
                        time.sleep(NormalParam.COM_READ_DURATION / 1000)
                    except Exception as e:
                        logging.error(e)
                self.trigger.emit(0, 0)
                self._is_conn = False
        try:
            self._serial.close()
        except Exception as e:
            logging.error(e)
        self._is_running = False

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped= True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped and not self._is_running


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
        self.is_running = False
        self.read_retry = 0

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        is_connect = normal_utils.is_connected(self.url)
        if is_connect:
            logging.info('camera can connect.')
        else:
            logging.error('camera connect failed.')
            return
        cap = cv2.VideoCapture(self.url)
        while cap.isOpened() and not self.stoped:
            self.is_running = True
            try:
                ret, frame = cap.read()
                # 读取失败，有可能连接断开或没有视频文件
                if not ret:
                    self.read_retry += 1
                    logging.error("carema read failed.")
                    if self.read_retry > 1:
                        self.read_retry = 0
                        cap.release()
                        time.sleep(0.5)
                        if normal_utils.is_connected(self.url):
                            cap.open(self.url)
                            logging.error("carema open again success.")
                        else:
                            logging.error("carema open again failed.")
                    continue
                frame_mini = cv2.resize(frame, (self.video_width, self.video_height))
                height, width, bytesPerComponent = frame_mini.shape
                bytesPerLine = bytesPerComponent * width
                # 变换彩色空间顺序
                cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame_mini)
                image = QImage(frame_mini.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.breakSignal.emit(str(self.camera_no), QPixmap.fromImage(image))
                if self.shot_flag:
                    logging.info('camera shot image! saved in %s.' % self.path)
                    cv2.imwrite(self.path, frame)
                    self.shot_flag = False
                    self.shortImage.emit(self.path)
                # 50毫秒发送一次信号
                # time.sleep(0.05)
            except Exception as e:
                logging.error(e)
                time.sleep(0.5)
                continue
        self.breakSignal.emit(str(self.camera_no), QPixmap(""))
        cap.release()
        self.is_running = False

    def set_size(self, width, height):
        """
        设置视频大小
        :param width:
        :param height:
        :return:
        """
        self.video_width = width
        self.video_height = height

    def shot_image(self, path):
        """
        截图操作
        :return:
        """
        self.shot_flag = True
        self.path = path

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped= True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped and not self.is_running


class SpeakerThread(QThread):
    """
    语音播报线程
    """
    def __init__(self):
        """
        初始化
        """
        super(SpeakerThread, self).__init__()
        self.speaker = comtypes.client.CreateObject("SAPI.SpVoice")
        self.words = ""
        self.mutex = QMutex()
        self.do_speak = False
        self.stoped = False

    def speak(self, words):
        """
        语音播报
        :param words:
        :return:
        """
        if words and not self.stoped:
            self.do_speak = True
            self.words = words

    def run(self):
        """
        运行
        :return:
        """
        comtypes.CoInitialize()
        while not self.stoped:
            if self.do_speak:
                self.do_speak = False
                try:
                    self.speaker.Speak(self.words)
                except Exception as e:
                    logging.error(e)
            self.msleep(10)
        comtypes.CoUninitialize()

    def stop(self):
        """
        :return:
        """
        with QMutexLocker(self.mutex):
            self.stoped = True


class AboutDialog(QtWidgets.QDialog, Ui_AboutDialog):
    u"""
    mainform
    """
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())