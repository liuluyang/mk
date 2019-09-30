import logging
import os

"""
logging模块
"""


# class MakeLogger(object):
#     def __init__(self, name='module.log'):
#         base_path = os.path.dirname(os.path.abspath(__file__))
#         path = os.path.join(base_path, name)
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.WARNING)
#         l = logging.FileHandler(path, 'a', encoding='utf8')
#         formatter = logging.Formatter(
#             "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
#         l.setFormatter(formatter)
#         self.logger.addHandler(l)
#
#
# Logger = MakeLogger().logger
#
# Logger.error('程序错误')

"""
1.日志的作用
2.简单日志打印
3.日志级别
CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
4.日志的使用
"""
def getlogger(file_name='test.log'):
    base_path = os.path.dirname(__file__)
    path = os.path.join(base_path, file_name)   # 日志文件路径
    logger = logging.getLogger(file_name)                 #  实例化logger
    logger.setLevel(logging.DEBUG)                          #  设置日志级别
    filehandler = logging.FileHandler(path, 'a', encoding='utf8') # 日志文件信息
    # 日志文件信息格式化输出
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger


# Logger = getlogger()
# Logger.debug('debug  Logger')
#
# ll = getlogger('t.log')
# ll.error('error ll')
import sys
# h = logging.FileHandler(filename='t', encoding='utf8')
# h2 = logging.FileHandler(filename='t2', encoding='utf8')
"""
stream和handlers参数不能共存
"""
# logging.basicConfig(stream=sys.stderr, handlers=[h])
# logging.basicConfig(handlers=[h, h2])
# logging.error('error的')

