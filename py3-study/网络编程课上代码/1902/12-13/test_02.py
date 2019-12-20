# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/13 16:58



def func_01(res, num):

    start = 0
    index = len(res) // num
    result = []
    for i in range(num):
        r = res[start:start+index]
        start += index
        result.append(r)
    result[-1] += res[start:]

    return result

def func_02(res, num):


    start = 0
    index = len(res) // num
    result = []
    for i in range(num):
        if i + 1 != num:
            r = res[start:start+index]
        else:
            r = res[start:]
        start += index
        result.append(r)

    return result


def func_03(res, num):

    start = 0
    index = len(res) // num + 1 if len(res) % num else len(res) // num
    result = []
    for i in range(num):
        if i + 1 != num:
            r = res[start:start+index]
        else:
            r = res[start:]
        start += index
        result.append(r)

    return result


if __name__ == '__main__':

    res = '1234567891231'
    num = 17
    # r = func_01(res, num)
    # r = func_02(res, num)
    r = func_03(res, num)
    print(r)