# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/31 14:14




from threading import Thread, Lock, RLock
import time, random

lock = Lock()
lock02 = Lock()
num = 0

def task(n):

    # time.sleep(random.randint(1, 3))
    # lock.acquire()
    global num
    time.sleep(random.random())
    num += 1
    print('---------->', n)
    # lock.release()


if __name__ == '__main__':


    # t1 = Thread(target=task, args=(1,))
    # # t1.daemon = True
    # t2 = Thread(target=task, args=(2,))
    # # t2.daemon = True
    # t3 = Thread(target=task, args=(3,))
    # # t3.daemon = True
    #
    # t1.start()
    # t2.start()
    # t3.start()

    for i in range(100):
        t = Thread(target=task, args=(i,))
        t.start()

    # t1.join()
    # t2.join()
    # t3.join()

    time.sleep(5)
    print('结果：', num)
    # 主线程代码执行完毕 并不代表主线程结束
    # 其他非守护线程全部执行完毕 主线程才会结束
    print('代码执行完毕')
    print('---------->', 4)
























