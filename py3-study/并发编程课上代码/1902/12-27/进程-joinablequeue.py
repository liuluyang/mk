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

    # 阻塞  等待管道数据处理完毕
    q.join()

# 处理数据
def task_process(q):

    while True:
        n= q.get()
        print('拿到的数据：', n)

        # 表示一个数据处理完毕
        q.task_done()
        # if n == '完成':
        #     break
    pass


if __name__ == '__main__':

    task_all = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # q = Queue()
    q = JoinableQueue()
    obj_all = []
    for lst in task_all:
        t = Process(target=task, args=(lst, q))
        obj_all.append(t)
        t.start()


    # 处理数据
    t1 = Process(target=task_process, args=(q,))
    t1.daemon = True
    t1.start()

    t2 = Process(target=task_process, args=(q,))
    t2.daemon = True
    t2.start()

    # 等待队列数据处理完毕
    for t_obj in obj_all:
        t_obj.join()

    # 告诉处理程序 看到这个信号 可以结束了
    # q.put('完成')
    # q.put('完成')
    # q.put('完成')

    # 能执行到这里说明 队列已经空了
    print(1111111111111111111111111)












