


"""
1 1 2 3 5 8 13 21 34 55
"""

def func_01(num):
    """
    斐波那契数列
    递归版本
    :param num:
    :return:
    """

    if num <= 1:
        return 1

    return func_01(num - 1) + func_01(num - 2)


# print(func_01(115))


def func_02(num):
    """
    斐波那契数列
    循环版本
    :param num:
    :return:
    """

    lst = [1, 1]

    for i in range(num - 2):
        lst.append(lst[-1] + lst[-2])

    return lst


# print(func_02(1116))


def func_03():
    """

    :return:
    """

    num = 0
    size = 0
    while True:
        num += 1
        size += len(bin(num)) - 2
        # if num % 100000 == 0:
        #     print(num)
        if num == 1000000:
            break

    print(size/1000/1000)



    # print(36**5*5/1000/1000)


import time
import set_color


def time_machine():
    """
    倒计时
    :return:
    """

    time_tuple = time.strptime('2019-11-11', '%Y-%m-%d')
    print(time_tuple)
    timestamp = time.mktime(time_tuple)
    print(timestamp)

    while True:
        d, h = divmod(timestamp-time.time(), 60*60*24)
        # print(d, h)
        h, m = divmod(h, 60*60)
        # print(h, m)
        m, s = divmod(m, 60)
        # print(m, s)
        res_time = '%s天 %s小时 %s分 %s秒'%tuple(map(lambda x:int(x), [d, h, m, s]))
        print('\r', set_color.set_color(res_time), end='')
        time.sleep(1)


# time_machine()













