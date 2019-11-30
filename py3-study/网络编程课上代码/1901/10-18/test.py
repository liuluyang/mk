# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/18 15:59

import random

def func(num):

    return random.choice(range(1, num+1))


count = 20000        # 总数
last = count         # 剩余数量
r = 0                # 累加数量
nums = 0             # 循环次数

while True:
    nums += 1
    if r == count:
        print(r)
        break

    # 变换参数
    if last > 2000:
        n = func(2000)
    else:
        n = func(last)

    r += n
    last -= n
    print(nums, n, r)




