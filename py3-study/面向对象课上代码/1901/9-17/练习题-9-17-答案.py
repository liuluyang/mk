# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/17 8:35

import sys
# 输出
# sys.stdout.write('输出')

# 接手输入
# input_ = sys.stdin.readline()

"""
第一题：
实现print、input函数
"""
def input_new(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    """
    # 输出提示信息
    if args:
        sys.stdout.write(args[0])

    # 接收用户输入
    txt = sys.stdin.readline()

    return txt

# t = input_new('请输入：')
# print(t)

f = open('test', 'w', encoding='utf8')

def print_new(*args, sep=' ', end='\n', file=None):
    """

    :param args:
    :param sep:
    :param end:
    :param file:
    :return:
    """
    length = len(args) - 1

    obj = file if file else sys.stdout
    for index, a in enumerate(args):
        obj.write(a)
        if index != length:
            obj.write(sep)

    obj.write(end)

    # if not file:
    #     for index, a in enumerate(args):
    #         sys.stdout.write(a)
    #         if index != length:
    #             sys.stdout.write(sep)
    #
    #     sys.stdout.write(end)
    # else:
    #     for index, a in enumerate(args):
    #         f.write(a)
    #         if index != length:
    #             f.write(sep)
    #
    #     f.write(end)

# print_new('12', '123', sep='|', file=f)
# print_new('1111')
# print('12', '123', sep='|')


class P:

    def write(self, text):
        print(text)

def main(obj):

    obj.write('哈哈fffffffff')

# f = open('test', 'w', encoding='utf8')
# p = P()
# main(p)


"""
第二题：
实现一个List
列表只能存数字
"""
from typing import Iterable


class ListNew(list):

    def __init__(self, seq):
        if not isinstance(seq, Iterable):
            raise TypeError("必须是一个 可迭代对象")
        self.values = seq
        for s in self.values:
            if not isinstance(s, int):
                raise TypeError('请写数字')
        self.extend(*self.values)  # 1, 12312,123,123,123,123,123,123123

    def extend(self, *args, **kwargs):
        list.extend(self, args)


# lst01 = ListNew([1, 12312,123,123,123,123,123,123123])
# print(lst01)


class ListNew(list):

    def __init__(self, seq):
        for s in seq:
            self.append(s)

    def append(self, *args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError('请输入数字')

        list.append(self, *args, **kwargs)

# lst = ListNew([1, 2])
# lst.append(3)
# print(lst)










