#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/27 下午3:48
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import os
import datetime
from utils.sqllite_util import EasySqlite
from PyQt5.QtWidgets import QMessageBox


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


def get_cur_time():
    """
    获取当前时间
    :return:
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def generate_balance_id():
    """
    获取当前时间
    :return:
    """
    cur_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    week = datetime.datetime.now().weekday()
    balance_id = cur_time + '0' + str(week)
    return balance_id


def get_user_permission(user_id):
    """
    获取用户的权限
    :param user_id:
    :return:
    """
    db = EasySqlite(r'rmf/db/balance.db')
    sql_tmp = """
        select 
            user_id,
            opt_type,
            opt_name,
            opt_code
        from 
            (
                select
                    user_id, 
                    role_id 
                from 
                    t_user 
                where 
                    user_id = '%s'
            )t1 
            join
            (
                select 
                    a.object_id,
                    a.object_type,
                    b.opt_type,
                    b.opt_name, 
                    b.opt_code
                from 
                    t_permission a 
                    join 
                    t_operation b on a.operation_id=b.id 
                where 
                    a.status=1 
                    and b.status=1
            )t2 on (t1.user_id=t2.object_id or t1.role_id=t2.object_id);"""
    sql = sql_tmp % user_id
    ret = db.query(sql)
    print(ret)
    opt_list = []
    for item in ret:
        opt_list.append(item.get('opt_code'))
    return opt_list


def has_permission(user_id, operation):
    def base_has_permission(func):
        def wrapper(*args, **kw):
            print('user_id=%s, operation=%s' % (user_id, operation))
            print('pre')
            opt_list = get_user_permission(user_id)
            if operation in opt_list:
                output = func(*args, **kw)
            else:
                print(args[0])
                QMessageBox.warning(args[0], '本程序', "没有权限！", QMessageBox.Ok)
                return
            print('post')
            return output
        return wrapper
    return base_has_permission


@has_permission('admin', 'system_params_form1')
def test_fun(text):
    print('我就是我，不一样的烟火 %s' % text)


if __name__ == '__main__':
    # print(get_file_list(r'H:\workspace\python3\balance_platform\rmf\rmf'))
    # print(generate_balance_id())
    test_fun('tttt')