# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/26 14:08


class F:
    def __init__(self):
        """
        初始化
        """
        print('__init__')
        pass

    def __new__(cls, *args, **kwargs):
        """
        构造函数
        :param args:
        :param kwargs:
        :return:
        """
        print(cls, args, kwargs)

        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print(args, kwargs)

    def e(self):
        print('11111111111')


# f = F()
# f2= F()
# print(f)
# print(f2)
# f.name = 'xx'
# print(f.name)
# f(11)
# f.e()

