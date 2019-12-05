
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
import sys
import os


class Log:

    __level_dict = {'error':40, 'warning':30, 'info':20, 'debug':10}
    __level_dict_reverse = {v:k for k,v in __level_dict.items()}

    def __init__(self, name):

        self.__name = name
        self.__f = open(self.__name, 'a', encoding='utf8')
        self.__level = 30

    def debug(self, msg):

        func_name = sys._getframe().f_code.co_name
        self.__write_msg(msg, func_name)

    def info(self, msg):

        func_name = sys._getframe().f_code.co_name
        self.__write_msg(msg, func_name)

    def warning(self, msg):

        func_name = sys._getframe().f_code.co_name
        self.__write_msg(msg, func_name)

    def error(self, msg):

        func_name = sys._getframe().f_code.co_name
        self.__write_msg(msg, func_name)

    def __write_msg(self, msg, level):
        """
        日志内容写入
        :param msg:
        :return:
        """
        if self.__level_dict.get(level, 0) < self.__level:
            return

        if not isinstance(msg, str):
            raise TypeError('日志内容必须是字符串')

        time_now = time.strftime('%Y-%m-%d %X', time.localtime())
        file_name = sys._getframe(2).f_code.co_filename
        file_name = os.path.basename(file_name)
        func_name = sys._getframe(2).f_code.co_name
        line_num = sys._getframe(2).f_lineno
        # print(time_now, file_name, func_name, line_num)

        content = '- %s - %s - %s[line:%s] - %s:%s\n'%(
            time_now, file_name, func_name, line_num, level.upper(), msg)

        self.__f.write(content)

    def setLevel(self, level):
        """
        设置日志等级
        :param level:
        :return:
        """

        if isinstance(level, int) and self.__level_dict_reverse.get(level):
            self.__level = level
        elif isinstance(level, str) and self.__level_dict.get(level):
            self.__level = self.__level_dict.get(level)
        else:
            raise ValueError('该日志等级不存在')



if __name__ == '__main__':
    pass
    def t():
        log = Log('日志.txt')
        log.setLevel(10)
        # print(log._Log__level)
        # log.setLevel(20)
        log.debug('这是一条信息')
    t()