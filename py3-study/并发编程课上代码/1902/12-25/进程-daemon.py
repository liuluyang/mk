# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/24 11:22


import multiprocessing            # 多进程模块
import time


tasks = ['从入门到放弃.pdf', '从删库到跑路.pdf']


def book_get(name, period=2):

    start = time.time()
    print('%s 正在下载。。。'%(name))
    time.sleep(period)
    print('%s 下载成功。。。'%(name), time.time() - start)


if __name__ == '__main__':

    t1 = multiprocessing.Process(target=book_get, args=(tasks[0], 1))

    # 是否开启守护进程 在start之前设置
    # 主进程结束 子进程随之结束
    # print(t1.daemon)
    t1.daemon = True
    t1.start()

    t2 = multiprocessing.Process(target=book_get, args=(tasks[1],))
    # t2.daemon = True
    t2.start()

    # time.sleep(0.5)

    print('主进程代码结束， 开始数据处理')
    # raise


# 子进程结束    2
# 主进程代码结束  1
# 主程序结束    3




