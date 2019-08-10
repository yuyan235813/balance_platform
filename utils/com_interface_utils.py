#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/24 下午2:08
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import serial
from time import sleep
from conf.constant import ErrorCode, NormalParam
from conf.config import (COM_BAUD_RATE, COM_INTERFACE)
import logging


def read_com_interface(my_serial):
    """
    读取串口数据
    :param my_serial:
    :return:
    """
    retry_time = 0
    while retry_time < NormalParam.COM_RETRY_TIMES:
        retry_time += 1
        my_serial.flush()
        data = my_serial.read(12)
        print_data(my_serial.portstr, data)
        # 验证数据
        verify = verify_data(data)
        if 0 == verify:
            break
        else:
            logging.error(verify)
            continue
        sleep(NormalParam.COM_READ_DURATION / 2 /1000)
    if 0 != verify:
        return NormalParam.ERROR_WEIGHT
    return format_data(data)


def read_com_interface_3168(my_serial):
    """
    读取串口数据
    :param my_serial:
    :return:
    """
    retry_time = 0
    while retry_time < NormalParam.COM_RETRY_TIMES:
        retry_time += 1
        my_serial.flush()
        data = my_serial.read(5)
        print_data(my_serial.portstr, data)
        # 验证数据
        verify = verify_data_3168(data)
        if 0 == verify:
            break
        else:
            logging.error(verify)
            continue
        sleep(NormalParam.COM_READ_DURATION / 2 /1000)
    if 0 != verify:
        return NormalParam.ERROR_WEIGHT
    return format_data_3168(data)


def print_data(port, data):
    """
    打印16进制和10进制data
    :param data:
    :return:
    """
    logging.debug('%s read data 16h: %s' % (port, ' '.join(hex(x) for x in data)))
    logging.debug('%s read data 10d: %s' % (port, ' '.join(str(x) for x in data)))


def verify_data_3168(data):
    """
    数据格式:
     每隔 100ms 发送一组数据.每组数据 5 帧,每帧
    数据有 11 位:1 位起始位(0),8 位数据位,2 位停止位(1)。
    第 1 帧：D0～D7······0FFH(起始标志帧)。
    第 2 帧：D0～D2······小 数点位置(0-5)。
    D4······1 表示称重值稳定,0 表示不稳定。
    D5······1 表示重量为负值,0 表示重量为正值。
    D7······1 表示超载。
    第 3 帧:D0～D3 位为重量值个位的 BCD 码。
     D4～D7 位为重量值十位的 BCD 码。
    第 4 帧 :D0～D3 位 为重量值百位的 BCD 码。
     D4～D7 位为重量值千位的 BCD 码。
    第 5 帧:D0～D3 位为重量值万位的 BCD 码。
     D4～D7 位为重量值十万位的 BCD 码。
    :param data:
    :return:
    """
    if not data:
        return ErrorCode.NOT_DATA_ERROR
    if 5 != len(data):
        return ErrorCode.DATA_LENGTH_ERROR
    if 0xff != data[0]:
        return ErrorCode.BEGIN_ERROR
    if 0x80 & data[1] == 1:
        return ErrorCode.OVER_LOAD_ERROR
    return 0


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


def format_data_3168(data):
    """
    数据格式:
     每隔 100ms 发送一组数据.每组数据 5 帧,每帧
    数据有 11 位:1 位起始位(0),8 位数据位,2 位停止位(1)。
    第 1 帧：D0～D7······0FFH(起始标志帧)。
    第 2 帧：D0～D2······小 数点位置(0-5)。
    D4······1 表示称重值稳定,0 表示不稳定。
    D5······1 表示重量为负值,0 表示重量为正值。
    D7······1 表示超载。
    第 3 帧:D0～D3 位为重量值个位的 BCD 码。
     D4～D7 位为重量值十位的 BCD 码。
    第 4 帧 :D0～D3 位 为重量值百位的 BCD 码。
     D4～D7 位为重量值千位的 BCD 码。
    第 5 帧:D0～D3 位为重量值万位的 BCD 码。
     D4～D7 位为重量值十万位的 BCD 码。
    :param data:
    :return:
    """
    if not data:
        return 0
    ret = 0
    for item in data[-1:1:-1]:
        ret = ret * 100 + item - (item >> 4) * 6
    symbol = -1 if data[1] & 0x20 else 1
    return symbol * ret


def format_data(data):
    """
    data 的第2个字节为符号位，倒数第4个字节为小数点偏移位数（从右往左）<br>
    中间的为具体数值
    :param data:
    :return:
    """
    if not data:
        return 0
    ret = ''
    for item in data[1:-4]:
        ret = ret + chr(item)
    dot = chr(data[-4])
    if dot == '0':
        return float(ret)
    else:
        return float(ret[0:0-dot] + '.' + ret[0-dot:])


def func():
    data1 = [0x02, 0x2B, 0x30, 0x31, 0x32, 0x30, 0x30, 0x35, 0x02, 0x32, 0x46, 0x03]
    data2 = [0X02, 0x2D, 0x30, 0x31, 0x32, 0x30, 0x30, 0x35, 0x02, 0x32, 0x39, 0x03]
    data3 = [0X02, 0x2D, 0x30, 0x31, 0x32, 0x30, 0x30, 0x35, 0x00, 0x32, 0x42, 0x03]
    data4 = [0x02, 0x2b, 0x30, 0x30, 0x30, 0x30, 0x34, 0x30, 0x30, 0x31, 0x46, 0x03]
    for data in (data4,):
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
        print(format_data(data))
        print('================')


if __name__ == '__main__':
    my_serial = serial.Serial('COM5', COM_BAUD_RATE, timeout=0.5)
    if my_serial.isOpen():
        print("open success")
    else:
        print("open failed")
    while True:
        data = read_com_interface(my_serial)
        print(data)
    my_serial.close()
    # func()
    # print(get_bytes_num())
    data = [0xff, 0x11, 0x60, 0x00, 0x00]
    ret = format_data_3168(data)
    print(ret)