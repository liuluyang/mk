# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/11/29 14:04


"""
特殊方法
magic

"""


class IntNew:

    def __int__(self):
        """
        可以支持int()操作
        返回值必须是整数
        :return:
        """

        return 111111

    def __str__(self):
        """
        可以支持str()操作
        返回值必须是字符串
        :return:
        """

        return 'u'

#########################################
"""
str
repr
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        """
        使str(),print()操作,返回的结果是__str__的返回结果
        返回值必须是字符串
        :return:
        """

        return str((self.name, self.age))

    def __repr__(self):
        """
        可以支持repr()操作
        返回值必须是字符串

        支持解释器的显示模式
        :return:
        """

        return str(('Person', (self.name, self.age)))

u = IntNew()
# print(int(u))

# print(str(u))

p_list = []

p = Person('小黑', 22)
p2 = Person('小2黑', 22)
p_list.append(p)
p_list.append(p2)

# print(p)

# print(p_list)
# print(repr(p))
# print(repr('hello world'))


########################################################
"""
contains
abs
add
ge
len
"""

class StrNew(str):

    def __contains__(self, item):
        """
        支持in语法
        返回值必须能表示真假
        :param item:
        :return:
        """
        if item == 'a':
            return True

        return

    def __abs__(self):
        """
        支持abs()操作
        :return:
        """

        return 'a'

    def __add__(self, other):
        """
        支持多个对象相加的运算
        :param other:
        :return:
        """

        return str(other) + str(self)

    def __ge__(self, other):
        """
        支持>=比较运算
        :param other:
        :return:
        """

        return len(self) >= len(other)

    def __len__(self):
        """
        支持len()操作
        :return:
        """

        return 1024


s = StrNew()
s2 = StrNew()

# print('a' in 'hello a')
# print('aa' in s)

# print(abs(s))

# print(s + s2)
# print(StrNew('hello') + StrNew('world'))

# print(StrNew('hell') >= StrNew('world'))

# print(len(StrNew('hell')))


###################################################### hash
"""
不可变数据类型：可哈希的对象
    数字 字符串 元组
可变数据类型：
    列表 集合 字典
"""

class DictNew(dict):

    def __hash__(self):
        """
        支持hasn()操作
        必须返回整数
        :return:
        """

        return 1

    pass


d = DictNew({1:2, 2:3})

# print({d:1})

# print(hash(d))








