#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import pypyodbc
from utils.log_utils import Logger


class OdbcUtil:
    """
    access 操作工具类
    database：数据库文件地址，如 db/demo.mdb
    """
    def __init__(self, database, pwd=''):
        """
        连接数据库
        :param database:
        :param pwd:
        """
        self._connection = None
        str = 'Driver={Microsoft Access Driver (*.mdb)};PWD=' + pwd + ";DBQ=" + database
        try:
            self._connection = pypyodbc.win_connect_mdb(str)
        except Exception as e:
            Logger.error(e)

    def update(self, sql):
        """
        更改操作
        :param sql:
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute(sql)
            self._connection.commit()
            return True
        except Exception as e:
            Logger.error(e)
            return False

    def query(self, sql, is_dict=False):
        """
        查询操作
        :param sql:
        :return:
        """
        try:
            cur = self._connection.cursor()
            cur.execute(sql)
            if is_dict:
                return [dict(zip(list(zip(*cur.description))[0], row)) for row in cur.fetchall()]
            else:
                return cur.fetchall()
        except Exception as e:
            Logger.error(e)
            return []


if __name__ == '__main__':
    odbc_util = OdbcUtil('../LocDB.mdb', pwd='abcabc')
    data = odbc_util.query('select * from Units')
    print(data)