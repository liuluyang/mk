
import random


################################ bool *
# 判断一个对象的真假

# print(bool(' '))


def bool_new(obj):
    """
    模仿bool函数
    :param obj:
    :return:
    """

    if obj:
        return True

    return False

# print(bool_new(' '))


############################### divmod *
# 计算两个数整除和取余的结果

# print(divmod(10, 2))

def divmod_new(num01, num02):
    """
    模仿divmod函数
    :param num01:
    :param num02:
    :return:
    """

    return (num01 // num02, num01 % num02)

# print(divmod_new(10, 2))


############################### enumerate *
# 把一个对象的数据和索引同时计算出来


# print(list(enumerate('abc', 10)))

def enumerate_new(item, start=0):
    """
    模仿enumerate函数
    :param item:
    :param start:
    :return:
    """
    result = []
    for i in item:
        result.append((start, i))
        start += 1

    return result


# for index, s in enumerate_new('abc'):
#     print(index, s)


################################ filter *
# 筛选函数

# nums = filter(lambda x:x>5, range(10))
# print(list(nums))
#
# print([i for i in range(10) if i > 5])


def filter_new(func, item):
    """
    模仿filter函数
    :param func:
    :param item:
    :return:
    """

    result = []
    for i in item:
        isAppend = func(i)
        if isAppend:
            result.append(i)

    return result

def map_new(func, item):
    """
    模仿map函数
    :param func:
    :param item:
    :return:
    """

    result = []
    for i in item:
        isAppend = func(i)
        result.append(isAppend)

    return result


# r = filter_new(lambda x:x>5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(r)
# print(map_new(lambda x:x>5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


################################ float * 可选
# 把整数或浮点字符串转换成浮点数

# print(float(10.111))
# # print(10 * 1.0)
# print(float('10.1'))

def float_new(obj):
    """
    模仿float函数
    :param obj:
    :return:
    """

    if isinstance(obj, float):
        return obj
    elif isinstance(obj, int):
        return obj * 1.0
    elif isinstance(obj, str):

        obj = obj.strip()
        obj_split = obj.split('.')

        if len(obj_split) == 1:
            return int(obj) * 1.0
        elif len(obj_split) > 2:
            raise

        digit = len(obj_split[-1])

        int_num = int(''.join(obj_split))
        r = int_num / 10**digit

        return r
    else:
        # raise TypeError("float_new() argument must be a string or a number, not %s"%(str(type(obj))))
        return '滚一边去'


# print(float_new('10.11'))


################################# zip *
# 并行迭代

a = [1,2,3,4]
b = [4,5]
c = [7,8,9]
d = '12345'

# z = zip(a, b, c, d)
# print(list(z))


def zip_new(*args):
    """
    模仿zip函数
    :param args:
    :return:
    """

    min_num = min([len(arg) for arg in args])
    result = []
    for index in range(min_num):
        lst = []
        for arg in args:
            lst.append(arg[index])
        result.append(tuple(lst))

    return result

# print(zip_new(a, b, c, d))
























