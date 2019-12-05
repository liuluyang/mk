# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/2 14:16


class F(object):
    """
    FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    """

    def __init__(self):

        self.name = 'xiaohei'

    def __getattr__(self, item):

        print('__getattr__', item)

    def __getattribute__(self, item):
        """
        获取属性
        1、对象通过.来调用任何属性或方法时，都会通过该方法实现
        2、只有该方法抛出AttributeError时，才会去调用__getattr__
        :param item:
        :return:
        """
        # print('__getattribute__', item)
        if item == 'age':
            return 20

        return super().__getattribute__(item)

        # return 1

        # raise AttributeError

    def __getitem__(self, item):
        """

        :param item:
        :return:
        """
        # print('__getitem__', item)

        return self.name[item]

        # return 1

    def __call__(self, *args, **kwargs):

        return args, kwargs


f = F()
# print(f.age)
# f.name

# print(f[-1])


# print(f.__doc__)
# print(F.__doc__)
from http import server
# print(server.__doc__)

# print(server.HTTPServer.__module__)
# print(f.__module__)

# print(f.__class__)
# print(type(f))

# print(f(1, 2, x=22))


if __name__ == '__main__':
    pass