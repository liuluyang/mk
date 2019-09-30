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

"""
第二题：
判断一个单个字符是否在一个字符串里面
s_father = 'hello world'
s_child = 'd'
注：不能用in
"""

"""
第三题：
判断一个字符串是否在另一个字符串里面
s_father = 'hello world'
s_child = 'hello'
注：不能用in
"""

"""
第四题：
给一个排好序的字符串
s = 'DDDAACCBB'
按顺序统计他们的字符出现次数：
s_new = 'D3A2C2B2'
"""

def func_00(res):
    """

    :param res:
    :return:
    """
    lst = []
    s_new = ''
    for s in res:
        if s not in lst:
            lst.append(s)

    for index, v in enumerate(lst):
        nums = res.count(v)
        s_new += v + str(nums)

    return s_new


def func_02(res):
    """

    :param s:
    :return:
    """

    if len(res) == 0:
        return

    s_new = ''
    lst = [[res[0], 1]]
    for s in res[1:]:
        if s == lst[-1][0]:
            lst[-1][-1] += 1
        else:
            lst.append([s, 1])

    for per in lst:
        s_new += per[0] + str(per[-1])

    print(lst, s_new)



s = 'DDDAACCBB'
func_02(s)

def func_01(res):
    """

    :param res:
    :return:
    """
    if len(res) == 0:
        return

    s = res[0]
    num = 1

    for per in res[1:]:
        if per == s[-1]:
            num +=1
        else:
            s += str(num)

            s += per
            num = 1

    s += str(num)
    return s


# s = 'DDDAACCBB'
# r = func_01(s)
# print(r)
