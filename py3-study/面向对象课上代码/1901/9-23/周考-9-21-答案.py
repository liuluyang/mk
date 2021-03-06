# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/21 8:33


"""10
1、简述你对类和对象的理解
"""


"""10
2、面向对象的三大特征？并简述自己的理解
"""


"""10
3、__init__函数的作用？self是什么？
"""
"""
"""


"""10
4、定义一个Person类：
    设置name/age都为私有属性
    对外提供查看修改name的接口
"""

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, name):

        self.__name = name

# p = Person('xx', 22)
# print(p.__dict__)
# #p.name = 'ff'
# print(p.name)


"""10
5、定义一个类：
    里面包括类方法和静态方法
"""
class P:
    N = 1

    @staticmethod
    def f():
        print('f')
        pass

    @classmethod
    def g(cls):
        print(cls)
        print(cls.N)
        return cls()

# p = P()
# p.f()
# P.f()
# P.g()
# p.g()


"""15
6、实现map()函数

生成器函数
"""


def map_new(func, iter):
    for i in iter:
        yield func(i)

print(map(lambda x:x*2, range(100000000)))
print(map_new(lambda x:x*2, range(10000000)))


"""15
7、扩展一下list类
    限制通过append方法添加的元素必须是字符串，否则报错
"""

"""20
8、完善OpenNew类
    要求以下代码正常执行：
    1. f = OpenNew('t.txt', 'wb') 
    2. f.write('你好哇 李银河') 
    3. f.write(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x93\x87 \xe6\x9d\x8e\xe9\x93\xb6\xe6\xb2\xb3')
"""

import time
import datetime

class OpenNew:

    def __init__(self, file, mode='r', encoding='utf8'):
        self.f = open(file, mode=mode, encoding=encoding)

    def write(self, msg):
        time_now = time.strftime('%Y-%m-%d %X')
        self.f.write(time_now + msg + '\n')

    def __getattr__(self, item):
        print('找不到方法', item)

        return getattr(self.f, item)


"""20
附加题：可做可不做
8、实现cycle类
"""
from itertools import cycle
import time

# for i in cycle(range(2)):
#     print(i)
#     time.sleep(0.5)