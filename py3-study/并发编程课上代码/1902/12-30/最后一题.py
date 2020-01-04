# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/30 14:56




from multiprocessing import Process
import time
import random


def task(n):

    time.sleep(random.randint(1, 3))
    print('-------->%s' %n)


if __name__ == '__main__':

    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))

    # p1.daemon = True
    p1.start()
    # p1.join()
    # p2.daemon = True
    p2.start()
    # p2.join()
    # p3.daemon = True
    p3.start()
    # p3.join()

    # p1.join()
    # p2.join()
    # p3.join()

    # time.sleep(4)

    print('-------->4')