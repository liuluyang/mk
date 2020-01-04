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
    # 主进程

    t_list = []
    for name in tasks:
        t = multiprocessing.Process(target=book_get, args=(name,), kwargs={'period':1})
        # 命名进程的别名
        t_list.append(t)
        t.name = name
        # print(t, t.name)
        t.start()

    print('存活的进程：', multiprocessing.active_children())

    time.sleep(2)
    # for i in t_list:
    #     # 查看进程的是否结束
    #     print(i.name, i.is_alive())
    # 查看cpu个数
    # print('cpu个数：', multiprocessing.cpu_count())

    print('存活的进程：', multiprocessing.active_children())
    print('主进程代码结束')






