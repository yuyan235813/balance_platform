#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/27 下午3:48
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import os


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


if __name__ == '__main__':
    print(get_file_list(r'H:\workspace\python3\balance_platform\rmf\rmf'))