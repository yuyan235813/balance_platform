#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from config_util import ConfigParser


class ErrorCode:
    """
    定义错误码
    """
    # 数据为空
    NOT_DATA_ERROR = ConfigParser.get_item('NOT_DATA_ERROR', 'E1001')
    # 数据起始错误
    BEGIN_ERROR = ConfigParser.get_item('BEGIN_ERROR', 'E1002')
    END_ERROR = ConfigParser.get_item('END_ERROR', 'E1003')
    HIGH_VERIFY_ERROR = ConfigParser.get_item('HIGH_VERIFY_ERROR', 'E1004')
    LOW_VERIFY_ERROR = ConfigParser.get_item('LOW_VERIFY_ERROR', 'E1005')
    DATA_LENGTH_ERROR = ConfigParser.get_item('DATA_LENGTH_ERROR', 'E1006')


class NormalParam:
    """
    定义时间相关的常量
    """
    # 读取 COM 接口延时 ms
    COM_READ_DURATION = int(ConfigParser.get_item('COM_READ_DURATION', 10))
    # 判断稳定时长 s
    STABLES_DURATION = int(ConfigParser.get_item('STABLES_DURATION', 5))
    # 判断稳定误差阀值
    STABLES_ERROR = int(ConfigParser.get_item('STABLES_ERROR', 0))
    # 检测称重仪表连接时长 s
    COM_CHECK_CONN_DURATION = int(ConfigParser.get_item('COM_CHECK_CONN_DURATION', 3))
    # 检测称重仪表连接时长 s
    COM_OPEN_DURATION = int(ConfigParser.get_item('COM_OPEN_DURATION', 3))
    # 单次读取串口重试次数
    COM_RETRY_TIMES = int(ConfigParser.get_item('COM_RETRY_TIMES', 3))
    # 错误重量
    ERROR_WEIGHT = int(ConfigParser.get_item('ERROR_WEIGHT', -10000))
    # 错误卡号
    ERROR_CARD_NO = int(ConfigParser.get_item('ERROR_CARD_NO', -1))


if __name__ == '__main__':
    print(NormalParam.ERROR_CARD_NO)
