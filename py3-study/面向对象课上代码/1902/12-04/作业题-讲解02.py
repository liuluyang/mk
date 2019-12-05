
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


logger.setLevel(logging.DEBUG)
"""
import time

class Log:

    def __init__(self, name):

        self.name = name
        self.f = open(name, 'a', encoding='utf8')

    def info(self, msg):

        msg = str(time.time()) + ' INFO:'+msg + '\n'
        self.f.write(msg)


log = Log('日志.txt')
log.info('这是一条信息')

#log.setLevel()

#log.error()
# log.debug()
