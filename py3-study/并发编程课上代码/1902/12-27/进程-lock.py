# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/27 9:24



from multiprocessing import Process, Lock
import time
import random



def task(lock):

    lock.acquire()  # 加锁
    with open('data.txt', 'r', encoding='utf8') as f:
        num = int(f.read())
        num += 1
    # time.sleep(random.random())
    with open('data.txt', 'w', encoding='utf8') as f:
        f.write(str(num))
    lock.release()  # 解锁


if __name__ == '__main__':


    lock = Lock()
    for i in range(10):
        t = Process(target=task, args=(lock,))
        t.start()
        # task()
    pass

