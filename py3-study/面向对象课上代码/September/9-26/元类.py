# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/26 14:25


class Base(type):

    def __init__(self, what, bases=None, dict=None):
        """
        self是由元类创建出来的普通的类
        """
        # print(self, what, bases, dict, '__init__')
        self.__instance = None
        # if not what.istitle():
        #     raise

    def __new__(cls, *args, **kwargs):
        """
        cls是Base 控制创建一个普通类
        :param args:
        :param kwargs:
        :return:
        """
        # print(cls, args, kwargs, '__new__')

        return super().__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        普通类实例化的时候会触发这个方法
        :param args:
        :param kwargs:
        :return:
        """
        # print(self, args, kwargs)

        # 单例模式
        if not self.__instance:
            obj = super().__call__(*args, **kwargs)
            self.__instance = obj

        return self.__instance


class FF(metaclass=Base):
    N = 1

    def __init__(self, name):
        self.name = name


# t = FF('xiaobai')
# t2 = FF('xiaohei')
# print(t)
# print(t2)
# print(t.name)
# print(t2.name)

# t = type('F', (str,), {'name':'xx'})
# print(t)