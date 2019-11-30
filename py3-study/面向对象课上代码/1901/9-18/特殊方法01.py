# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/18 9:40

################################################## __getattr__ ,__setattr__ ,__delattr__

class Person(object):

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        """
        1. 当调用的属性不存在的时候，会调用这个方法
        :param item:
        :return:
        """
        pass
        # print('__getattr__', item)

        return '没有这个属性，滚蛋吧'

    def __setattr__(self, key, value):
        """
        1. 当用点.来设置属性的时候，自动调用这个方法, 设置属性
        2. 自己实现属性的添加，否则属性添加失败
        :param key:
        :param value:
        :return:
        """

        print('__setattr__', key, value)

        # object.__setattr__(self, key, value)  # 可以用

        # self.key = value                       # 递归调用

        self.__dict__[key] = value             # 可以用


    def __delattr__(self, item):
        """
        1. 当删除属性的时候，会调用这个方法
        :param item:
        :return:
        """
        print('__delattr__', item)

        # object.__delattr__(self, item)  # 可以用

        self.__dict__.pop(item)      # 可以用


# p = Person('xx')
# print(p.name)
# del p.name
# print(p.name111)

# p.__dict__['name'] = 'xx'           # 通过 属性字典 添加 修改 删除属性



################################################   __getattribute__


class Person02(object):

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        print('__getattr__', item)

    def __getattribute__(self, item):
        """
        # 当用点.来调用属性和方法时，都会执行这个方法
        # 只有该方法抛出AttributeError异常时，才会去调用__getattr__方法（前提是已经实现该方法）
        :param item:
        :return:
        """
        print('__getattribute__', item)
        # if item == 'name':
        #     return '沙雕'
        # raise ValueError
        return object.__getattribute__(self, item)     #

        # return 11111

    def w(self):
        print('w')


# p = Person02('xx')
# print(p.__dict__)
# print(p.name1)
# print(p.w1)


#################################################  __setitem__,__getitem__,__delitem__


class Person03(object):

    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):
        """
        1. 父类没有实现这个方法
        2. 如果实现了这个方法，支持以[]调用属性
        :param item:
        :return:
        """
        print('__getitem__', item)

        return 1111

    def __setitem__(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """

        self.__dict__[key] = value


# p = Person03('xx')
# p['age'] = 11

# print(p['name'])

# print(p.age)

############################################## __str__,__repr__

class Person04(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        1. 友好一点的展示方式
        2. print(), str()都会优先调用该方法，如果没有，去找__repr__
        3. 返回值必须是字符串
        :return: str
        """
        # return '<__main__.%s object at 0x0000000001DCB3C8>'
        return  '(%s, %s)'%(self.name, self.age)

    def __repr__(self):
        """
        1. 被解释器调用
        2. 返回值必须是字符串
        :return:
        """
        return 'Person(%s, %s)'%(self.name, self.age)

    def __int__(self):
        """
        int()调用该方法
        返回值必须是数字
        :return:
        """

        return len(self.name)

    def __add__(self, other):
        """
        支持两个对象相加 +
        :param other:
        :return:
        """

        return self.name + '-' + other.name

    def __abs__(self):
        """
        支持abs()函数
        :return:
        """
        return 1111111111111

import uuid

p = Person04('小绿', 22)
p2 = Person04('xx', 22)

# print(int(p))

# print(p + p2)
# print(abs(p))

# lst = [p, p2]
# print(lst)
# print(p)

# print(p)
# print(p2)
# p_str = str(p)
# print(p, type(p), type(p_str), p_str)   #

# uid = uuid.uuid1()
# uid_str = str(uid)
# print(uid, uid_str.replace('-', ''))


#################################################

class F(dict):
    # __hash__ = None
    pass

    def __hash__(self):

        return 1

# f = F()
# dic = {'a':'b'}
# f2 = F(dic)
# print(f, hash(f))
#
# d = {f:1, f2:2}
# # print(hash(f), id(f))
# print(d)
# for i in range(10):
#     f[i] = 'b'
# print(d)
#
# for k, v in d.items():
#     print(k, v, id(k), )
# f2[2] = 1
# print(d.get(f2))
# print(d)


####################################################

# a = {1:1, 2:2}
# b = {2:2, 1:1}
# print(id(a) , id(b))





