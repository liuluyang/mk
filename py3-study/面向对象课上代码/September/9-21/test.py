# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/21 11:31


class P:
    instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):

        if not cls.instance:
            cls.instance = object.__new__(cls)

        return cls.instance

# p1 = P('x')
# p2 = P('C')
# print(p1, p2)
# print(p1.name, p2.name)


def fun():
    yield 1

# print(type(fun))

# lst = list(range(100))
# print(id(lst))
# for i in range(100, 20000):
#     lst.append(i)
# print(id(lst))

# a = set()
# b = set()
# print(a is b)