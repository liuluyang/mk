# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/27 8:50


"""
lst = [1, 2, 3, 4]
num = 100
"""
# lst = [1, 2, 3, 4]
# num = 30
# print(lst*(num//len(lst)) + lst[:(num%len(lst))])
# print([lst[i%(len(lst))] for i in range(num)])


import multiprocessing
import time



def task(num):

    time.sleep(20)

    print('进程%s结束'%(num))



if __name__ == '__main__':

    for i in range(100):
        t = multiprocessing.Process(target=task, args=(i,))
        t.start()