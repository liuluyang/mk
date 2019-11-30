# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/11/29 15:03





#################################################  __getattr__



class Person(object):

    def __init__(self, name):
        self.name = name

    # def __getattr__(self, item):
    #     """
    #     当用.来调用一个对象 不存在** 的属性或方法时，
    #     会执行这个特殊方法，前提是实现了该方法
    #     :param item:
    #     :return:
    #     """
    #     print(item)
    #
    #     return '属性或方法不存在。。。。'

    def __setattr__(self, key, value):
        """
        当通过.来给对象添加属性时，
        会调用该方法
        :param key:
        :param value:
        :return:
        """
        print(key, value)
        if len(key) < 3:
            return '滚蛋'

        # 第一种：调用父类方法 来给对象添加属性
        # super().__setattr__(key, value)

        # 第二种：通过属性字典 来给对象添加属性
        self.__dict__[key] = value

    def walk(self):

        print('is walking.....')
        pass

p = Person('xiaohei')

# print(p.name1)
# print(p.w())
# print(p['name'])


# p.age = 20
# p.name = 'xx'
# print(p.age)
# print(p.name, p.__dict__)
