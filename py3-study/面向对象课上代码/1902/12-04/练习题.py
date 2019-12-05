# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/4 8:48



res = '(((((((((((((((((((((((((((()'


def func_01(res):

    while True:
        if res.startswith(')') or res.endswith('('):
            return False
        if len(res) == 0:
            return True
        res = res.replace('()', '')

# print(func_01(res))


def func_02(res):

    num = 0

    for i in res:

        if i == '(':
            num += 1
        elif i == ')' and num != 0:
            num -= 1
        else:
            return False

    return not bool(num)


# print(func_02(res))
