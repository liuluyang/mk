# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/31 16:08



from threading import Thread, Event, Timer
import time

# 事件对象
event = Event()


signal = False

def is_wait():

    while True:
        if signal == True:
            return signal

# # 返回状态 默认是False
# print(event.isSet())
# event.set()
#
# # 清除状态 改为默认False
# event.clear()
# print(event.wait())
# # 设置状态 为True
# event.set()
#
# print(event.isSet())


def task(n):

    print('等待执行任务。。。', n)
    if event.wait():
        print('正在进行。。。', n)


if __name__ == '__main__':

    for i in range(10):
        t = Thread(target=task, args=(i,))
        t.start()

    time.sleep(3)
    event.set()
    # signal = True
    pass


