#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/27 下午3:48
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import os
import datetime
from utils.sqllite_util import EasySqlite
from PyQt5.QtWidgets import QMessageBox, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap
import serial
import time
import hashlib
import cv2
import logging
import socket
import base64
import requests
import json


def stdev(sequence, value):
    """
    计算相对于value的平均偏离值
    :param sequence:
    :return:
    """
    if len(sequence) <= 1:
        return 0
    else:
        sdsq = sum([abs(i - value) for i in sequence])
        stdev = sdsq / len(sequence)
        return stdev


def get_file_list(path, file_type='.rmf'):
    """
    获取指定目录下特定类型的文件
    :param path:
    :param file_type:
    :return:
    """
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            pass
        elif os.path.splitext(file)[1] == file_type:
            list_name.append(file_path)
        else:
            pass
    return list_name


def get_cur_time():
    """
    获取当前时间
    :return:
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def generate_balance_id():
    """
    获取当前时间
    :return:
    """
    cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    week = datetime.datetime.now().weekday()
    balance_id = cur_time + '0' + str(week)
    return balance_id


def get_current_user_dir():
    """
    获取当前用户的主目录
    :return:
    """
    dir = os.path.expanduser('~')
    if not dir:
        dir = "c:"
    return dir


def get_pwd_md5(pwd):
    """
    加密密码
    :param pwd:
    :return:
    """
    solt = "whoisyourdady"
    return hashlib.md5((solt + pwd).encode(encoding='UTF-8')).hexdigest()


def get_user_permission(user_id):
    """
    获取用户的权限
    :param user_id:
    :return:
    """
    db = EasySqlite(r'rmf/db/balance.db')
    sql_tmp = """
        select 
            user_id,
            opt_type,
            opt_name,
            opt_code
        from 
            (
                select
                    user_id, 
                    role_id 
                from 
                    t_user 
                where 
                    user_id = '%s'
            )t1 
            join
            (
                select 
                    a.object_id,
                    a.object_type,
                    b.opt_type,
                    b.opt_name, 
                    b.opt_code
                from 
                    t_permission a 
                    join 
                    t_operation b on a.operation_id=b.id 
                where 
                    a.status=1 
                    and b.status=1
            )t2 on t1.user_id=t2.object_id;"""
    sql = sql_tmp % user_id
    ret = db.query(sql)
    logging.debug(ret)
    opt_list = []
    for item in ret:
        opt_list.append(item.get('opt_code'))
    return opt_list


def has_permission(user_id, operation):
    def base_has_permission(func):
        def wrapper(*args, **kw):
            print('user_id=%s, operation=%s' % (user_id, operation))
            print('pre')
            opt_list = get_user_permission(user_id)
            if operation in opt_list:
                output = func(*args, **kw)
            else:
                print(args[0])
                QMessageBox.warning(args[0], '本程序', "没有权限！", QMessageBox.Ok)
                return
            print('post')
            return output
        return wrapper
    return base_has_permission


@has_permission('admin', 'system_params_form1')
def test_fun(text):
    print('我就是我，不一样的烟火 %s' % text)


def show_image(path, graph: QGraphicsView, origin_size=False):
    """
    在 QGraphicsView 控件上显示图片
    """
    img = cv2.imread(path)  # 读取图像
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
    zoomscale = 1  # 图片放缩尺度
    if origin_size:
        height, width = img.shape[:2]
        frame = QImage(img, width, height, QImage.Format_RGB888)
    else:
        frame_mini = cv2.resize(img, (graph.width(), graph.height()))
        frame = QImage(frame_mini, graph.width(), graph.height(), QImage.Format_RGB888)
    pix = QPixmap.fromImage(frame)
    item = QGraphicsPixmapItem(pix)  # 创建像素图元
    item.setScale(zoomscale)
    scene = QGraphicsScene()  # 创建场景
    scene.addItem(item)
    graph.setScene(scene)
    graph.setWindowFilePath(path)


def is_connected(url):
    """
    是否可以连通 rtsp 地址
    :param url: rtsp 地址
    :return:
    """
    if len(url) < 10 and '@' in url:
        return False
    username_password, ip = url[7:].split('@')
    if ':' in ip:
        ip, port = ip.split(':')
    else:
        port = 554
    buffer_len = 1024
    auth_64 = base64.b64encode(username_password.encode("utf-8")).decode()
    header = 'DESCRIBE %s RTSP/1.0\r\n' % url
    header += 'CSeq: 4\r\n'
    header += 'User-Agent: RTSP Client\r\n'
    header += 'Accept: application/sdp\r\n'
    header += 'Authorization: Basic ' + auth_64 + ' \r\n'
    header += '\r\n'
    socket_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_send.settimeout(2)
    msg_recv = None
    try:
        socket_send.connect((ip, port))
        socket_send.send(header.encode())
        msg_recv = socket_send.recv(buffer_len).decode()
    except Exception as e:
        print(e)
    finally:
        socket_send.close()
    if msg_recv and '200 OK' in msg_recv:
        return True
    else:
        return False


def open_barrier_gate(num):
    """
    打开第 num 个道闸
    :param num:
    :return:
    """
    return set_barrier_gate(num, 1)


def close_barrier_gate(num):
    """
    关闭第 num 个道闸
    :param num:
    :return:
    """
    return set_barrier_gate(num, 0)


def set_barrier_gate(num, state):
    """
    设置道闸
    :param state:
    :return:
    """
    open_msg_1 = b"\x55\x01\x01\x00\x57"
    close_msg_1 = b"\x55\x02\x01\x00\x58"
    open_msg_2 = b"\x55\x01\x02\x00\x58"
    close_msg_2 = b"\x55\x02\x02\x00\x59"
    close_msg_all = b"\x55\x02\x0f\x00\x66"
    msgs = [open_msg_1, close_msg_1]
    states = [1, 0]
    if num == 1 and state == 0:
        msgs = [close_msg_1]
        states = [0]
    elif num == 2 and state == 1:
        msgs = [open_msg_2, close_msg_2]
        states = [1, 0]
    elif num == 2 and state == 0:
        msgs = [close_msg_2]
        states = [0]
    elif state == -1:
        msgs = [close_msg_all]
        states = [-1]
    db = EasySqlite(r'rmf/db/balance.db')
    ret = db.query("select barrier_com from t_com_auto where id = 1")
    if not ret:
        logging.error('获取道闸串口信息失败！')
        return False
    port = 'COM%s' % ret[0]['barrier_com']
    success = list()
    try:
        my_serial = serial.Serial(port, 9600, timeout=0.5)
        if my_serial.isOpen():
            start = time.time()
            for i in range(len(msgs)):
                if i == 1:
                    time.sleep(0.01)
                msg = msgs[i]
                state = states[i]
                retry = 0
                while retry < 5:
                    my_serial.write(msg)
                    retry += 1
                    read = my_serial.read(5)
                    if state == 1:
                        if read[2] & 2 ** (num - 1) == 2 ** (num - 1):
                            success.append(True)
                    elif state == 0:
                        if not read[2] & 2 ** (num - 1) == 2 ** (num - 1):
                            success.append(True)
                    else:
                        if read[2] == 0:
                            success.append(True)
                    if success:
                        if state:
                            print('open barrier %s success' % num)
                        else:
                            print('close barrier %s success' % num)
                        break
            print('set_barrier_gate spend time %s second.' % (time.time() - start))
        else:
            print("set_barrier_gate fialed num: %s -- state: %s." % (num, state))
        my_serial.close()
    except Exception as e:
        print('set_barrier_gate error: ' + str(e.__str__()))
    return True if len(msgs) == len(success) and False not in success else False


def get_barrier_state(nums):
    """
    获取道闸状态
    ****
    例如接收到如下返回帧:0x55  0xF0  0x05  0x0E  0x58
    第三字节(参数0):=0x05=0101=Y3 Y2 Y1 Y0.表示Y3,Y1断开.Y2,Y0吸合
    第四字节(参数1):=0x0E=1110=X3 X2 X1 X0.表示X3,X2,X1没信号,X0有信号
    ****
    :param nums:
    :return:-1 读取失败；0 关闭；1 打开
    """
    result = list()
    ports = list()
    if isinstance(nums, (tuple, list)):
        ports = nums
    else:
        ports.append(nums)
    send_msg = b"\x55\x04\x00\x00\x59"
    db = EasySqlite(r'rmf/db/balance.db')
    ret = db.query("select barrier_com from t_com_auto where id = 1")
    if not ret:
        logging.error('获取道闸串口信息失败！')
        return [-1 for i in range(len(ports))]
    port = 'COM%s' % ret[0]['barrier_com']
    msg = ''
    success = False
    try:
        my_serial = serial.Serial(port, 9600, timeout=0.5)
        if my_serial.isOpen():
            start = time.time()
            retry = 0
            while retry < 5:
                my_serial.write(send_msg)
                retry += 1
                msg = my_serial.read(5)
                if msg and msg[0] == 85:
                    success = True
                    break
            logging.info('get_barrier_state spend time %s second.' % (time.time() - start))
        else:
            logging.info("get_barrier_state fialed num: %s." % ",".join(ports))
        my_serial.close()
    except Exception as e:
        print('get_barrier_state error: ' + str(e.__str__()))
    for num in ports:
        if num > 0:
            if success:
                if len(msg) > 2 and msg[2] & 2 ** (num - 1) == 2 ** (num - 1):
                    result.append(1)
                else:
                    result.append(0)
            else:
                result.append(-1)
        else:
            num = abs(num)
            if success:
                if len(msg) > 3 and (msg[3] ^ 15) & 2 ** (num - 1) == 2 ** (num - 1):
                    result.append(0)
                else:
                    result.append(1)
            else:
                result.append(-1)
    return result if len(result) > 1 else result[0]


def set_barrier_gate1(num, state):
    """
    设置道闸
    :param state:
    :return:
    """
    open_msg_1 = b"\x01\x05\x00\x00\xFF\x00\x8C\x3A"
    close_msg_1 = b"\x01\x05\x00\x00\x00\x00\xCD\xCA"
    open_msg_2 = b"\x01\x05\x00\x01\xFF\x00\xDD\xFA"
    close_msg_2 = b"\x01\x05\x00\x01\x00\x00\x9C\x0A"
    msg = open_msg_1
    if num == 1 and state == 0:
        msg = close_msg_1
    elif num == 2 and state == 1:
        msg = open_msg_2
    elif num == 2 and state == 0:
        msg = close_msg_2
    db = EasySqlite(r'rmf/db/balance.db')
    ret = db.query("select barrier_com from t_com_auto where id = 1")
    if not ret:
        logging.error('获取道闸串口信息失败！')
        return -1
    port = 'COM%s' % ret[0]['barrier_com']
    success = False
    try:
        my_serial = serial.Serial(port, 9600, timeout=0.5)
        if my_serial.isOpen():
            start = time.time()
            retry = 0
            while retry < 5:
                my_serial.write(msg)
                retry += 1
                if msg == my_serial.read(8):
                    print('open barrier %s success' % num)
                    success = True
                    break
            print('set_barrier_gate spend time %s second.' % (time.time() - start))
        else:
            print("set_barrier_gate fialed num: %s -- state: %s." % (num, state))
        my_serial.close()
    except Exception as e:
        print('set_barrier_gate error: ' + str(e.__str__()))
    return success


def get_barrier_state1(num):
    """
    获取道闸状态
    :param state:
    :return:-1 读取失败；0 关闭；1 打开
    """
    send_msg = b"\x01\x01\x00\x00\x00\x10\x3D\xC6"
    db = EasySqlite(r'rmf/db/balance.db')
    ret = db.query("select barrier_com from t_com_auto where id = 1")
    if not ret:
        logging.error('获取道闸串口信息失败！')
        return -1
    port = 'COM%s' % ret[0]['barrier_com']
    msg = ''
    success = False
    try:
        my_serial = serial.Serial(port, 9600, timeout=0.5)
        if my_serial.isOpen():
            start = time.time()
            retry = 0
            while retry < 5:
                print('send msg')
                my_serial.write(send_msg)
                retry += 1
                msg = my_serial.read(7)
                if msg and msg[1] == 1:
                    print('get barrier %s state success' % num)
                    success = True
                    break
            print('get_barrier_state spend time %s second.' % (time.time() - start))
        else:
            print("get_barrier_state fialed num: %s." % num)
        my_serial.close()
    except Exception as e:
        print('get_barrier_state error: ' + str(e.__str__()))
    if success:
        if len(msg) > 3 and msg[3] & num == num:
            return 1
        else:
            return 0
    else:
        return -1


def sync_data(table_name, url):
    """
    同步数据，上行
    :return:
    """
    db = EasySqlite(r'rmf/db/balance.db')
    # db = EasySqlite(r'../rmf/db/balance.db')
    time1 = '1970-01-01 00:00:00'
    time_now = datetime.datetime.now()
    time2 = (time_now + datetime.timedelta(seconds=-1)).strftime("%Y-%m-%d %H:%M:%S")
    query_sql1 = """select max(sync_time) as sync_time from t_balance_sync where table_name = '%s'""" % table_name
    if table_name == 't_balance':
        time_column = 'balance_time'
        query_sql2 = """select * from t_balance a left join (select company_id as company from t_system_params_conf limit 1) b on 1=1 where a.balance_time > '%s' and a.balance_time <='%s' order by a.balance_time limit 10"""
    else:
        time_column = 'operation_date'
        query_sql2 = """select * from t_card_info a left join (select company_id as company from t_system_params_conf limit 1) b on 1=1  where a.operation_date > '%s' and a.operation_date <='%s' order by a.operation_date limit 10"""
    ret1 = db.query(query_sql1)
    if ret1 and ret1[0].get('sync_time'):
        time1 = ret1[0].get('sync_time')
    ret2 = db.query(query_sql2 % (time1, time2))
    if ret2:
        company = ''
        sync_time = time1
        for item in ret2:
            item.pop("id")
            company = item.get('company')
            sync_time = item.get(time_column) if item.get(time_column) > sync_time else sync_time
        data = dict()
        # result 取值1，0:无需同步；-1：接口请求失败；-2:同步数据抛异常；-3：更新本地数据库失败；>0:同步成功，同步的条数
        data['count'] = result = len(ret2)
        data['data'] = json.dumps(ret2)
        data['company'] = company
        logging.info(data)
        try:
            response = requests.post(url, data)
            res = json.loads(response.text)
            logging.info(res)
            if 'success' in res.keys() and res.get('success'):
                update_sql = """insert into t_balance_sync(table_name, sync_time) values('%s', '%s')""" % (table_name, sync_time)
                ret = db.update(update_sql)
                if ret:
                    logging.info('同步数据 %s 成功，时间：%s' % (table_name, sync_time))
                else:
                    logging.error('同步数据客户端错误， %s 失败，时间：%s' % (table_name, sync_time))
            else:
                result = -1
                logging.error('同步数据服务端错误， %s 失败，时间：%s' % (table_name, sync_time))
        except Exception as e:
            logging.error(e)
            result = -2
    else:
        logging.info('没有需要同步的数据！')
        result = 0
    return result


def sync_card_info(url):
    """
    同步数据，下行
    :return:
    """
    db = EasySqlite(r'rmf/db/balance.db')
    # db = EasySqlite(r'../rmf/db/balance.db')
    query_sql1 = """select max(operation_date) as operation_date from t_card_info"""
    query_sql2 = """select * from t_system_params_conf limit 1"""
    delete_sql = """delete from t_card_info where card_no in (%s)"""
    ret1 = db.query(query_sql1)
    ret2 = db.query(query_sql2)
    if ret1 and ret1[0].get('operation_date') and ret2:
        operation_date = ret1[0].get('operation_date')
        data = dict()
        data['operation_date'] = operation_date
        data['company'] = ret2[0].get('company_id')
        # result 取值1，0:无需同步；-1：接口请求失败；-2:同步数据抛异常；-3：更新本地数据库失败；>0:同步成功，同步的条数
        data['limit'] = result = 10
        try:
            logging.info(data)
            response = requests.post(url, data)
            res = json.loads(response.text)
            # res = {'success':True, 'res':[{'card_no':'0', 'ext1':'1'},{'card_no':'1', 'ext1':'2'}]}
            logging.info(res)
            if 'success' in res.keys() and res.get('success') and len(res.get('result')) > 0:
                res_data = res.get('result')
                result = len(res_data)
                card_nos = [item.get('card_no') for item in res_data]
                delete_sql = delete_sql % ','.join(["'%s'" % card_no for card_no in card_nos])
                db.update(delete_sql, commit=False)
                insert_values = list()
                for item in res_data:
                    if 'id' in item.keys():
                        item.pop('id')
                    if 'company' in item.keys():
                        item.pop('company')
                    insert_data = [(k, item[k]) for k in item if item[k] is not None]
                    insert_sql = 'insert into t_card_info (' + ','.join(i[0] for i in insert_data) + ') values(' + ','.join(['?'] * len(item)) + ')'
                    insert_values.append(['%s' % i[1] for i in insert_data])
                logging.info(insert_values)
                ret = db.update(insert_sql, args=insert_values)
                if ret:
                    logging.info('下载卡信息成功')
                else:
                    result = -3
                    logging.error('下载卡信息失败')
            elif len(res.get('res')) <= 0:
                result = 0
            else:
                result = -1
        except Exception as e:
            result = -2
            logging.info(e)
    else:
        result = 0
    return result


if __name__ == '__main__':
    # print(get_file_list(r'H:\workspace\python3\balance_platform\rmf\rmf'))
    # print(generate_balance_id())
    # test_fun('tttt')
    # print(get_pwd_md5('kitty.'))
    # url = """http://39.97.120.140:1818/api/search/addBalance"""
    # sync_data('t_balance', url)
    # url = """http://39.97.120.140:1818/api/Card/index"""
    # sync_data('t_card_info', url)
    url = """http://39.97.120.140:1818/api/Card/getList"""
    sync_card_info(url)