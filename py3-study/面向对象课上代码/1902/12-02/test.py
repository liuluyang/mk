# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/2 15:08

import time
import logging
import os


def test():
    with open('test.txt', 'a', encoding='utf8') as f:

        for i in range(100):

            f.write(str(i) + '\n')
            f.flush()
            print(i)

            time.sleep(1)


def getlogger(file_name='test.log'):

    base_path = os.path.dirname(__file__)
    path = os.path.join(base_path, file_name)            # 日志文件路径


    logger = logging.getLogger(file_name)                 #  实例化logger
    logger.setLevel(logging.DEBUG)                        #  设置日志级别


    filehandler = logging.FileHandler(path, 'a', encoding='utf8')   # 日志文件信息


    # 日志文件信息格式化输出
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")


    filehandler.setFormatter(formatter)        # 日志文件和格式化 组合

    logger.addHandler(filehandler)

    return logger

def test_log():
    log = getlogger()

    for i in range(100):
        log.error(str(i))
        time.sleep(1)


import sys

# lam = lambda : sys._getframe(1)

class F:
    def function(self):
        print(sys._getframe().f_code.co_filename)  # 当前位置所在的文件名
        print(sys._getframe().f_code.co_name)  # 当前位置所在的函数名
        # print(lam().f_lineno)  # 当前位置所在的行号
        print(sys._getframe(1).f_lineno)


if __name__ == '__main__':
    pass
    # test()
    # test_log()
    def t():

        f = F()
        f.function()
        import traceback

        try:
            1 + 'a'
        except Exception as e:
            print(type(e))
            # 获取更加详细的异常信息
            exc = traceback.format_exc()
            print(type(exc))


    t()
