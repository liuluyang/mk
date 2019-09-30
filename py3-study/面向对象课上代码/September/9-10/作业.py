# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/10 16:55


"""
创建一个Person类
1.
有私有属性：name. age, gender
但是有两个公开属性info, isAdult
info属性以元组的形式返回该对象所有私有属性
isAdult属性返回该对象是否成年 True or False 注：>=18是成年
2.
有一个方法birthday
每次调用这个方法，都会长一岁
"""

class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def info(self):
        """
        所有信息
        :return:
        """
        return self.__name, self.__age, self.__gender

    @property
    def isAdult(self):
         """
         是否成年
         :return:
         """
         if self.__age >= 18:
             return True

         return False

    def birthday(self):
        """
        过生日
        :return:
        """

        self.__age += 1