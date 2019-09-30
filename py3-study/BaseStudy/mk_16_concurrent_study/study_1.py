from random import randint
from time import time, sleep
from multiprocessing import Process, Pool, Lock, Queue, JoinableQueue, cpu_count
# from threading import Thread as Process
from os import getpid
import os, time, json


"""
单进程
"""

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

################################################################

"""
多进程（可利用多核,进程内数据独立）
注：
1.join()之后需等待join的进程执行结束，才执行主进程中join()后面的代码
(如果某一个子进程的join()在另一个子进程start()之前，那这个子进程需等待上个子进程结束
才能开始执行)
2.如果没有join()，顺序执行代码，所有进程结束，程序结束
3.daemon=True（守护进程）在start()之前设置，设置之后主进程结束所有子进程全部结束
4.当互相争夺共享数据时，会出现问题，需要互斥锁

关于守护进程需要强调两点：
其一：守护进程会在主进程代码执行结束后就终止
其二：守护进程内无法再开启子进程,否则抛出异常：
AssertionError: daemonic processes are not allowed to have children
"""

def download_task_02(filename):
    print('启动下载进程，进程号[%d].' %(getpid()))
    print('开始下载%s...' % filename)
    time_to_download = randint(2, 5)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main_02():
    start = time()
    p1 = Process(target=download_task_02, args=('Python从入门到住院.pdf',)) # 创建进程
    # p1.daemon = True
    p2 = Process(target=download_task_02, args=('Peking Hot.avi',))
    # p2.daemon = True

    p1.start()  # 开始进程
    p2.start()
    p1.join()
    p2.join()

    # p = Pool(3)
    # p.apply_async(download_task_02, args=('ptyoj'))
    # p.apply_async(download_task_02, args=('pd'))
    # p.close()
    # p.join()

    end = time()
    print('总共耗费了%.2f秒.' % (end - start))
    return 1

    # while True:
    #     print(1)
    #     sleep(1)
##############################################################

"""
数据独立
"""
counter = 0

def sub_task(string):
    global counter
    while counter < 10:
        print(string)
        counter += 1
        sleep(0.01)
    print(string, counter)

def main_03():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()
    while True:
        print(counter)
        sleep(1)
####################################################

"""
互斥锁
保证同一时刻某一公有数据只能被一个进程修改
"""
def work(lock):
    # lock.acquire()  # 加锁
    print('%s is running' %os.getpid())
    # lock.release()  # 释放锁
    time.sleep(2)
    # lock.acquire()  # 加锁
    print('%s is done' %os.getpid())
    # lock.release()  # 释放锁

def main_04():
    # 由并发变成了串行,牺牲了运行效率,但避免了竞争
    lock = Lock()
    for i in range(5):
        p = Process(target=work, args=(lock,))
        p.start()

"""
互斥锁练习
"""
def search(name):
    dic=json.load(open('db.txt'))
    time.sleep(1)
    print('%s 查到剩余票数 %s'%(name,dic['count']))

def get(name):
    dic=json.load(open('db.txt'))
    time.sleep(1) #模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count'] -= 1
        time.sleep(1) #模拟写数据的网络延迟
        json.dump(dic,open('db.txt','w'))
        print('%s 购票成功'%name)

def task(name, lock):
    search(name)
    with lock:
        get(name)

def main_05():
    lock = Lock()
    with open('db.txt', 'w', encoding='utf8') as f:
        json.dump({'count':1}, f)
    for i in range(10):
        name = '<路人%s>'%(i)
        Process(target=task, args=(name,lock)).start()

###########################################################

"""
队列(进程间通信)
1.Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，
可以使用Queue实现多进程之间的数据传递。

2.maxsize是队列中允许最大项数，省略则无大小限制。
但需要明确：
    1、队列内存放的是消息而非大数据
    2、队列占用的是内存空间，因而maxsize即便是无大小限制也受限于内存大小
    
3.q=Queue()
q.put方法用以插入数据到队列中。
q.get方法可以从队列读取并且删除一个元素。

生产者、消费者模型练习
"""
def production(q):
    """
    生产
    :return:
    """
    for i in range(50):
        q.put(i)
        sleep(0.1)
    # q.join()    #等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束
    print('########%s生产者结束'%(getpid()))

def consumption(q):
    """
    消费
    :return:
    """
    while True:
        data = q.get()
        if data is None:
            print('over')
            break
        sleep(1)
        print('%s处理完成%s'%(getpid(), data))
        # q.task_done() #发送信号给q.join()，说明已经从队列中取走一个数据并处理完毕了

def main_06():
    q = Queue()  # put get empty full
    # q = JoinableQueue() # task_done
    p_list = []
    for i in range(5):
        p = Process(target=consumption, args=(q,))
        # p.daemon = True  # 随主进程一块结束
        p.start()

    for i in range(2):
        p = Process(target=production, args=(q,))
        p.start()
        p_list.append(p)

    # for p in p_list:
    #     p.join()
    # for i in range(5):
    #     q.put(None)

    print('end')
    # while True:
    #     pass


"""
进程池Pool
控制同时执行的进程的数量
"""

def download_task_03(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(1, 3)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main_07():

    p = Pool()
    for i in range(10):
        p.apply_async(download_task_03, args=(i,))
    p.close()
    p.join()  # 开始进程
    print('end')


if __name__ == '__main__':
    print('cpu数量:%s'%(cpu_count()))
    # main()
    # print('主进程：', getpid())
    # main_02()
    # main_03()
    # main_04()
    # main_05()
    # main_06()
    # main_07()
    pass