# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/20 14:49


# class Ran:
#
#     def __init__(self):
#         self.start = 0
#         self.end = 10
#
#     def __next__(self):
#
#         n = self.start
#         if n < self.end:
#             self.start += 1
#             return n
#         else:
#             raise StopIteration
#
# r = Ran()
#
# while True:
#     try:
#         print(next(r))
#     except StopIteration:
#         break


from typing import Iterable, Iterator

def check(obj):
    # 可迭代 迭代器对象（__iter__/__next__）
    print(isinstance(obj, Iterable), isinstance(obj, Iterator))


class Ran:

    def __iter__(self):
        """
        1. 只要实现了__iter__方法，那实例化出来的对象就是可迭代的
        2. 可迭代的对象 不一定真正可迭代
        3. iter()/for循环都会调用这个方法， 而且返回值必须是 迭代器对象
        :return:
        """

        return (i for i in range(10))

    pass

# r = Ran()
# r2 = (i for i in range(10))

# print(r2.__dir__())

# check(r)

# for a in r:
#     pass
#     print(a)

# r = iter(r)
# while True:
#     try:
#         a = next(r)
#     except StopIteration:
#         break
#     print(a)

########################################### __next__

class Ran02:

    def __init__(self):
        self.start = 0
        self.end = 10

    def __getitem__(self, item):

        return item

    def __iter__(self):

        # return self

        return Ran02()

    def __next__(self):
        """
        next()调用这个特殊方法
        :return:
        """

        if self.start < self.end:
            self.start += 1
            return self.start - 1
        else:
            raise StopIteration

# r = Ran02()
# r2 = range(10)
# print(r2[0])
# print(r[1111111111])

# check(r)

# print(next(r))

# while True:
#     try:
#         print(next(r))
#     except Exception:
#         break

###################################### return self, return Ran02()
# for i in r:
#     print(i)
#
# for i in r:
#     print(i)

# for i in r2:
#     print(i)
#
# for i in r2:
#     print(i)
















