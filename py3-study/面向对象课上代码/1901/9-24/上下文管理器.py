# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/24 11:23



class OpenNew:

    def __init__(self, file, mode='r', encoding=None):
        self.f = open(file, mode=mode, encoding=encoding)

    def __enter__(self):
        """
        1 先执行
        :return:
        """
        print('__enter__')

        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        1. 后执行
        2. 异常对象
        3. 异常内容
        4.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print('#'*20)
        print(exc_type, 'exc_type')
        print(exc_val, 'exc_val')
        print(exc_tb, 'exc_tb')
        print('__exit__')
        self.f.close()

        print('11111111111')

        return True               # 异常不传递
        # return False               # 异常传递


# with OpenNew('t.txt', 'r', encoding='utf8') as f:
#     pass
#     print(f)
#     # raise TypeError('type error')
# print(f.closed)
#
# with open('t.txt', 'r', encoding='utf8') as f:
#     print(f)
# print(f.closed)

######################################################


class OpenNew_02:

    def __init__(self, func, args, kwargs):
        self.func = func(*args, **kwargs)
        print(func)
        pass

    def __enter__(self):
        """
        :return:
        """

        return next(self.func)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        try:
            next(self.func)
        except StopIteration:
            pass


def func(func_name):

    def inner(*args, **kwargs):

        return OpenNew_02(func_name, args, kwargs)

    return inner

from contextlib import contextmanager

@func
# @contextmanager
def open_01(name):
    f = open(name, mode='r', encoding='utf8')
    yield f
    f.close()

with open_01('t.txt') as f:
    print(f)
    # raise TypeError

print(f.closed)


# def open_01():
#     f = open('t.txt', mode='r', encoding='utf8')
#
#     yield f
#
#     f.close()
#     # yield 1111111111
#
# p = open_01()
# print(next(p))
# next(p)

# def f():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
#
# f = f()
# print(next((f)))
# print(next((f)))
# print(next((f)))
# print(next((f)))
# print(next((f)))


# __set__
# __get__
# __delete__

class Desicaption(object):

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        print(instance)
        print("__delete__ 被触发")


class Foo(object):
    name = Desicaption("name")
    def __init__(self, name):
        self.name = name


# f1 = Foo("miller")
#
# print(f1.name)










