# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/17 14:00

import struct


def func_01():

    start  = 0
    num = 10 ** (len(str(256**4)) - 1)
    count = 0

    while True:
        try:
            count += 1
            struct.pack('i', start)
            start += num
        except:
            start -= num
            num //= 10
            if num == 0:
                break

    return start, count

# print(func_01())

def func_02():

    count = 0
    start, end = 0, 256 ** 4 - 1

    while start <= end:
        count += 1
        mid = (start + end) // 2

        try:
            struct.pack('i', mid)
            start = mid + 1
        except:
            end = mid - 1

    return mid - 1, count


print(func_02())

