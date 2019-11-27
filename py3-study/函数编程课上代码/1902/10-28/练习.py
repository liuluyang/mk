
import random


def set_color(res):
    """
    给字符串添加颜色
    :param res:
    :return:
    """

    res_new = '\033[1;%sm%s\033[0m' % (random.randint(30, 37), res)

    return res_new


def print_triangle(size):
    """
    打印三角形
    :param size:
    :return:
    """

    if size > 100:
        size = 100

    for i in range(size):
        if i % 2 == 1:
            res = '*'*i
            res = set_color(res)
            print(res.center(size + 20))


# print_triangle(10)
# print(set_color('你好'), set_color('你好啊'))