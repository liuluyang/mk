# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/25 13:07


"""
周考
"""


"""
第一题：
计算机的组成
"""


"""
第二题：
谈谈对于并发和并行的理解以及计算机是如何实现的
"""


"""
第三题：
进程是什么，谈谈对于单进程和多进程的理解
"""


"""
第四题：
进程对象的start/join/name/daemon等方法或属性的作用是什么
"""


"""
第五题：
写一个多进程应用的案列代码
"""


"""
第六题：
把一个给定的字符串res，处理成字符串r的样子
res = 'aabcdda'
r = 'a2b1c1d2a1'
"""
def func_06():

    res = 'aabcdda'

    lst = []

    for s in res:
        if not lst or lst[-1][0] != s:
            lst.append([s, 1])
        else:
            lst[-1][-1] += 1

    r = ''
    for per in lst:
        r += per[0] + str(per[1])

    return r

# print(func_06())


"""
第七题：
写个多进程程序，来处理下面的菜单menu,user_time是每道菜处理所需的时间，
但是只有两个厨师，所以同一时刻只能有两个进程在同时进行。
user_time = {'宫保鸡丁':4, '鱼香肉丝':4, '红烧肉':5, '烧茄子':3, '干煸豆角':3, '尖椒鸡蛋':2}
menu = ['宫保鸡丁', '宫保鸡丁', '鱼香肉丝', '红烧肉', '红烧肉',
        '烧茄子', '烧茄子', '干煸豆角', '尖椒鸡蛋']

def cook(name, usertime):

    import time
    print('%s正在做。。。'%(name))
    time.sleep(usertime)
    print('%s完成'% (name))
    
"""


"""
第八题：
from multiprocessing import Process
import time
import random


def task(n):

    time.sleep(random.randint(1,3))
    print('-------->%s' %n)


if __name__ == '__main__':

    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))


    p1.start()
    p2.start()
    p3.start()

    print('-------->4')


效果一：保证最先输出-------->4
-------->4
-------->1
-------->3
-------->2
效果二：保证最后输出-------->4
-------->2
-------->3
-------->1
-------->4
效果三：保证按顺序输出
-------->1
-------->2
-------->3
-------->4
效果四：保证只输出-------->4
-------->4
"""