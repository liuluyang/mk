# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/30 14:03

import multiprocessing
import time

"""
第六题：
把一个给定的字符串res，处理成字符串r的样子
"""
res = 'aabcdda'
r = 'a2b1c1d2a1'


def func_06():

    res = 'aaabcdda'
    # r = 'a2b1c1d2a1'
    res_list = []

    for s in res:
        # 找到连续的字符 累加个数
        if not res_list or s != res_list[-1][0]:
            res_list.append([s, 1])
            print(res_list, '新添加的')
        else:
            res_list[-1][1] += 1
            print(res_list, '连续的')

    r = ''
    for lst in res_list:
        r += lst[0] + str(lst[-1])

    return r

# func_06()


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

user_time = {'宫保鸡丁':4, '鱼香肉丝':4, '红烧肉':5, '烧茄子':3, '干煸豆角':3, '尖椒鸡蛋':2}
menu = ['宫保鸡丁', '宫保鸡丁', '鱼香肉丝', '红烧肉', '红烧肉',
        '烧茄子', '烧茄子', '干煸豆角', '尖椒鸡蛋']

def cook(name, usertime, q=None):

    import time
    print('%s正在做。。。'%(name))
    time.sleep(usertime)
    print('%s完成'% (name))

    # q.put(1)

if __name__ == '__main__':

    # 第一种解法
    # while menu:
    #     # 已经创建的进程的数量
    #     is_active = len(multiprocessing.active_children())
    #     if is_active < 2:
    #         m = menu.pop()
    #         t = multiprocessing.Process(target=cook, args=(m, user_time[m]))
    #         t.start()
    #     else:
    #         # print('检测...')
    #         time.sleep(1)
    #         continue


    # 第二种解法
    # q = multiprocessing.Queue()
    # for i in [1]*2:
    #     q.put(i)
    #
    # for m in menu:
    #     is_ok = q.get()
    #     if is_ok:
    #         t = multiprocessing.Process(target=cook, args=(m, user_time[m], q))
    #         t.start()

    # 进程池
    pool = multiprocessing.Pool(2)
    print(multiprocessing.cpu_count())
    for m in menu:
        # 添加任务 不阻塞
        pool.apply_async(cook, args=(m,  user_time[m]))

    # 关闭进程池 不能再添加任务
    pool.close()
    # 阻塞等待
    pool.join()
    pass












