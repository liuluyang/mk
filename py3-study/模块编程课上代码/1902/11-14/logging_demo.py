

import logging
import os


"""
日志模块：
    记录程序执行的一些信息（正常或者错误信息）
    
    级别：level
        ERROR = 40
        WARNING = 30
        INFO = 20
        DEBUG = 10

        error > warning > info > debug
        错误    警告      信息    调试
        
    内容格式：
        '%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s'


"""
# logging.basicConfig(filename='test.txt', level=logging.INFO,
#                     format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s')
#
# logging.info('hello')
# logging.warning('warning')
# logging.error('error')


#######################################################


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


logger = getlogger()
# print(logger)

# 记录调试信息
# logger.debug('调试信息')

# 记录正常信息
name = 'xiaolv'
passwd = 'xx'
if name == 'xiaolv' and passwd == 'xx':
    logger.info('%s登陆成功'%(name))

# 记录错误信息
# try:
#     1 + '1'
# except Exception as e:
#     logger.error(str(e))


