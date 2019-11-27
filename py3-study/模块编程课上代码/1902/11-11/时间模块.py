

import time


"""
date 日期
time 
"""

"""
timestamp 时间戳
"""
# 获取当前时间的时间戳
timestamp_now = time.time()
# print(timestamp_now, type(timestamp_now))


"""
struct_time 九元组
year
month
day
hour
minute
second
"""
# 返回本地时间
struct_time = time.localtime()
# print(struct_time)
struct_time_02 = time.gmtime()
# print(struct_time_02)


"""
字符串时间
"""
# print('2019-11-11 11:12:11')


"""
时间类型之间的转换
"""
# 时间戳 => 九元组
# print(time.localtime(123213))
# print(time.localtime(time.time()))
# print(time.localtime())


# 九元组 => 时间戳
# print(time.mktime(time.localtime()))


# 九元组 => 字符串 #######################**
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(132123123)))
# print(time.strftime('%Y-%m-%d %X', time.localtime()))


# 字符串 => 九元组
# print(time.strptime('2019-11-11 11:42:30', '%Y-%m-%d %H:%M:%S'))


# 字符串 => 时间戳 ######################**
# print(time.mktime(time.strptime('2019-11-11 11:49:30', '%Y-%m-%d %H:%M:%S')))
# print(time.mktime(time.strptime('2019-11-11 0:0:0', '%Y-%m-%d %H:%M:%S')))


###################################  其他转换方法
# print(time.ctime(time.time()))
# print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))


###################################


