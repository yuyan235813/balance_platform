#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/27 下午4:04
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
import traceback
import os
import datetime
import sys
sys.path.append('..')
from conf import config


class Logger:
    """
    自定义日志类
    """
    @staticmethod
    def info(msg):
        tb = traceback.extract_stack()
        file_name = os.path.basename(tb[-2][0])
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if config.LOGGER_DIR == sys.stdout:
            print(u'%s [INFO] %s: %s' % (current_time, file_name, msg))
        else:
            with open(config.LOGGER_DIR, 'a+', encoding='utf-8') as f:
                f.write(u'%s [INFO] %s: %s\n' % (current_time, file_name, msg))

    @staticmethod
    def debug(msg):
        tb = traceback.extract_stack()
        file_name = os.path.basename(tb[-2][0])
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if config.LOGGER_DIR == sys.stdout:
            print(u'%s [DEBUG] %s: %s' % (current_time, file_name, msg))
        else:
            with open(config.LOGGER_DIR, 'a+', encoding='utf-8') as f:
                f.write(u'%s [DEBUG] %s: %s\n' % (current_time, file_name, msg))

    @staticmethod
    def error(msg):
        tb = traceback.extract_stack()
        file_name = os.path.basename(tb[-2][0])
        line = tb[-2][1]
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if config.LOGGER_DIR == sys.stdout:
            print(u'\033[31m%s [ERROR] %s, line %s: %s\033[0m' % (current_time, file_name, line, msg))
        else:
            with open(config.LOGGER_DIR, 'a+', encoding='utf-8') as f:
                f.write(u'%s [ERROR] %s, line %s: %s\n' % (current_time, file_nameline, msg))


if __name__ == '__main__':
    Logger.info('test')
    Logger.debug('test')
    Logger.error('test')