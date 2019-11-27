

import random

"""
func函数接收一个参数num
然后随机返回一个1-num之间的数，包括num
"""
def func(num):

    if num > 200:
        num = 200

    return random.choice(range(1, num+1))

"""
写一个程序，把每次调用func获取到的数累加起来
如何快速准确的让累加的数到达1024（不多不少）
func函数的参数num最大可填200
"""
count = 0
while True:

    r = func(200)
    count += r

    if count >= 1024:
        print(count)
        break




