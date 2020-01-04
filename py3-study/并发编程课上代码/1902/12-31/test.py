# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/31 13:49


import threading
import time,random

event = threading.Event()
#set为绿灯，clear为红灯
def light():
    count = 0
    if not event.isSet():
        event.set()#设置初始状态为绿灯
    while True:
        if count <10:
            #绿灯
            print('\033[1;42;1m绿灯-可以通行 %s\033[0m'%count)
            event.set()
        elif count <13:
            #黄灯
            print('\033[1;43;1m黄灯 %s\033[0m' % count)

        elif count <25:
            #红灯
            print('\033[1;41;1m红灯-禁止通行 %s\033[0m' % count)
            event.clear()
        else:
            count = 0
            event.set()
        count +=1
        time.sleep(1)

def car(n):
    while True:
        time.sleep(1)#random.randrange(3)
        if event.isSet():#绿灯状态
            print('car[%s] is running...'%str(n))
            #event.wait()
        else:
            print('car[%s] is waitting ...'%str(n))
            event.wait()#阻塞等待标志位被设定

def main():
    t_light = threading.Thread(target=light)
    t_light.start()
    for i in range(3):
        t_car = threading.Thread(target=car,args=(i,))
        t_car.start()

main()