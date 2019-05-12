#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/8 20:50
@Author  : lizhiran
@Email   : 794339312@qq.com
"""

from ctypes import WinDLL, c_int, c_bool, byref, c_wchar_p, pointer, c_char_p
import ctypes

# 一体机DLL
DLL_PATH = 'lib/ParkComm.dll'


class AIODll(object):
    """
    一体机操作类
    """
    def __init__(self):
        """
        初始化
        """
        self.dll = WinDLL(DLL_PATH)

    def open_com(self, com_number):
        """
        打开 com_number 号串口
        :param com_number:
        :return: 是否打开
        """
        self.dll.OpenCom.argtypes = [c_int]
        self.dll.OpenCom.restype = c_bool
        c_com_number = c_int(com_number)
        return bool(self.dll.OpenCom(c_com_number))

    def close_com(self):
        """
        关闭串口
        :return: 是否关闭
        """
        self.dll.CloseCom.restype = c_bool
        return bool(self.dll.CloseCom())

    def equ_check_with_time(self):
        """
        检测设备在线，并下传时间
        :return: int
        """
        self.dll.EquCheckWithTime.restype = c_int
        return int(self.dllEquCheckWithTime())

    def equ_check(self):
        """
        检测设备在线
        :return: int
        """
        self.dll.EquCheck.restype = c_int
        return int(self.EquCheck())

    def issue_card(self, car_no, valid_date, anti_back, card_type, is_use):
        """
        发行卡片
        注意：临时卡进出场写卡，入场有效日期写yydd-hh-nn，yy为年，dd为日期，hh为小时，nn为分钟
        :param car_no:卡号 16进制8个字符
        :param valid_date:有效日期 yyyy-mm-dd
        :param anti_back:是否反潜回限制
        :param card_type:卡片类型 1月卡2临时卡3免费卡
        :param is_use:是否授权
        :return:int
        """
        self.dll.IssueCard.argtypes = [c_wchar_p, c_wchar_p, c_bool, c_int, c_bool]
        self.dll.IssueCard.restype = c_int
        c_car_no = c_wchar_p(car_no)
        c_valid_date = c_wchar_p(valid_date)
        c_anti_back = c_bool(anti_back)
        c_card_type = c_int(card_type)
        c_is_use = c_bool(is_use)
        res = self.dll.IssueCard(c_car_no, c_valid_date, c_anti_back, c_card_type, c_is_use)
        return c_int(res)

    def set_card_grant(self, card_no, in_grant, out_grant):
        """
        写卡片出入口权限
        :param card_no:卡号 16进制8个字符
        :param in_grant:0000000000000000 16个0或1 对应 0-15入口
        :param out_grant:0000000000000000 16个0或1  对应16-31出口
        :return:int
        """
        self.dll.SetCardGrant.argtypes = [c_wchar_p, c_wchar_p, c_wchar_p]
        self.dll.SetCardGrant.restype = c_int
        c_card_no = c_wchar_p(card_no)
        c_in_grant = c_wchar_p(in_grant)
        c_out_grant = c_wchar_p(out_grant)
        return int(self.dll.SetCardGrant(c_card_no, c_in_grant, c_out_grant))


    def read_user_card(self):
        c_card_no_ref = ctypes.create_string_buffer(8)
        c_card_type_ref = ctypes.create_string_buffer(1)
        c_valid_date_ref = ctypes.create_string_buffer(16)
        c_is_use_ref = ctypes.byref(ctypes.c_bool)
        c_anti_back_ref = ctypes.byref(ctypes.c_bool)
        res = self.dll.ReadUserCard(c_card_no_ref, c_card_type_ref, c_valid_date_ref, c_is_use_ref, c_anti_back_ref)
        print(c_card_no_ref.value)
        print(c_card_type_ref.value)
        print(c_valid_date_ref.value)
        print(c_is_use_ref.value)
        print(c_anti_back_ref.value)
        print(res)

    def read_user_card(self, card_no_ref, card_type_ref, valid_date_ref, is_use_ref, anti_back_ref):
        """
        读取用户卡
        :param card_no_ref:卡号 8位16进制字符
        :param card_type_ref:卡片类型 1月卡2临时卡3免费卡
        :param valid_date_ref:>有效期  yyyy-mm-dd
        :param is_use_ref:是否授权
        :param anti_back_ref:是否限制反潜回
        :return:int
        """
        c_card_no_ref = byref(c_char_p(bytes(card_no_ref)))
        c_card_type_ref = byref(c_char_p(bytes(card_type_ref)))
        c_valid_date_ref = byref(c_char_p(bytes(valid_date_ref)))
        c_is_use_ref = byref(c_bool(is_use_ref))
        c_anti_back_ref = byref(c_bool(anti_back_ref))
        res = self.dll.ReadUserCard(c_card_no_ref, c_card_type_ref, c_valid_date_ref, c_is_use_ref, c_anti_back_ref)
        return int(res)

    def manager_time(self, date_time):
        """
        管理卡校时
        :param date_time:校时时间 yyyy-mm-dd hh:nn:ss
        :return:int
        """
        c_date_time = ctypes.c_wchar_p(date_time)
        return c_int(self.dll.ManagerTime(c_date_time))

    def manager_set_pos(self, pos_id, pos_type, in_out_type):
        """
        管理卡设置机号
        :param pos_id:机号 0~15对应入口的1~16号进，16~31对应出口的1~16号出
        :param pos_type:大小场 1：大车场；2：小车场
        :param in_out_type:进出类型 1：进口  0： 出口
        :return:
        """
        c_pos_id = ctypes.c_int(pos_id)
        c_pos_type = ctypes.c_int(pos_type)
        c_in_out_type = ctypes.c_int(in_out_type)
        res = self.dll.ManagerSetPos(c_pos_id, c_pos_type, c_in_out_type)
        return ctypes.c_int(res)

    def manager_lost(self, car_no, lost_type):
        """
        管理卡挂失解挂
        :param car_no:卡号
        :param lost_type:操作类型 0：挂失；1：解挂
        :return:
        """
        c_car_no = ctypes.c_wchar_p(car_no)
        c_lost_type = ctypes.c_int(lost_type)
        res = self.dll.ManagerLost(c_car_no, c_lost_type)
        return ctypes.c_int(res)

    def read_equ_date_time(self, date_time):
        """
        读取设备时间
        :param date_time:设备时间 yyyy-mm-dd hh:nn:ss
        :return:
        """
        c_date_time = pointer(ctypes.c_wchar_p(date_time))
        return self.dll.ReadEquDateTime(c_date_time)



if __name__ == '__main__':
    # dll = AIODll()
    # print(dll.open_com(2))
    ss = ctypes.c_wchar_p('2019-05-11 13:43:50')
    print(ss.value)