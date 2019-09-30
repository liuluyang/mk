# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/19 8:33

from typing import Iterable, Iterator, Generator
import itertools

# for i in itertools.cycle(['—', '\\', '|', '/']):
#     print(i)

# for i in itertools.repeat([1, 2]):
#     print(i)

# lst = [1, 2, 3, 4, 5, 6]
# s = 'abc'

# r = itertools.combinations(lst, 3)
# print(list(r))


def check(obj):
    print(isinstance(obj, Generator), isinstance(obj, Iterable), isinstance(obj, Iterator))


"""
实现range()/int()

enumerate(lst)
zip()

"""
############################################ range()实现

def range_new_01(end):
    if not isinstance(end, int):
        raise TypeError('参数必须是整数')
    start = 0

    while start < end:
        yield start
        start += 1

# print(list(range(10)))
# print(list(range_new_01(10)))

def range_new_02(start, end):

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError('参数必须是整数')
    start = start

    while start < end:
        yield start
        start += 1

# print(list(range(2, 11)))
# print(list(range_new_02(2, 11)))

def range_new_03(start, end, step):

    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
        raise TypeError('参数必须是整数')
    if step == 0:
        raise ValueError('步长不能为0')
    start = start

    while start < end:
        yield start
        start += step

# for i in range(2, 11, -2):
#     print(i)
# for i in (range_new_03(2, 11, 2)):
#     print(i)

def range_new_04(start, end, step):

    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
        raise TypeError('参数必须是整数')
    if step == 0:
        raise ValueError('步长不能为0')
    start = start

    while start > end:
        yield start
        start += step

# print(list(range(22, 11, -2)))
# print(list(range_new_04(22, 11, -2)))
# for i in range_new_04(22, 11, -2):
#     print(i)

def range_new_05(*args):
    start, end, step = 0, None, 1
    if len(args) == 1:
        end = args[0]
    elif len(args) == 2:
        start, end = args[0], args[1]
    elif len(args) == 3:
        start, end, step = args[0], args[1], args[2]
    else:
        raise TypeError('参数错误')

    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
        raise TypeError('参数必须是整数')
    if step == 0:
        raise ValueError('步长不能为0')

    tag = '<' if step > 0 else '>'

    s = '%s %s %s' % (start, tag, end)
    while eval(s):
        yield start
        start += step
        s = '%s %s %s' % (start, tag, end)

# print(list(range(2)))
# print(list(range_new_05(2)))

def int_new(obj, base=10):
    tag = 1
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, float):
        # obj = str(obj // 1)[:-2]
        obj = str(obj).split('.')[0]

    if isinstance(obj, str):
        obj = obj.strip()
        if obj.startswith('-'):
            tag = -1
            obj = obj[1:]
        elif obj.startswith('+'):
            obj = obj[1:]
    else:
        raise TypeError('类型错误')

    b_10 = {str(i):i for i in range(10)}
    b_02 = {str(i):i for i in range(2)}
    b_16 = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    b_16.update(b_10)
    data_match = {2:b_02, 16:b_16, 10:b_10}

    num = 0
    length = len(obj)-1
    for index, n in enumerate(obj):

        num += data_match[base][n] * (base ** (length-index))

    return num * tag

# print(int('-11'))
# print(isinstance(1.1, (int, float)))
# print(int_new('-11a', 16))
# print(' 1'.isdigit())
# d = range(10)
# print(range(10)[0])
# print(d[-1])
# print(d[0])
# print(list(d))
############################################# 练习题答案02

"""
1.实现enumerate()函数
"""
def enum_new(obj, num=0):
    for i in obj:
        yield (num, i)
        num += 1

# lst = ['a', 'b', 'c']
#
# for i in enumerate(lst, 1):
#     print(i)
# print('#'*20)
# for i in enum_new(lst, 1):
#     print(i)

"""
2.实现zip()函数
"""
# print(zip([1, 2, 3], ['a', 'b', 'c', 'd']))

def zip_01(*args):
    index = 0

    for i in range(10):
        lst = []
        try:
            for ar in args:
                lst.append(ar[index])
        except:
            # print('error')
            break
        yield tuple(lst)
        index += 1

# z = zip_01([1, 2, 3], ['a', 'b', 'c', 'd'], 'dasdafsasdsa', (i for i in range(10)))
# print(list(z))


def zip_new(*args):
    args = [iter(a) for a in args]
    while True:
        lst = []
        try:
            for a in args:
                lst.append(next(a))
        except StopIteration:
            break
        yield tuple(lst)

# for i in zip(range(5), enumerate(range(5)), [1, 1, 1, 1, 1], (i for i in range(10))):
#     print(i)
# print('#'*20)
# for i in zip_new(range(5), enumerate(range(5)), [1, 1, 1, 1, 1], (i for i in range(10))):
#     print(i)


"""
3. 实现int()函数
"""
# print(int(12313))
# print(int(123.123))
# print(int('12313'))
# print(int(' +134124 '))
# print(int([123]))

def int_new02(obj, base=10):

    tag = 1
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, float):
        # obj = str(obj // 1)[:-2]
        obj = str(obj).split('.')[0]

    if not isinstance(obj, str):
        raise TypeError

    obj = obj.strip()
    if obj.startswith('-'):
        tag = -1
        obj = obj[1:]
    elif obj.startswith('+'):
        obj = obj[1:]

    b_10 = {str(i): i for i in range(10)}
    b_02 = {str(i): i for i in range(2)}
    b_16 = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    b_16.update(b_10)
    data_match = {2: b_02, 16: b_16, 10: b_10}

    num = 0
    for index, per in enumerate(obj[::-1]):
        num += data_match[base][per] * base ** index

    return num * tag

# print(int_new02(123.1))

"""
转换方法
'123'
1 * 10**2  + 2 * 10**1 + 3 * 10**0
"""
def test():
    s = '1a'
    b_10 = {str(i):i for i in range(10)}
    b_02 = {str(i):i for i in range(2)}
    b_16 = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    b_16.update(b_10)
    # print(b_10)


    num = 0
    for index, per in enumerate(s[::-1]):
        print(index, per)
        num += b_16[per] * 16 ** index

    print(num, type(num))





