# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/20 15:01


from itertools import cycle
import time

# class Cycle:
#
#     def __init__(self, obj):
#         self.obj_origin = obj
#         self.obj = iter(obj)
#
#     def __iter__(self):
#
#         return self
#
#     def __next__(self):
#
#         try:
#             return next(self.obj)
#         except StopIteration:
#             self.obj = iter(self.obj_origin)
#             return next(self.obj)





# for i in cycle('你好哇李银河'):
#     print("\r%s"%i, end="")
#     time.sleep(0.5)



def er():

    lst = list(range(10))
    num = 1

    start = 0
    end = len(lst) - 1

    while start <= end:
        mid_index = (start + end) // 2
        mid_num = lst[mid_index]
        print(start, end, mid_num)
        if num == mid_num:
            return True
        elif num < mid_num:
            end = mid_index - 1
        elif num > mid_num:
            start = mid_index + 1

    return False

"""
10 // 2 == 5
5 // 2 == 2
2 // 2 == 1
1 // 2 == 0 
"""

r = er()
print(r)

import math

print(math.log(10, 3))
print(3 ** math.log(10, 3))
print(2 ** 1.5)
