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
    def get_item(cls, key, default_value):
        """
        根据key获取配置的value
        :param item:
        :return:
        """
        key = key.lower()
        if not cls.config_dic:
            cf = configparser.ConfigParser()
            # cf.read('../conf/settings.ini', encoding='utf8')  #注意settings.ini配置文件的路径
            cf.read('conf/settings.ini', encoding='utf8')  #注意settings.ini配置文件的路径
            for section, item in cf.items():
                for i in item:
                    cls.config_dic[i] = cf.get(section, i)
        if key in cls.config_dic.keys():
            default_value = cls.config_dic.get(key)
        return default_value

if __name__ == '__main__':
    conf = ConfigParser.get_item('debug', 1)
    conf = ConfigParser.get_item('debug', 1)
    print(conf)
