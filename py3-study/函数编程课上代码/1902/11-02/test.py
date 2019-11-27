


import random

def set_color(res):
    """
    给字符串添加颜色
    :param res:
    :return:
    """

    res_new = '\033[1;%sm%s\033[0m' % (random.randint(30, 37), res)

    return res_new

def test():
    for i in range(15):
        print(' '*(15-i), set_color('* '*(i+1)), set_color('* '*(15-i-1)))