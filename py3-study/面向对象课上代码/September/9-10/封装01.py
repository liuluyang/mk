# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/10 14:22



class Person:

    def __init__(self, name, age):

        print(name, age, '开始的时候')
        if age < 18 or age > 40 :
            # 主动的引发异常
            raise ValueError('年龄错误')

        if not isinstance(name, str):
            raise TypeError('名字类型错误')

        self.__name = name
        self.__age = age

    def setAge(self, age):
        """
        设置年龄
        :param age:
        :return:
        """
        if age < 18 or age > 40 :
            # 主动的引发异常
            raise ValueError('年龄错误')
        self.__age = age

    def getAge(self):
        """
        获取年龄
        :return:
        """

        return self.__age

    def setName(self, name):
        """
        设置名字
        :param name:
        :return:
        """
        if not isinstance(name, str):
            raise TypeError('名字类型错误')
        self.__name = name

    def getName(self):
        """
        获取名字
        :return:
        """

        return self.__name



# p = Person('老王', 20)
# print(p.getAge())
# p.setAge('30')
# print(p.getAge())

# print(p.getName())
# p.setName('老齐')
# print(p.getName())


# 动态的添加属性
# p.gender = '男'
# p.age = 20


# 对象属性
# {'_Person__name': '老王', '_Person__age': 20, '__name': 'xiao'}
# print(p.__dict__)

################################################02

class Person:

    def __init__(self, name, age):

        # print(name, age, '开始的时候')

        if age < 18 or age > 40 :
            # 主动的引发异常
            raise ValueError('年龄错误')

        if not isinstance(name, str):
            raise TypeError('名字类型错误')

        self.__name = name
        self.__age = age

    # 属性装饰器
    # 让方法像属性一样来调用
    @property
    def age(self):
        """
        获取年龄
        :return:
        """

        return self.__age

    #
    @age.setter
    def age(self, age):
        """
        设置年龄
        :param age:
        :return:
        """
        if age < 18 or age > 40 :
            # 主动的引发异常
            raise ValueError('年龄错误')
        self.__age = age

    def setName(self, name):
        """
        设置名字
        :param name:
        :return:
        """
        if not isinstance(name, str):
            raise TypeError('名字类型错误')
        self.__name = name

    @property
    def name(self):
        """
        获取名字
        :return:
        """

        return self.__name


# p = Person('老王', 20)
# print(p.age)
# print(p.name)
#
# p.age = 30
# print(p.age)

#######################################################
class Person:

    def __init__(self, age):

        # if age < 18 or age > 40:
        #     # 主动的引发异常
        #     raise ValueError('年龄错误')

        # self.__age = age
        print('__init__')
        self.age = age

    # 属性装饰器
    # 让方法像属性一样来调用
    @property
    def age(self):
        """
        获取年龄
        :return:
        """

        return self.__age

    @age.setter
    def age(self, age):
        """
        设置年龄
        :param age:
        :return:
        """
        print('设置年龄', age)
        if age < 18 or age > 40:
            # 主动的引发异常
            raise ValueError('年龄错误')

        self.__age = age


# p = Person(20)
# print(p.__dict__)
# print()
# p.age = 30
# print(p.age)

