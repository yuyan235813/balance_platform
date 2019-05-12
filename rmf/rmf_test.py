#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/9 23:27
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import ctypes

DLL_PATH = 'MyReportMachine.dll'


class MyReportMachine(object):
    """
    报表操作类
    """
    def __init__(self):
        """
        初始化
        """
        self.rmf = ctypes.WinDLL(DLL_PATH)

    def create(self, hwnd):
        """
        创建控件
        :param hwnd:
        :return:
        """
        self.rmf.argtypes = [ctypes.c_int]
        self.rmf.restype = ctypes.c_voidp
        c_hwnd = ctypes.c_int(hwnd)
        return self.rmf.MCreate(c_hwnd)

    def close(self):
        """
        关闭
        :return:
        """
        return ctypes.c_voidp(self.rmf.MClose())

    def clear_all(self):
        """
        清除所有变量与数据对象
        :return:
        """
        return ctypes.c_voidp(self.rmf.MClearAll())

    def add_data(self, name, value):
        """
        添加变量
        :param name:
        :param value:
        :return:
        """
        res = self.rmf.MAddV(
            ctypes.c_wchar_p(name),
            ctypes.c_wchar_p(value)
        )
        return ctypes.c_voidp(res)

    def print_report(self, kind, show_dialog, progress, file_name, printer):
        """
        打印报表
        :param kind:
        :param show_dialog:
        :param progress:
        :param file_name:
        :param printer:
        :return:
        """
        res = self.rmf.MPrintReport(
            ctypes.c_int(kind),
            ctypes.c_int(show_dialog),
            ctypes.c_int(progress),
            ctypes.c_wchar_p(file_name),
            ctypes.c_wchar_p(printer)
        )
        return ctypes.c_voidp(res)


if __name__ == '__main__':
    rmf = MyReportMachine()
    rmf.create(0)
    rmf.clear_all()
    rmf.add_data('name', '1')
    rmf.print_report(0, 1, 0, 'rmf/test.rmf', '')
    rmf.close()