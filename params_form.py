#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from ui.params_setup import Ui_paramsSetupForm
from ui.params_dialog import Ui_dialog
from PyQt5.QtCore import *
from utils.sqllite_util import EasySqlite
from functools import partial
import logging


class ParamsForm(QtWidgets.QWidget, Ui_paramsSetupForm):
    """
    参数设置
    """
    def __init__(self, parent):
        super(ParamsForm, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.params_dialog = ParamsDialog(self)
        self.cancelPushButton.clicked.connect(self.close)
        self.savePushButton.clicked.connect(self.save_data)
        self.portPushButton.clicked.connect(partial(self.params_dialog_show, 't_com_conf', 'com_no'))
        self.baudPushButton.clicked.connect(partial(self.params_dialog_show, 't_baud_rate_conf', 'baud_rate'))
        self.verifyPushButton.clicked.connect(partial(self.params_dialog_show, 't_verification_bit_conf', 'verification_bit'))
        self.dataPushButton.clicked.connect(partial(self.params_dialog_show, 't_data_bit_conf', 'data_bit'))
        self.stopPushButton.clicked.connect(partial(self.params_dialog_show, 't_stop_bit_conf', 'stop_bit'))
        self.testPushButton1.clicked.connect(self.test_camera1)
        self.testPushButton2.clicked.connect(self.test_camera2)
        self.testPushButton3.clicked.connect(self.test_camera3)
        self.testPushButton4.clicked.connect(self.test_camera4)
        self.set_data()

    def params_dialog_show(self, table, column):
        """
        参数配置对话框
        :return:
        """
        self.params_dialog.my_signal.connect(self.set_data)
        self.params_dialog.show(table, column)

    def set_data(self, table=''):
        """
        设置combobox 数据
        :param table:
        :return:
        """
        logging.info(table)
        # com 端口
        self.set_com()
        # 波特率
        self.set_baud_rate()
        # 校验位
        self.set_verification_bit()
        # 数据位
        self.set_data_bit()
        # 结束位
        self.set_stop_bit()
        # 设置默认值
        query_sql = 'select * from t_com where is_default = 1'
        ret = self.db.query(query_sql)[0]
        if ret:
            self.portComboBox.setCurrentText(ret['com_no'])
            self.baudComboBox.setCurrentText(str(ret['baud_rate']))
            self.verifyComboBox.setCurrentText(str(ret['verification_bit']))
            self.dataComboBox.setCurrentText(str(ret['data_bit']))
            self.stopComboBox.setCurrentText(str(ret['stop_bit']))
        # 设置摄像头
        query_sql = """select * from t_camera where camera_no <= 4"""
        ret = self.db.query(query_sql)
        if ret:
            for item in ret:
                if item['camera_no'] == 1:
                    self.ip1LineEdit.setText(item['ip_addr'])
                    self.user1LineEdit.setText(item['user_id'])
                    self.pwd1LineEdit.setText(item['password'])
                    if item['is_active']:
                        self.camera1CheckBox.setChecked(True)
                elif item['camera_no'] == 2:
                    self.ip2LineEdit.setText(item['ip_addr'])
                    self.user2LineEdit.setText(item['user_id'])
                    self.pwd2LineEdit.setText(item['password'])
                    if item['is_active']:
                        self.camera2CheckBox.setChecked(True)
                elif item['camera_no'] == 3:
                    self.ip3LineEdit.setText(item['ip_addr'])
                    self.user3LineEdit.setText(item['user_id'])
                    self.pwd3LineEdit.setText(item['password'])
                    if item['is_active']:
                        self.camera3CheckBox.setChecked(True)
                elif item['camera_no'] == 4:
                    self.ip4LineEdit.setText(item['ip_addr'])
                    self.user4LineEdit.setText(item['user_id'])
                    self.pwd4LineEdit.setText(item['password'])
                    if item['is_active']:
                        self.camera4CheckBox.setChecked(True)

    def set_com(self):
        """
        com 端口
        :return:
        """
        com_list = self.get_conf_list('t_com_conf', 'com_no')
        self.portComboBox.clear()
        self.portComboBox.addItems(com_list)

    def set_baud_rate(self):
        """
        波特率
        :return:
        """
        baud_rate_list = self.get_conf_list('t_baud_rate_conf', 'baud_rate')
        self.baudComboBox.clear()
        self.baudComboBox.addItems(baud_rate_list)

    def set_verification_bit(self):
        """
        校验
        :return:
        """
        verification_bit_list = self.get_conf_list('t_verification_bit_conf', 'verification_bit')
        self.verifyComboBox.clear()
        self.verifyComboBox.addItems(verification_bit_list)

    def set_data_bit(self):
        """
        数据位
        :return:
        """
        data_bit_list = self.get_conf_list('t_data_bit_conf', 'data_bit')
        self.dataComboBox.clear()
        self.dataComboBox.addItems(data_bit_list)

    def set_stop_bit(self):
        """
        停止位
        :return:
        """
        stop_bit_list = self.get_conf_list('t_stop_bit_conf', 'stop_bit')
        self.stopComboBox.clear()
        self.stopComboBox.addItems(stop_bit_list)

    def save_data(self):
        """
        :return:
        """
        com_no = self.portComboBox.currentText()
        ret_com_no = self.update_conf('t_com_conf', 'com_no', com_no)
        baud_rate = self.baudComboBox.currentText()
        ret_baud_rate = self.update_conf('t_baud_rate_conf', 'baud_rate', baud_rate)
        verification_bit = self.verifyComboBox.currentText()
        ret_verification_bit = self.update_conf('t_verification_bit_conf', 'verification_bit', verification_bit)
        data_bit = self.dataComboBox.currentText()
        ret_data_bit = self.update_conf('t_data_bit_conf', 'data_bit', data_bit)
        stop_bit = self.stopComboBox.currentText()
        ret_stop_bit = self.update_conf('t_stop_bit_conf', 'stop_bit', stop_bit)
        logging.debug(ret_com_no)
        logging.debug(ret_baud_rate)
        logging.debug(ret_verification_bit)
        logging.debug(ret_data_bit)
        logging.debug(ret_stop_bit)
        ret = 0
        if (ret_com_no or ret_baud_rate or ret_verification_bit or ret_data_bit or ret_stop_bit):
            update_sql = '''update t_com set com_no="%s",baud_rate=%s,verification_bit=%s,data_bit=%s,stop_bit=%s
             where is_default=1''' % (com_no, baud_rate, verification_bit, data_bit, stop_bit)
            logging.debug(update_sql)
            ret = self.db.update(update_sql, commit=False)
        ret1 = self.save_camera()
        if ret and ret1:
            QtWidgets.QMessageBox.information(self, '本程序', "保存成功！", QtWidgets.QMessageBox.Ok)
            self.set_data()
            self.parent.active_video()
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', "保存失败！", QtWidgets.QMessageBox.Ok)

    def save_camera(self):
        """
        保存摄像头设置
        :return:
        """
        sql_tmp = """replace into t_camera(ip_addr, user_id, password, camera_name, is_active, camera_no) values(?, ?, ?, ?, ?, ?)"""
        camera1 = (self.ip1LineEdit.text(), self.user1LineEdit.text(), self.pwd1LineEdit.text(), '摄像头1', 1 if self.camera1CheckBox.isChecked() else 0, 1)
        camera2 = (self.ip2LineEdit.text(), self.user2LineEdit.text(), self.pwd2LineEdit.text(), '摄像头2', 1 if self.camera2CheckBox.isChecked() else 0, 2)
        camera3 = (self.ip3LineEdit.text(), self.user3LineEdit.text(), self.pwd3LineEdit.text(), '摄像头3', 1 if self.camera3CheckBox.isChecked() else 0, 3)
        camera4 = (self.ip4LineEdit.text(), self.user4LineEdit.text(), self.pwd4LineEdit.text(), '摄像头4', 1 if self.camera4CheckBox.isChecked() else 0, 4)
        ret = self.db.update(sql_tmp, args=[camera1, camera2, camera3, camera4])
        return ret


    def get_conf_list(self, table, column):
        """
        获取端口配置列表
        :param table:
        :param column:
        :return:
        """
        query_sql = 'select %s from %s order by %s' % (column, table, column)
        ret = self.db.query(query_sql, result_dict=False)
        if ret:
            data_list = map(str, list(zip(*ret))[0])
            return data_list
        else:
            return list()

    def update_conf(self, table, column, value):
        """
        更新配置
        :param table:
        :param column:
        :param value:
        :return:
        """
        update_sql = 'replace into %s(%s) values("%s")' % (table, column, value)
        ret = self.db.update(update_sql)
        return ret

    def test_camera1(self):
        """
        测试摄像头1
        :return:
        """
        ip_addr = self.ip1LineEdit.text()
        user_id = self.user1LineEdit.text()
        password = self.pwd1LineEdit.text()
        self.test_camera(ip_addr, user_id, password)

    def test_camera2(self):
        """
        测试摄像头2
        :return:
        """
        ip_addr = self.ip2LineEdit.text()
        user_id = self.user2LineEdit.text()
        password = self.pwd2LineEdit.text()
        self.test_camera(ip_addr, user_id, password)

    def test_camera3(self):
        """
        测试摄像头3
        :return:
        """
        ip_addr = self.ip3LineEdit.text()
        user_id = self.user3LineEdit.text()
        password = self.pwd3LineEdit.text()
        self.test_camera(ip_addr, user_id, password)

    def test_camera4(self):
        """
        测试摄像头4
        :return:
        """
        ip_addr = self.ip4LineEdit.text()
        user_id = self.user4LineEdit.text()
        password = self.pwd4LineEdit.text()
        self.test_camera(ip_addr, user_id, password)

    def test_camera(self, ip_addr, user_id, password):
        """
        测试摄像头
        :return:
        """
        if not ip_addr:
            QtWidgets.QMessageBox.warning(self, '本程序', 'ip不能为空！')
            return
        if not user_id:
            QtWidgets.QMessageBox.warning(self, '本程序', '用户名不能为空！')
            return
        if not password:
            QtWidgets.QMessageBox.warning(self, '本程序', '密码不能为空！')
            return
        url = "rtsp://%s:%s@%s" % (user_id, password, ip_addr)
        test_thread = CameraTestThread(url)
        test_thread.start()
        import time
        time.sleep(2)
        if test_thread.get_result():
            logging.info('camera open success.')
            QtWidgets.QMessageBox.information(self, '本程序', '连接成功！')
        else:
            QtWidgets.QMessageBox.warning(self, '本程序', '连接失败！')
        test_thread.terminate()


class ParamsDialog(QtWidgets.QDialog, Ui_dialog):
    """
    参数修改
    """
    my_signal = pyqtSignal(str)

    def __init__(self, parent):
        super(ParamsDialog, self).__init__()
        self.setupUi(self)
        # 自定义信号
        self.table = ''
        self.column = ''
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.setWindowModality(Qt.ApplicationModal)
        self.addPushButton.clicked.connect(self.add_item)
        self.deletePushButton.clicked.connect(self.delete_item)
        self.savePushButton.clicked.connect(self.save_item)
        self.cancelPushButton.clicked.connect(self.cancel_item)

    def show(self, table, column):
        """
        :param table:
        :param column:
        :return:
        """
        super(ParamsDialog, self).show()
        self.table = table
        self.column = column
        title = ''
        group_box = ''
        if table == 't_com_conf':
            title = u'端口设置'
            group_box = u'端口设置'
        elif table == 't_baud_rate_conf':
            title = u'波特率设置'
            group_box = u'波特率设置'
        elif table == 't_verification_bit_conf':
            title = u'校验设置'
            group_box = u'校验设置'
        elif table == 't_data_bit_conf':
            title = u'数据位设置'
            group_box = u'数据位设置'
        elif table == 't_stop_bit_conf':
            title = u'停止位设置'
            group_box = u'停止位设置'
        self.setWindowTitle(title)
        self.groupBox.setTitle(group_box)
        self.label.setText(title[:-2])
        list_item = self.get_conf_list(table, column)
        self.listWidget.clear()
        self.listWidget.addItems(list_item)


    def add_item(self):
        """
        增加item
        :return:
        """
        text = self.lineEdit.text()
        if self.listWidget.findItems(text, Qt.MatchExactly):
            QtWidgets.QMessageBox.warning(self, '本程序', u'%s 已经存在!' % text, QtWidgets.QMessageBox.Ok)
        else:
            if self.windowTitle() != u'端口设置':
                if not text.isdigit():
                    QtWidgets.QMessageBox.warning(self, u'本程序', u'请输入数字!', QtWidgets.QMessageBox.Ok)
                    return self
            self.listWidget.addItem(text)

    def delete_item(self):
        """
        删除item
        :return:
        """
        if not self.listWidget.currentItem():
            QtWidgets.QMessageBox.warning(self, '本程序', "请选择要删除的参数！", QtWidgets.QMessageBox.Ok)
            return
        if self.listWidget.count():
            if self.listWidget.selectedItems():
                remove_items = self.listWidget.selectedItems()
                self.listWidget.removeItemWidget(self.listWidget.takeItem(self.listWidget.row(remove_items[0])))

    def save_item(self):
        """
        保存item
        :return:
        """
        items = [self.listWidget.item(i) for i in range(self.listWidget.count())]
        list_value = [item.text() for item in items]
        ret = self.update_conf(self.table, self.column, list(zip(list_value)))
        if ret:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)
            self.my_signal.emit(self.table)
        else:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)

    def cancel_item(self):
        """
        取消更改
        :return:
        """
        self.close()

    def get_conf_list(self, table, column):
        """
        获取端口配置列表
        :param table:
        :param column:
        :return:
        """
        query_sql = 'select %s from %s order by %s' % (column, table, column)
        ret = self.db.query(query_sql, result_dict=False)
        data_list = map(str, list(zip(*ret))[0])
        return data_list

    def update_conf(self, table, column, value):
        """
        更新配置
        :param table:
        :param column:
        :param value:
        :return:
        """
        self.db.update('delete from %s' % table, commit=False)
        update_sql = 'replace into %s(%s) values(?)' % (table, column)
        logging.debug(value)
        ret = self.db.update(update_sql, args=value)
        return ret


class CameraTestThread(QThread):
    """
    测试摄像头连通性
    """
    def __init__(self, url):
        super(CameraTestThread, self).__init__()
        self.url = url
        self.result = 0

    def run(self):
        import cv2
        try:
            cap = cv2.VideoCapture(self.url)
        except Exception as e:
            print(e)
        self.result = 1 if cap.isOpened() else 0

    def get_result(self):
        return self.result


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = ParamsForm()
    myshow.show()
    sys.exit(app.exec_())

