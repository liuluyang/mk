# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/31 14:14




from threading import Thread, Semaphore
import time, random


# 信号量
# 可以控制同一时间创建或者存活的线程的数量
sem = Semaphore(2)


def limit_num(func):

    def inner(*args, **kwargs):

        with sem:
            return func(*args, **kwargs)

    return inner


# @limit_num
def task(n):

    # sem.acquire()

    # with sem:
    time.sleep(random.randint(1, 1))
    print('---------->', n)

    # sem.release()


if __name__ == '__main__':

    for i in range(100):
        t = Thread(target=task, args=(i,))
        t.start()

    # print('---------->', 4)
























