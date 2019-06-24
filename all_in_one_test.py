#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019/5/8 20:50
@Author  : lizhiran
@Email   : 794339312@qq.com
**********************
ER_Suc: integer = 0;             //执行成功
ER_NoReturn: integer = 2;        //无返回值
ER_SumErr: integer = 3;          //校验和错误
ER_TimeOut: integer = 4;         //超时
ER_ErrData: integer = 5;         //无效数据
ER_NoData: integer = 6;          //无返回数据
ER_OtherData: integer = 7;       //其它数据
ER_ErrDateTime: integer = 8;         //无效日期时间
ER_UserStop: integer = 9;        //用户终止
ER_EquInUse: Integer = 100;       //设备占用
ER_EquNotAvailable: Integer = 101;  //设备找不到
ER_EquExcept: integer = 102; //设备通讯异常
ER_EquTypeInUse: Integer = 103;       //设备类型在使用

ER_NoObject: Integer = 200;       //soyal没有创建
ER_ComClose: Integer = 201;       //串口没打开
ER_OhterExcept: Integer = 202;       //未知异常
***********************
"""
import ctypes
from ctypes import pointer

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
        try:
            self.dll = ctypes.WinDLL(DLL_PATH)
            self.status = True
        except Exception as e:
            self.status = False
            print(e)

    def open_com(self, com_number):
        """
        打开 com_number 号串口
        :param com_number:
        :return: 是否打开
        """
        self.dll.OpenCom.argtypes = [ctypes.c_int]
        self.dll.OpenCom.restype = ctypes.c_bool
        c_com_number = ctypes.c_int(com_number)
        return bool(self.dll.OpenCom(c_com_number))

    def close_com(self):
        """
        关闭串口
        :return: 是否关闭
        """
        self.dll.CloseCom.restype = ctypes.c_bool
        return bool(self.dll.CloseCom())

    def equ_check_with_time(self):
        """
        检测设备在线，并下传时间
        :return: int
        """
        self.dll.EquCheckWithTime.restype = ctypes.c_int
        return int(self.dllEquCheckWithTime())

    def equ_check(self):
        """
        检测设备在线
        :return: int
        """
        self.dll.EquCheck.restype = ctypes.c_int
        return int(self.EquCheck())

    def issue_card(self, card_no, valid_date, anti_back, card_type, is_use):
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
        card_no = self.card_no_to_hex(card_no)
        c_car_no = ctypes.c_char_p(card_no.encode("utf-8"))
        c_valid_date = ctypes.c_char_p(valid_date.encode("utf-8"))
        c_anti_back = ctypes.c_bool(anti_back)
        c_card_type = ctypes.c_int(card_type)
        c_is_use = ctypes.c_bool(is_use)
        res = self.dll.IssueCard(c_car_no, c_valid_date, c_anti_back, c_card_type, c_is_use)
        return int(res)

    def set_card_grant(self, card_no, in_grant, out_grant):
        """
        写卡片出入口权限
        :param card_no:卡号 16进制8个字符
        :param in_grant:0000000000000000 16个0或1 对应 0-15入口
        :param out_grant:0000000000000000 16个0或1  对应16-31出口
        :return:int
        """
        card_no = self.card_no_to_hex(card_no)
        self.dll.SetCardGrant.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        self.dll.SetCardGrant.restype = ctypes.c_int
        c_card_no = ctypes.c_char_p(card_no)
        c_in_grant = ctypes.c_char_p(in_grant)
        c_out_grant = ctypes.c_char_p(out_grant)
        return int(self.dll.SetCardGrant(c_card_no, c_in_grant, c_out_grant))

    def read_user_card(self, data: dict):
        """
        读取用户卡片
        :param data:
            card_no_ref:卡号 8位16进制字符
            card_type_ref:卡片类型 1月卡2临时卡3免费卡
            valid_date_ref:>有效期  yyyy-mm-dd
            is_use_ref:是否授权
            anti_back_ref:是否限制反潜回
        :return: int
        """
        c_card_no_ref = ctypes.c_char_p()
        c_card_type_ref = ctypes.c_int()
        c_valid_date_ref = ctypes.c_char_p()
        c_is_use_ref = ctypes.c_bool()
        c_anti_back_ref = ctypes.c_bool()
        res = self.dll.ReadUserCard(pointer(c_card_no_ref), pointer(c_card_type_ref), pointer(c_valid_date_ref), pointer(c_is_use_ref), pointer(c_anti_back_ref))
        if int(res) == 0:
            data['card_no'] = eval('0x' + c_card_no_ref.value.decode('utf-8'))
            data['card_type'] = c_card_type_ref.value
            data['valid_date'] = c_valid_date_ref.value.decode('utf-8')
            data['is_use'] = c_is_use_ref.value
            data['anti_back'] = c_anti_back_ref.value
        return int(res)

    def manager_time(self, date_time):
        """
        管理卡校时
        :param date_time:校时时间 yyyy-mm-dd hh:nn:ss
        :return:int
        """
        c_date_time = ctypes.c_char_p(date_time.encode("utf-8"))
        res = self.dll.ManagerTime(c_date_time)
        return int(res)

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
        return int(res)

    def manager_lost(self, card_no, lost_type):
        """
        管理卡挂失解挂
        :param car_no:卡号
        :param lost_type:操作类型 0：挂失；1：解挂
        :return:
        """
        card_no = self.card_no_to_hex(card_no)
        c_car_no = ctypes.c_char_p(card_no)
        c_lost_type = ctypes.c_int(lost_type)
        res = self.dll.ManagerLost(c_car_no, c_lost_type)
        return int(res)

    def read_equ_date_time(self, data: dict):
        """
        读取设备时间
        :param data
            date_time:设备时间 yyyy-mm-dd hh:nn:ss
        :return:
        """
        c_date_time = ctypes.c_char_p()
        res = self.dll.ReadEquDateTime(pointer(c_date_time))
        if int(res) == 0:
            data['date_time'] = c_date_time.value.decode('utf-8')
        return int(res)

    def multi_psw(self):
        """
        开始批量加密
        操作流程：
        A、执行时需要执行MultiPsw  3遍，间隔200ms；
        B、然后循环执行（读取结果GetComResult，清除结果EmptyComData）；
        C、最后执行 MultiStop终止批量操作；
        :return:
        """
        res = self.dll.MultiPsw()
        return int(res)

    def clear_psw(self):
        """
        开始批量清除密码
        操作流程：
        A、执行时需要执行ClearPsw  3遍，间隔200ms；
        B、然后循环执行（读取结果GetComResult，清除结果EmptyComData）；
        C、最后执行 MultiStop终止批量操作；
        :return:
        """
        res = self.dll.ClearPsw()
        return int(res)

    def multi_stop(self):
        """
        批量操作停止
        :return:
        """
        res = self.dll.MultiStop()
        return int(res)

    def get_com_result(self):
        """
        批量结果读取
        :return:
        """
        res = self.dll.GetComResult()
        return int(res)

    def empty_com_data(self):
        """
        批量结果清除
        :return:
        """
        res = self.dll.EmptyComData()
        return int(res)

    def set_psw(self, password):
        """
        下发密码到发卡器
        :param password 密码 6个字节 16进制的12个字符
        :return:
        """
        c_password = ctypes.c_char_p(password)
        res = self.dll.SetPsw(c_password)
        return int(res)

    def manager_delay_card(self, card_no, valid_date):
        """
        制作无卡延期用的管理卡
        :param card_no: 要延期的卡片号码 16进制8位字符
        :param valid_date: 延期卡片的新有效期 yyyy-mm-dd
        :return:
        """
        card_no = self.card_no_to_hex(card_no)
        c_card_no = ctypes.c_char_p(card_no)
        c_valid_date = ctypes.c_char_p(valid_date)
        res = self.dll.ManagerDelayCard(c_card_no, c_valid_date)
        return int(res)

    def set_tmp_card(self, card_no, start_date_time):
        """
        临时卡发卡
        :param card_no:卡片号码 16进制8位字符
        :param start_date_time:入场时间 yyyy-mm-dd hh:nn:ss
        :return:
        """
        card_no = self.card_no_to_hex(card_no)
        c_card_no = ctypes.c_char_p(card_no.encode("utf-8"))
        c_start_date_time = ctypes.c_char_p(start_date_time.encode("utf-8"))
        res = self.dll.SetTmpCard(c_card_no, c_start_date_time)
        return int(res)

    def open_pos(self, pos_id, pos_type, in_out_type):
        """
        临时卡发卡后，开闸命令
        :param pos_id:车场编号 0-31
        :param pos_type:大小场 1：大车场；2：小车场
        :param in_out_type:进出类型 1：进口  0： 出口
        :return:
        """
        c_pos_id = ctypes.c_int(pos_id)
        c_pos_type = ctypes.c_int(pos_type)
        c_in_out_type = ctypes.c_int(in_out_type)
        res = self.dll.OpenPos(c_pos_id, c_pos_type, c_in_out_type)
        return int(res)

    @staticmethod
    def card_no_to_hex(card_no):
        """
        转化十进制卡号到8位16进制字符
        :param card_no:
        :return:
        """
        card_no = int(card_no)
        card_no_hex = hex(card_no).strip('0x')
        zero_str = ''
        for i in range(8 - len(card_no_hex)):
            zero_str += '0'
        card_no_hex = zero_str + str(card_no_hex)
        return card_no_hex.upper()


if __name__ == '__main__':
    dll = AIODll()
    res = dll.open_com(3)
    print(res)
    # while True:
    #     data = dict()
    #     dll.read_user_card(data)
    #     for k, v in data.items():
    #         print("%s = %s" % (k, v))
    #     print("======================================")
    # time_now = "2019-06-19 21:00:01"
    # res = dll.manager_time(time_now)
    # print(res)
    # card_no = "12345677"
    # valid_date = '2019-07-19'
    # anti_back = False
    # card_type = 2
    # is_use = True
    # res = dll.issue_card(card_no, valid_date, anti_back, card_type, is_use)
    # print(res)
    # res = dll.empty_com_data()
    # print(res)
    # res = dll.set_tmp_card(card_no, time_now)
    # print(res)
    res = dll.open_pos(1, 2, 1)
    print(res)