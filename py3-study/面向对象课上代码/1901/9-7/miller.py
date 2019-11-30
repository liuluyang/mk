# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/21 13:55


# class Foo(object):
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#     def __getattr__(self, item):  # 通过 . 语法查找一个属性的时候, 如果没有找到,触发该方法的执行。
#         print("__getattr__ 被触发")
#
#     def __delattr__(self, item):  # 通过 del 方式删除的时候, 会触发这个执行。
#         print("__delattr__ 被触发")
#         self.__dict__.pop(item)
#
#     def __getattribute__(self, item):  # 无条件触发, 只要实例对象通过 . 语法访问属性, 就会无条件被触发
#         dic = super().__getattribute__("__dict__")
#         if item == "__dict__":
#             return dic
#         if item in dic:
#             return dic[item]
#         raise AttributeError("%s no attribute '%s'" % (self, item))


# __class__  # 获取当前对象 是由哪个类实例化出来的, 并返回这个类


# class UrlGenerator(object):
#     def __init__(self, root):
#         self.root = root
#
#     def __getattr__(self, item):
#         return UrlGenerator(self.root + item + "/")
#
#
# url = UrlGenerator("http://127.0.0.1:8000/")
# url = url.miller.aticles.html
# print(url.root)
#


# 1. 直接通过, 类名重用父类方法. 不依赖继承。
# 2. super()  依赖继承, mro列表, 顺序的查找。


class Person(object):
    def __init__(self, height, wight, salary):
        self.height = height
        self.wight = wight
        self.__salary = salary

    # def BMI(self):
    #     return self.wight / ((self.height/100) ** 2)

    # @property
    # def salary(self):
    #     return self.__salary
    #
    # @salary.setter
    # def salary(self, val):
    #     self.__salary = val

    @classmethod
    def talk(cls):
        print(cls)
        print("is talking..... can you speak English")

    @staticmethod
    def run(name):
        print("%s runing" % name)


# p1 = Person(170, 60, 15000)
# p1.talk()
# Person.talk()










