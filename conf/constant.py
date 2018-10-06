#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""


class ErrorCode:
    """
    定义错误码
    """
    # 数据为空
    NOT_DATA_ERROR = 'E1001'
    # 数据起始错误
    BEGIN_ERROR = 'E1002'
    END_ERROR = 'E1003'
    HIGH_VERIFY_ERROR = 'E1004'
    LOW_VERIFY_ERROR = 'E1005'
    DATA_LENGTH_ERROR = 'E1006'


class NormalParam:
    """
    定义时间相关的常量
    """
    # 读取 COM 接口延时 ms
    COM_READ_DURATION = 10
    # 判断稳定时长 s
    STABLES_DURATION = 1
    # 判断稳定误差阀值
    STABLES_ERROR = 0
    # 检测称重仪表连接时长 s
    COM_CHECK_CONN_DURATION = 0.5
    # 检测称重仪表连接时长 s
    COM_OPEN_DURATION = 1

