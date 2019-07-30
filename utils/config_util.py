#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/29 下午2:08
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import configparser
import chardet


class ConfigParser:
    """
    读取配置文件信息
    """
    config_dic = {}

    @classmethod
    def get_item(cls, key, default_value):
        """
        根据key获取配置的value
        :param key:
        :param default_value:
        :return:
        """
        key = key.lower()
        if not cls.config_dic:
            encoding = 'utf8'
            file_path = 'conf/settings.ini'
            with open(file=file_path, mode='rb') as f:
                data = f.read()
                ret = chardet.detect(data)
                encoding = ret.get('encoding')
            cf = configparser.ConfigParser()
            cf.read(file_path, encoding=encoding)
            for section, item in cf.items():
                for i in item:
                    cls.config_dic[i] = cf.get(section, i)
        if key in cls.config_dic.keys():
            default_value = cls.config_dic.get(key)
        return default_value


if __name__ == '__main__':
    conf = ConfigParser.get_item('DEBUG', 1)
    print(conf)
