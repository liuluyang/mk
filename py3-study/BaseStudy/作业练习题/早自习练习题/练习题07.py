# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/26 8:38



"""
判断下面的字符串里面括号是否 完整正确闭合

s = '(())'

不符合的：
s1 = ')'
s2 = '('
s3 =  '())(()'
"""

def func_01(res):

    while True:
        if res.startswith(')') or res.endswith('('):
            return False
        if len(res) == 0:
            return True
        res = res.replace('()', '')


def func_02(res):

    nums = 0
    for per in res:
        if per == '(':
            nums += 1
        elif per == ')' and nums != 0:
            nums -= 1
        elif per == ')' and nums == 0:  # 中途出现 ')'没有元素与之配对
            return False

    if nums != 0:   # 剩余没有配对完
        return False
    else:
        return True


if __name__ == '__main__':
    pass
    res = '(())'
    # print(func_01(res))
    # print(func_02(res))

























