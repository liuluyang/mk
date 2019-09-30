import threading
from threading import Thread, Lock, RLock, Semaphore
from queue import Queue
import time


"""
多线程
"""

"""
死锁现象
多个锁存在的时候
"""

mutexA=Lock()
mutexB=RLock()

def fun_01():
    mutexA.acquire()
    print('fun01 a')
    time.sleep(2)

    mutexB.acquire()
    print('fun01 b')

    mutexB.release()
    mutexA.release()

def fun_02():
    mutexB.acquire()
    print('fun02 b')
    time.sleep(2)

    mutexA.acquire()
    print('fun02 a')

    mutexB.release()
    mutexA.release()

# t1 = Thread(target=fun_01)
# t2 = Thread(target=fun_02)
# t1.start()
# t2.start


"""
信号量
效果类似进程池
"""

def func():
    sm.acquire()
    print('%s get sm' %threading.current_thread().getName())
    time.sleep(3)
    sm.release()

if __name__ == '__main__':
    sm=Semaphore(5)
    for i in range(23):
        t=Thread(target=func)
        t.start()