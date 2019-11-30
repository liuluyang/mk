# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/10 8:37



"""
第一题：
给一个下落次数，
1.求出此时小球离地面的距离
2.小球总共走的路径
"""
def func_01(num, is_count=None):

    r = 0
    hight = 100

    for i in range(num):
        r += hight
        hight /= 2
        r += hight

    # hight_new = 100
    # count_ = 0
    # print(is_count, bool(is_count))
    # if is_count:
    #     while True:
    #         hight_new /= 2
    #         count_ += 1
    #         if hight_new < is_count:
    #             break

    return hight, r

# f = func_01(1)
# print(f)

"""
第二题：
判断一个单个字符是否在一个字符串里面
s_father = 'hello world'
s_child = 'd'
注：不能用in
"""

def func_02(s_father, s_child):
    """
    第二题：
    判断一个单个字符是否在一个字符串里面
    s_father = 'hello world'
    s_child = 'd'
    注：不能用in
    """
    for per in s_father:
        if per == s_child:
            return True

    return False

# f = func_02('hello world', 'f')
# print(f)

"""
第三题：
判断一个字符串是否在另一个字符串里面
s_father = 'hello world'
s_child = 'hello'
注：不能用in
"""
def func_03(s_father, s_child):
    """
    第三题：
    判断一个字符串是否在另一个字符串里面
    s_father = 'hello world'
    s_child = 'hello'
    注：不能用in
    """
    s_len = len(s_child)
    for index_ in range(len(s_father)-s_len+1):
        per = s_father[index_:index_+s_len]
        if per == s_child:
            return True

    return False


# f = func_03('helloworld', 'worldd')
# print(f)

"""
第四题：
给一个排好序的字符串
s = 'DDDAACCBB'
按顺序统计他们的字符出现次数：
s_new = 'D3A2C2B2'
"""

class Pratice:

    def func_01(self, num, is_count=None):
        """
        第一题：
        给一个下落次数，
        1.求出此时小球离地面的距离
        2.小球总共走的路径
        :param num:
        :param is_count:
        :return:
        """

        r = 0
        hight = 100

        for i in range(num):
            r += hight
            hight /= 2
            r += hight

        # hight_new = 100
        # count_ = 0
        # print(is_count, bool(is_count))
        # if is_count:
        #     while True:
        #         hight_new /= 2
        #         count_ += 1
        #         if hight_new < is_count:
        #             break

        return hight, r

    def func_02(self, s_father, s_child):
        """
        第二题：
        判断一个单个字符是否在一个字符串里面
        s_father = 'hello world'
        s_child = 'd'
        注：不能用in
        """
        for per in s_father:
            if per == s_child:
                return True

        return False


    def func_03(self, s_father, s_child):
        """
        第三题：
        判断一个字符串是否在另一个字符串里面
        s_father = 'hello world'
        s_child = 'hello'
        注：不能用in
        """
        s_len = len(s_child)
        for index_ in range(len(s_father) - s_len + 1):
            per = s_father[index_:index_ + s_len]
            if per == s_child:
                return True

        return False

# p = Pratice()
# print(p.func_01(3))


