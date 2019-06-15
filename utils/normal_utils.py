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
import hashlib
import cv2
import logging
import socket
import base64


def stdev(sequence):
    """
    计算标准差
    :param sequence:
    :return:
    """
    if len(sequence) <= 1:
        return 0
    else:
        avg = sum(sequence)/len(sequence)
        sdsq = sum([(i - avg) ** 2 for i in sequence])
        stdev = (sdsq / (len(sequence) - 1)) ** .5
        return stdev


def get_file_list(path, type='.rmf'):
    """
    获取指定目录下特定类型的文件
    :param parh:
    :param type:
    :return:
    """
    list_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            pass
        elif os.path.splitext(file)[1] == type:
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

if __name__ == '__main__':
    # print(get_file_list(r'H:\workspace\python3\balance_platform\rmf\rmf'))
    # print(generate_balance_id())
    # test_fun('tttt')
    print(get_pwd_md5('686868'))