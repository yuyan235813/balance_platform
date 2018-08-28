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
            print('%s [INFO] %s: %s' % (current_time, file_name, msg), file=config.LOGGER_DIR)
        else:
            with open(config.LOGGER_DIR, 'a+') as f:
                f.write('%s [INFO] %s: %s\n' % (current_time, file_name, msg))

    @staticmethod
    def debug(msg):
        tb = traceback.extract_stack()
        file_name = os.path.basename(tb[-2][0])
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if config.LOGGER_DIR == sys.stdout:
            print('%s [DEBUG] %s: %s' % (current_time, file_name, msg), file=config.LOGGER_DIR)
        else:
            with open(config.LOGGER_DIR, 'a+') as f:
                f.write('%s [DEBUG] %s: %s\n' % (current_time, file_name, msg))

    @staticmethod
    def error(msg):
        tb = traceback.extract_stack()
        file_name = os.path.basename(tb[-2][0])
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if config.LOGGER_DIR == sys.stdout:
            print('%s [ERROR] %s: %s' % (current_time, file_name, msg), file=config.LOGGER_DIR)
        else:
            with open(config.LOGGER_DIR, 'a+') as f:
                f.write('%s [ERROR] %s: %s\n' % (current_time, file_name, msg))


if __name__ == '__main__':
    Logger.info('test')
    Logger.debug('test')
    Logger.error('test')