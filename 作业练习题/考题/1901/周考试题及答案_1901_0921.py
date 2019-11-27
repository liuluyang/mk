


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

def map_new_02(func, *iter):
    for i in zip(*iter):
        yield func(*i)

# print(list(map(lambda x, y:x + y, range(10), range(10, 20))))
# print(map_new_02(lambda x, y:x + y, range(10), range(10, 20)))

obj = map_new_02(lambda x:x, range(10))
# for i in obj:
#     print(i)

"""15
7、扩展一下list类
    限制通过append方法添加的元素必须是字符串，否则报错
"""


class List(list):

    def append(self, args):
        if not isinstance(args, str):
            raise ValueError('must be str')
        # list.append(self, args)
        super().append(args)


# lst = List('eqwe')
# lst.append('q')
# print(lst)


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
        # if 'b' in mode:
        #     self.f = open(file, mode=mode)
        # else:
        #     self.f = open(file, mode=mode, encoding=encoding)

        encoding = None if 'b' in mode else encoding
        self.f = open(file, mode=mode, encoding=encoding)

    def write(self, msg):
        time_now = time.strftime('%Y-%m-%d %X')
        if 'b' in self.f.mode:
            if isinstance(msg, str):
                self.f.write((time_now + msg).encode())
            elif isinstance(msg, bytes):
                self.f.write(time_now.encode() + msg)
            else:
                raise TypeError
        else:
            if isinstance(msg, bytes):
                msg = msg.decode(encoding='utf8')
            self.f.write(time_now + msg)

    def __getattr__(self, item):
        print('找不到方法', item)

        return getattr(self.f, item)


# f = OpenNew('t.txt', 'w')
# f.write('你好哇 李银河')
# f.write(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x93\x87 \xe6\x9d\x8e\xe9\x93\xb6\xe6\xb2\xb3')

"""20
附加题：可做可不做
8、实现cycle类
"""

from itertools import cycle, count, repeat
import itertools
import time

# for i in cycle((i for i in range(3))):
#     print(i)
#     time.sleep(0.5)

# for i in cycle([1, 3]):
#     print(i)
#     time.sleep(0.5)

def cycle_01(iter):

    while True:
        for i in iter:
            yield i

# for i in cycle_01([1, 2]):
#     print(i)
#     time.sleep(0.5)


class C:

    def __init__(self, num, step):
        self.num = num
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):

        self.num += self.step

        return self.num - self.step


# for i in count(0, 10):
#     print(i)

# for i in C(0, 10):
#     print(i)

# for i in repeat([1], 10):
#     print(i)

# for i in itertools.product('abc', repeat=5):
#     print(i)






