# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/3 14:07


# print('')

# not > and > or
v1 = 10 or 1
v2 = (3 and 0) or (9 and 10)
v3 = 10 and 11

# print(bool(v1))
# print(v2)
# print(v3)
# print(bool(1.1))
# print(bool(''))


v11 = [1,2,3]
v22 = [(1),(2),(3)]
v33 = [(1,),(2,),(3,)]

# print(v11, v22, v33)

# 5. 数值交换
a, b = 1, 2
a, b = b, a
# print(a, b)


s1 = 'hell"o'
s2 = "hell\no"
s3 = """
hello
world

"""
# print(s2)
# print(s3)


lst1 = [1, 2]
lst2 = [1, 2]

res01 = 'hello'
res02 = 'hello'

# print(lst1 == lst2)
# print(lst1 is lst2)
# print(id(lst1), id(lst2))
# print(res01 is res02)
# print(id(res01), id(res02))
#
# print(res02 is None)


set_01 = {1, 2, 3}
set_02 = {4, 2, 3}

# print(set_01 & set_02)
# print(set_01 | set_02)
# print(set_01 - set_02)
# print(set_02 - set_01)

class SetNew(set):

    def __add__(self, other):

        return self | other

# set_01 = SetNew({1, 2, 3})
# set_02 = SetNew({4, 2, 3})
#
# print(set_01 + set_02)

import copy


a = [1, 2, 3, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(11)
a[3].append(11)

# print(b)
# print(c)
# print(d)



def feibo():

    a, b = 0, 1

    while True:

        a, b = b, a+b
        yield a
        if a > 100:
            break

# for i in feibo():
#     print(i)


with open('test.txt', 'rb') as f:

    # print(f.read())
    for line in f:
        print(line)

def func(name, *args, **kwargs):

    print(name, args, kwargs)

# print(func('xx', 20, c='cc'))

def func02(a, b, c):

    return a + b + c

nums = [1, 2, 3]
# print(func02(1, 2, 3))
# print(func02(*nums))


def generator(func):

    def inner(*args, **kwargs):
        print('我是装饰器')
        return func()

    return inner

@generator
def func03():

    print(nums)
    global de
    de = 1
#
# func03()
# print(de)


def nums_new():

    return [lambda x:x*i for i in range(5)]

# print(nums_new())
# print([f(2) for f in nums_new()])

# for i in range(10):
#     print(i)
#
# print(i)


def func04(a, b=[]):

    b.append(a)

    return b


# print(func04(1))
# print(func04(2))


ip = '10.3.9.12'
s = ''
for i in ip.split('.'):
    bin_num = bin(int(i))[2:].zfill(8)
    print(bin_num)
    s += bin_num
# print(s, int(s, base=2))


import os


def check_file(path):

    file_list = os.listdir(path)

    # print(file_list)

    for file_path in file_list:

        full_path = os.path.join(path, file_path)
        if os.path.isfile(full_path):
            print(full_path, '文件')
        else:
            print(full_path, '目录')
            check_file(full_path)



# check_file(r'F:\刘禄扬\project\project\education')


import math

# print(math.floor(-5.9))
# print(math.pi)


import functools


# open_new = functools.partial(open, encoding='utf8')
# print(open_new('test.txt', 'r'))

# int_new = functools.partial(int, base=2)
#
# print(int_new('11111111'))
# print(int('11111111', base=2))


def outer(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        """
        我是装饰器
        :param args:
        :param kwargs:
        :return:
        """

        return func()

    return inner

@outer
def test():
    """
    这是注释
    :return:
    """
    pass

# print(test.__doc__)
# print(test.__name__)









