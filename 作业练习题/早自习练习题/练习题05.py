

from typing import Iterable, Iterator, Generator

def check(obj):
    print(isinstance(obj, Generator), isinstance(obj, Iterable), isinstance(obj, Iterator))

"""
实现：
range()
int()

enumerate()
zip()等函数
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

# for i in range(2, 11, 2):
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
# for i in range_new_04(22, 11, -2):
#     print(i)

def range_new_05(*args):
    """
    range()函数完整实现
    :param args:
    :return:
    """
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

######################################################int()函数实现

def int_new(obj, base=10):
    """
    int()
    :param obj:
    :param base:
    :return:
    """
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


############################################# 练习题答案02

"""
1.实现enumerate()函数
"""
def enum_new(obj, num=0):
    for i in obj:
        yield (num, i)
        num += 1


"""
2.实现zip()函数
"""
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


############################################## 思路
"""
3. 实现int()函数
转换方法
'123'
1 * 10**2  + 2 * 10**1 + 3 * 10**0
"""
def test():
    s = '1a'

    b_10 = {str(i):i for i in range(10)}   # 十进制
    b_02 = {str(i):i for i in range(2)}    # 二进制
    b_16 = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}  #十六进制
    b_16.update(b_10)

    num = 0
    for index, per in enumerate(s[::-1]):
        print(index, per)
        num += b_16[per] * 16 ** index

    print(num, type(num))





