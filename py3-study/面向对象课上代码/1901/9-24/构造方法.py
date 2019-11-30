# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/24 15:53



class Person(object):

    opp = None

    def __init__(self, name):
        """
        初始化函数
        :param name:
        """
        self.name = name
        print('__init__', name)

    def __new__(cls, *args, **kwargs):
        """
        构造函数
        创造一个空对象
        :param args:
        :param kwargs:
        :return:
        """
        # print('__new__')
        # print(cls, args, kwargs)

        # 实现单例
        if not Person.opp:
            obj = object.__new__(cls)  # 空对象
            Person.opp = obj
        # print(obj)

        return Person.opp

    def __call__(self, *args, **kwargs):
        print('__call__')
        print(args, kwargs)



# p1 = Person('xiaohei')
# p2 = Person('xiaobai')
#
# print(p1, p2)
# print(p1.name, p2.name)
# p('xx', p='pp')

# print(p.__dict__)