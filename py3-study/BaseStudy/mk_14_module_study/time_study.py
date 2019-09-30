import time, datetime

"""
time模块学习
"""

"""
时间戳timestamp
表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
"""
timestamp = time.time()
# print(timestamp)

"""
struct_time（元组时间）
time.struct_time(tm_year=2019, tm_mon=7, tm_mday=13, 
                    tm_hour=9, tm_min=3, tm_sec=42, 
                    tm_wday=5, tm_yday=194, tm_isdst=0
                    )
注：tm_wday代表周几 0-6 代表周一至周日
"""
struct_time = time.localtime()
struct_gmtime = time.gmtime()
# print(struct_time)
# print(struct_gmtime)
# print(struct_time.tm_wday)

# 反转
# print(time.mktime(time.localtime()))

"""
时间格式化
"""
str_f = '%Y-%m-%d %H:%M:%S'
str_f2 = '%Y-%m-%d %X'
str_f3 = '%x %X'
# str_time = time.strftime(str_f, time.localtime())
# print(str_time)
# str_time_p = time.strptime(str_time, str_f)
# print(str_time_p)

"""
转成其他形式
"""
# print(time.asctime(time.localtime()))
# print(time.ctime())




