# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/24 11:22



import multiprocessing            # 多进程模块
import time



tasks = ['从入门到放弃.pdf', '从删库到跑路.pdf']


def book_get(name):

    print('%s 正在下载。。。'%(name))
    time.sleep(2)


# for name in tasks:
#     book_get(name)

if __name__ == '__main__':

    for name in tasks:
        # 创建多进程对象
        t = multiprocessing.Process(target=book_get, args=(name,))
        # 可以给子进程设置名字
        t.name = name
        # 开始执行
        print(t)
        t.start()
    time.sleep(3)
    # 查看存活的子进程
    print(multiprocessing.active_children())
    pass



