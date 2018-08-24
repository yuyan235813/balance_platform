#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/24 下午2:08
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import serial
from time import sleep


def read_com_interface(my_serial):
    """
    读取串口数据
    :param my_serial:
    :return:
    """
    while True:
        data = my_serial.read_all()
        if data[0] == 0x02 and data[-1] == 0x03:
            break
        else:
            continue
        sleep(0.02)
    return format_data(data)


def format_data(data):
    """
    data 的第2个字节为符号位，倒数第4个字节为小数点偏移位数（从右往左）<br>
    中间的为具体数值
    :param data:
    :return:
    """
    ret = ''
    for item in data[1:-4]:
        ret = ret + chr(item)
    dot = data[-4]
    return ret[0:0-dot] + '.' + ret[0-dot:]


if __name__ == '__main__':
    my_serial = serial.Serial('COM5', 9600, timeout=0.5)  # /dev/ttyUSB0
    if my_serial.isOpen():
        print("open success")
    else:
        print("open failed")
    data = read_com_interface(my_serial)
    my_serial.close()
