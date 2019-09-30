# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/17 14:09

class ListNew(list):

    def __init__(self, seq):

        for s in seq:
            if not isinstance(s, int):
                raise TypeError('请输入数字')

        list.__init__(self, seq)

    def append(self, *args, **kwargs):
        print(args)
        if not isinstance(args[0], int):
            raise TypeError('请输入数字')

        list.append(self, *args, **kwargs)


# lst = ListNew([1, 2])
# lst.append(3)
# print(lst)


class Base01(object):

    def func_01(self):
        print('Base01_func_01')

class Base02(Base01):
    pass
    # def func_01(self):
    #     print('Base02_func_01')

class Base03(Base02):
    pass

    # def func_01(self):
    #     print('Base01_func_01')

class Base04(Base01):

    def func_01(self):
        print('Base04_func_01')

class Child(Base03, Base04):
    pass


# (<class '__main__.Child'>, <class '__main__.Base03'>, <class '__main__.Base02'>,
# <class '__main__.Base04'>, <class '__main__.Base01'>, <class 'object'>)

#(<class '__main__.Child'>, <class '__main__.Base03'>, <class '__main__.Base02'>,
# <class '__main__.Base04'>, <class '__main__.Base01'>, <class 'object'>)

# c = Child()
# c.func_01()
# print(Child.mro())

############################################## 类属性
import uuid


# def makeUid():
#     uid = str(uuid.uuid1()).replace('-', '')
#
#     return uid

class Foo(object):

    # 类属性私有化
    __country = '中国'
    __nums = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.uid = self.makeUid()
        Foo.__nums += 1

    @property
    def age(self):
        return self.__age

    # @property
    # def nums(self):
    #
    #     return Foo.__nums

    # 类装饰器
    @classmethod
    def nums(cls):

        return cls.__nums

    # 静态方法
    @staticmethod
    def makeUid():

        uid = str(uuid.uuid1()).replace('-', '')

        return uid





#
# f = Foo('kk', 22)
# f02 = Foo('kkk', 22)

# print(f.uid)
# print(f02.uid)
# print(f.age)

# 类方法的调用
#print(Foo.nums())

# 静态方法调用
# print(f.makeUid())

######################################### isinstance issubclass

class Per(list):
    pass

# p = Per()


# print(isinstance(p, Per))

# print(issubclass(Per, list))

############################################## hasattr()getattr()setattr()delattr()


class Person:

    p = 'Person'

    def __init__(self, name):
        self.name = name

    def x(self):
        print('is x')
        pass

# p = Person('xxxxxx')

# 检查一个对象 是否有某个属性或方法
# print(hasattr(p, 'name'))

# 获取一个对象的属性
# func = getattr(p, 'xx', '没有')
# print(func)

# 设置一个对象的属性
# p.ff = 'rr'
# setattr(p, 'name1', 'ooo')
# print(p.name1)
# print(p.ff)

# 删除一个对象的属性
# del p.name
# delattr(p, 'name')
# print(p.name)

############################################### 简单应用

class User:
    def login(self):
        print('欢迎来到登录页面')

    def register(self):
        print('欢迎来到注册页面')

    def save(self):
        print('欢迎来到存储页面')

# 之前
def choose_01():
    u = User()
    while True:
        choose = input('>>>').strip()
        if choose == 'login':
            u.login()
        elif choose == 'register':
            u.register()
        elif choose == 'save':
            u.save()

# 之后
def choose_02():
    u = User()
    while True:
        choose = input('>>>').strip()
        if hasattr(u, choose):
            func = getattr(u, choose)
            func()