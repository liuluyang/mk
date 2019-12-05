# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/4 14:22



class Foo(object):

    __instance = None

    def __init__(self, name):
        """
        初始化函数
        给对象绑定一些属性
        :param name:
        """
        # print('__init__')
        self.name = name

    def __call__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        """
        构造函数
        在初始化函数之前执行
        创建一个没有属性的对象
        :param args:
        :param kwargs:
        :return:
        """
        # print('__new__')
        # print(cls, args, kwargs)

        # 实现单例模式
        if cls.__instance is None:

            obj_new = super().__new__(cls)
            cls.__instance = obj_new

        return cls.__instance

    def w(self):
        print('wwwwwwwwww')


"""

创建实例化对象  绑定属性    调用对象
__new__()  =>  __init__()  => __call__
"""

f = Foo('xiaohei')
f2 = Foo('小白')

print(f.name)
print(f2.name)
print(f is f2)
# print(f is None)
# print(f.name1)
# print(None.x)












