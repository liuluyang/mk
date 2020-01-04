# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/26 10:49



import multiprocessing
from multiprocessing import Process, Queue, JoinableQueue
import time
import random

"""
Queue:
    实现进程之间的数据共享
    
q = Queue()
q.put()  # 放数据
q.get()  # 拿数据
"""


# 提供数据
def task(lst, q):

    for i in lst:
        time.sleep(random.random())
        num = i * 10
        q.put(num)
    q.put('完成')


if __name__ == '__main__':

    task_all = [[1, 2, 3], [4, 5, 6]]
    q = Queue()
    for lst in task_all:
        t = Process(target=task, args=(lst, q))
        t.start()

    # 处理数据
    count = 0
    while True:
        try:
            n = q.get(timeout=1)
            print('拿到的数据：', n)
        except:
            print('超时')
            if not multiprocessing.active_children():
                break

        # if n == '完成':
        #     count += 1
        #     if count == 2:
        #         break












