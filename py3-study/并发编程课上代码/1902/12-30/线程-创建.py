# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/30 14:56




from multiprocessing import Process
# 线程模块
from threading import Thread
import threading
import time
import random
import os


num = 1

def task(n):

    global num
    num += 1
    # time.sleep(random.randint(1, 3))
    # print('-------->%s' %n, threading.currentThread(), os.getpid())
    print('-------->%s' % n)
    # print('-------->%s' % n, os.getpid())


if __name__ == '__main__':

    # 获取当前线程对象
    # print(os.getpid())
    print(threading.currentThread())   # 主线程
    p1=Thread(target=task,args=(1,))
    p2=Thread(target=task,args=(2,))
    p3=Thread(target=task,args=(3,))


    # p1 = Process(target=task, args=(1,))
    # p2 = Process(target=task, args=(2,))
    # p3 = Process(target=task, args=(3,))

    p1.start()
    print(threading.enumerate(), 111111111)
    p2.start()
    print(threading.enumerate(), 2222222)
    p3.start()
    print(threading.enumerate(), 3333333)

    time.sleep(2)
    print('-------->4')
    print(num)

"""
进程和线程的区别：
    1.优点
    创建、启动进程的开销大
    创建、启动线程的开销小
    
    2.
    线程之间全局变量数据共享
    
    3.缺点
    多个线程只能共用一个cpu =>(跟python的解释器Cpython有关)
    
    多进程：
        计算密集型任务
    多线程：
        I/O密集型
        
    
"""