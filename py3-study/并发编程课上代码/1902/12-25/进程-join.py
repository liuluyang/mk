# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/24 11:22


import multiprocessing            # 多进程模块
import time


tasks = ['从入门到放弃.pdf', '从删库到跑路.pdf']
num = 0
"""
进程之间数据不共享，进程之间不受影响，内存隔离
"""

def book_get(name, period=2):

    global num

    num = period

    start = time.time()
    print('%s 正在下载。。。'%(name), num)
    time.sleep(period)
    # 断言
    # assert 1==period
    print('%s 下载成功。。。'%(name), time.time() - start)


if __name__ == '__main__':

    t1 = multiprocessing.Process(target=book_get, args=(tasks[0], 1))
    t1.start()

    t2 = multiprocessing.Process(target=book_get, args=(tasks[1],))
    t2.start()

    # t1.join()
    # t2.join()


    # while True:
    #     if not multiprocessing.active_children():
    #         break
    #     time.sleep(1)

    print('主进程代码结束， 开始数据处理', num)






