# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/3 9:17

from typing import Iterable, Iterator, Generator


class RangeNew:


    def __iter__(self):
        """
        1、当一个对象拥有该特殊方法时，就是一个可迭代对象
        2、可作用于for循环的都是可迭代对象
        3、迭代对象不一定真正的可循环
        4、支持iter()操作、需要返回一个迭代器对象 **
        :return:
        """
        print('__iter__')

        return (i for i in range(10))


r = RangeNew()

# print(isinstance('abc', Iterable))
# print(isinstance(r, Iterable))

# print(iter(r))

# for i in r:
#     print(i)

#####################################################
"""
1、一个对象里面如果同时拥有__iter__、__next__这两个特殊方法、它就是迭代器对象
"""

class RangeNew02:

    def __init__(self, num):

        self.start = 0
        self.end = num

    def __iter__(self):

        return self

    def __next__(self):
        """
        支持next()操作
        :return:
        """

        self.start += 1

        if self.start <= self.end:
            return self.start - 1
        else:
            raise StopIteration


r02 = RangeNew02(10)

# print(isinstance(r02, Iterator))

# for i in r02:
#     print(i)


"""
模拟for循环的实现原理
"""
# iter_obj = iter(r02)
# while True:
#     try:
#         i = next(iter_obj)
#         print(i)
#     except StopIteration:
#         break


# print(next(r02))
# print(next(r02))

