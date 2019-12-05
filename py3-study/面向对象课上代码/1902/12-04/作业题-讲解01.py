# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/4 10:37




# 1、一个参数 必须是整数

r01 = range(10, 1, -3)

def func_01(start, num, step):

    if not isinstance(num, int) or not isinstance(start, int) or not isinstance(step, int):
        raise TypeError('参数错误')
    if step == 0:
        raise TypeError('参数错误')
    # start = 0

    while start > num:

        yield start
        start += step


print(list(r01))
# print(func_01(10))
# for i in func_01(10, 1, 3):
#     print(i)


# 2、两个参数 必须是整数

r02 = range(1, 10)
# print(list(r02))


# 3、三个参数 必须是整数

r03 = range(1, 10, 2)
# print(list(r03))


# 4、三个参数 必须是整数

r04 = range(10, 1, -2)
# print(list(r04))


# 5、满足所有情况


def range_new(*args):

    start, end, step = 0, None, 1

    if len(args) == 1:
        end = args[0]
    elif len(args) == 2:
        start, end = args[0], args[1]
    elif len(args) == 3:
        start, end, step = args[0], args[1], args[2]

    if not isinstance(end, int) or not isinstance(start, int) or not isinstance(step, int):
        raise TypeError('参数错误')
    if step == 0:
        raise TypeError('参数错误')

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step

# print(range(1, 10))
# for i in range_new(10, 1, -2):
#     print(i)

from typing import Iterable, Iterator


# print(isinstance(range(10), Iterator))
#
# print(range(1000000)[-9999])