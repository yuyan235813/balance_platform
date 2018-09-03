#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/29 下午2:08
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import configparser


class ConfigParser:
    """
    读取配置文件信息
    """
    config_dic = {}

    @classmethod
    def get_config(cls, sector, item):
        value = None
        try:
            value = cls.config_dic[sector][item]
        except KeyError:
            cf = configparser.ConfigParser()
            cf.read('settings.ini', encoding='utf8')  #注意setting.ini配置文件的路径
            value = cf.get(sector, item)
            cls.config_dic = value
        finally:
            return value


if __name__ == '__main__':
    con = ConfigParser()
    res = con.get_config('logging', 'log_dir')
    print(res)
