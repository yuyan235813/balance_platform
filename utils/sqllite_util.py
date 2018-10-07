#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/29 下午2:45
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import sqlite3
import traceback
from utils.log_utils import Logger as logger


class EasySqlite:
    """
    sqlite数据库操作工具类
    database: 数据库文件地址，例如：db/mydb.db
    """
    _connection = None

    def __init__(self, database):
        # 连接数据库
        try:
            self._connection = sqlite3.connect(database)
        except Exception as e:
            logger.error('%s 数据库连接失败！' % database)

    def __dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __execute(self, sql, args=[], result_dict=True, commit=True) -> list:
        """
        执行数据库操作的通用方法
        Args:
        sql: sql语句
        args: sql参数
        result_dict: 操作结果是否用dict格式返回
        commit: 是否提交事务
        Returns:
        list 列表，例如：
        [{'id': 1, 'name': '张三'}, {'id': 2, 'name': '李四'}]
        """
        if result_dict:
            self._connection.row_factory = self.__dict_factory
        else:
            self._connection.row_factory = None
        # 获取游标
        data = None
        _cursor = self._connection.cursor()
        # 执行SQL获取结果
        try:
            if args and (isinstance(args[0], tuple) or isinstance(args[0], list)):
                _cursor.executemany(sql, args)
            else:
                _cursor.execute(sql, args)
            if commit:
                self._connection.commit()
            data = _cursor.fetchall()
        except Exception as e:
            logger.error(traceback.format_exc())
        finally:
            _cursor.close()
        return data

    def query(self, sql, args=[], result_dict=True) -> list:
        """
        查询数据
        :param sql:
        :param args:
        :param result_dict:
        :return:
        """
        return self.__execute(sql, args, result_dict)

    def update(self, sql, args=[], result_dict=True) -> int:
        """
        查询数据
        :param sql:
        :param args:
        :param result_dict:
        :return:
        """
        ret = self.__execute(sql, args, result_dict)
        print(ret)
        if ret:
            return 0
        else:
            return 1


if __name__ == '__main__':
    db = EasySqlite('../rmf/db/balance.db')
    ret = db.update('replace into t_data_bit_conf(data_bit) values(?)', args=[[-1], [-2]])
