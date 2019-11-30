# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/19 16:06


from typing import Iterable, Iterator, Generator


def check(obj):
    # 可迭代 迭代器对象 生成器对象
    print(isinstance(obj, Iterable), isinstance(obj, Iterator), isinstance(obj, Generator))

class Nums:

    def __iter__(self):
        """
        1.只要实现了该方法的对象，那么就认为该对象是可迭代对象
        2.可迭代对象不一定可迭代
        3. iter()函数会调用这个方法、for循环也会调用该方法，
        并且返回值是实现了__iter__/__next__的迭代器对象，这时候才真正可迭代
        :return:
        """
        print('__iter__')
        return (i for i in range(10))

# n = Nums()
#
# # print(iter(n))
# check(n)
#
# for i in n:
#     print(i)

# check(iter([1, 2]))

#########################################

class Nu:

    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.start >= self.end - 1:
            raise StopIteration

        self.start += 1

        return self.start

# n = Nu(0, 10)
#
# check(n)
#
# for i in n:
#     print(i)

# nums = iter(n)
# print(nums is n)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))




