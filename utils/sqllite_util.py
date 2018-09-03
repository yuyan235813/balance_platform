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

    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def execute(self, sql, args=[], result_dict=True, commit=True) -> list:
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
            self._connection.row_factory = self._dict_factory
        else:
            self._connection.row_factory = None
        # 获取游标
        data = None
        _cursor = self._connection.cursor()
        # 执行SQL获取结果
        try:
            _cursor.execute(sql, args)
            if commit:
                self._connection.commit()
            data = _cursor.fetchall()
        except Exception as e:
            logger.error(traceback.format_exc())
        finally:
            _cursor.close()
        return data


if __name__ == '__main__':
    db = EasySqlite('../db/browser.db')
    # print(db.execute("select name from sqlite_master where type=?", ['table']))
    # print(db.execute("pragma table_info([user])"))
    print(db.execute("insert into user(id, name, password) values (?, ?, ?)", [3, "李五", "123456"]))
    print(db.execute("select id, name userName, password pwd from user"))
    print(db.execute("select * from user", result_dict=False, commit=False))
    data = db.execute("select * from user")
    print(data)
