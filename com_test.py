#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/24 下午2:08
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import serial
from time import sleep
from constant import ErrorCode


def read_com_interface(my_serial):
    """
    读取串口数据
    :param my_serial:
    :return:
    """
    while True:
        data = my_serial.readline(12)
        print_data(data)
        # 验证数据
        verify = verify_data(data)
        if 0 == verify:
            break
        else:
            print(verify)
            continue
        sleep(0.02)
    return format_data(data)


def print_data(data):
    """
    打印16进制和10进制data
    :param data:
    :return:
    """
    print('read data 16h: %s' % ' '.join(hex(x) for x in data))
    print('read data 10d: %s' % ' '.join(str(x) for x in data))


def verify_data(data):
    """
    data 共 12 个字节
    第1个字节：开始 0x02
    第2个字节到第9个字节为数据组
    第10、11个字节为高低异或校验字节
    第12个字节为结束 0x03
    异或校验高、低 4位的确定：异或和高、低4位如果小于、等于9，则加上30h，成为 ASCII 码数字发送，<br>
    例如：异或校验高4位为6，加30h 后，为36h 即 ASCII 码的6发送；异或和高、低4位如果大于9，<br>
    则加上37h，成为 ASCII 码字母发送，例如：异或校验高4位为 B， 加37h 后，为42h 即 ASCII 码的<br>
    B 发送。
    :param data:
    :return:
    """
    if not data:
        return ErrorCode.NOT_DATA_ERROR
    if 12 != len(data):
        return ErrorCode.DATA_LENGTH_ERROR
    if 0x02 != data[0]:
        return ErrorCode.BEGIN_ERROR
    if 0x03 != data[-1]:
        return ErrorCode.END_ERROR
    ret = data[1]
    for item in data[2:-3]:
        ret = ret ^ item
    verify_high = data[-3]
    high = (ret & 0xF0) >> 4
    high += 0x30 if high <= 9 else 0x37
    if verify_high != high:
        return ErrorCode.HIGH_VERIFY_ERROR
    verify_low = data[-2]
    low = ret & 0x0F
    low += 0x30 if low <= 9 else 0x37
    if verify_low != low:
        return ErrorCode.LOW_VERIFY_ERROR
    return 0


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


def func():
    data1 = [0x02, 0x2B, 0x30, 0x31, 0x32, 0x30, 0x30, 0x35, 0x02, 0x32, 0x46, 0x03]
    data2 = [0X02, 0x2D, 0x30, 0x31, 0x32, 0x30, 0x30, 0x35, 0x02, 0x32, 0x39, 0x03]
    data3 = [0X02, 0x2D, 0x30, 0x31, 0x32, 0x30, 0x30, 0x35, 0x00, 0x32, 0x42, 0x03]
    for data in (data1, data2, data3):
        ret = data[1]
        for item in data[2:-3]:
            ret = ret ^ item
        v1 = data[-3]
        v2 = data[-2]
        high = (ret & 0xF0) >> 4
        high += 0x30 if high <= 9 else 0x37
        low = ret & 0x0F
        low += 0x30 if low <= 9 else 0x37
        print('ret = %s, %s' % (bin(ret), hex(ret)))
        print('v1 = %s, %s' % (bin(v1), hex(v1)))
        print('v2 = %s, %s' % (bin(v2), hex(v2)))
        print('high = %s, %s' % (bin(high), hex(high)))
        print('low = %s, %s' % (bin(low), hex(low)))
        print('================')


if __name__ == '__main__':
    my_serial = serial.Serial('COM5', 9600, timeout=0.5)  # /dev/ttyUSB0
    if my_serial.isOpen():
        print("open success")
    else:
        print("open failed")
    while True:
        data = read_com_interface(my_serial)
        print(data)
    my_serial.close()
