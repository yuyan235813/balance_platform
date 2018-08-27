#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/27 下午3:48
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from utils.log_utils import Logger as logger


def stdev(sequence):
    """
    计算标准差
    :param sequence:
    :return:
    """
    if len(sequence) < 1:
        return 0
    else:
        avg = sum(sequence)/len(sequence)
        sdsq = sum([(i - avg) ** 2 for i in sequence])
        stdev = (sdsq / (len(sequence) - 1)) ** .5
        return stdev