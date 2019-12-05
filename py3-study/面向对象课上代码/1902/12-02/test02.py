# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/2 15:08

import time
import logging
import os


def test():
    with open('test.txt', 'a', encoding='utf8') as f:

        for i in range(100, 200):

            f.write(str(i) + '\n')
            f.flush()
            print(i)

            time.sleep(0.5)


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
        time.sleep(0.5)


if __name__ == '__main__':
    test()