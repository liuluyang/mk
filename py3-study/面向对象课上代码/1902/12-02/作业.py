





# 1、一个参数 必须是整数

r01 = range(10)
# print(list(r01))


# 2、两个参数 必须是整数

r02 = range(1, 10)
# print(list(r02))


# 3、三个参数 必须是整数

r03 = range(1, 10, 2)
# print(list(r03))


# 4、三个参数 必须是整数

r04 = range(10, 1, -2)
print(list(r04))


# 5、满足所有情况


############################################### log

import logging


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

class Log:


    pass

log = Log()


log.setLevel()

log.error()
log.debug()





