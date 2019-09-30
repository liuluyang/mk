# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/18 15:17


# def open_new(file, mode='r', encoding='utf8'):
#     print(file, mode, encoding)
#     f = open(file, mode=mode, encoding=encoding)
#     return f

# f = open_new('__init__.py', 'r')
# print(f)
# print(f.read())

# with open_new('__init__.py', 'r') as f:
#     print(f)
#     pass


class Foo(object):

    __cls = None

    def __init__(self, name, age=20, *args, **kwargs):
        self.name = name
        print('__init__', name)

    def __new__(cls, *args, **kwargs):
        print(cls, args, kwargs)
        if cls.__cls is None:
            print(cls.__cls)
            new_class = super().__new__(cls)
            print(new_class)
            cls.__cls = new_class

        return cls.__cls

        # return super().__new__(cls)


# f = Foo('xx', age=12)
# f2 = Foo('ww', age=22)
# print(f, f2)
# print(f.name)


nums = range(2, 1000000000, 5)
print(77777778111 in nums)

def fun(end):

    # if end <= 0:
    #     return []

    n = 0
    while True:
        yield n

        n += 1
        if n >= end:
            break

f = fun(100)
print(f)
# for i in f:
#     print(i)







