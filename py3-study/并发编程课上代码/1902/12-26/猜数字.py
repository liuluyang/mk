# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/25 11:25


"""
第八题：
猜数字游戏
规则：
    实例化GuessNum会得到一个实例对象
    同时该对象拥有一个属性num，是一定范围内的随机数

    我们能做的是调用check_num_01这个方法，把猜测的数字传进去，
    来获取两个数字对比的结果， 从而来确定num的值

写个函数来完成此游戏，把猜测正确的数字返回

g = GuessNum()
r = g.check_num_01(32423432)
print(r)   # 大了、小了或等于
"""


class GuessNum:
    """
    一个猜数字的游戏
    """

    def __init__(self):

        self.num = self.make_num()

    def make_num(self):
        """
        产生一个随机数
        :return:
        """
        import random

        return random.randint(1000000, 100000000)

    def check_num_01(self, guess_num):
        """
        检查猜测的数字
        :param guess_num:
        :return:
        """
        if guess_num > self.num:
            return '大了'
        elif guess_num < self.num:
            return '小了'

        return '等于'

    def check_num_02(self, guess_num):
        """
        检查猜测的数字
        :param guess_num:
        :return:
        """
        if guess_num > self.num:
            return '大了'
        elif guess_num <= self.num:
            return '小了'


def func_08():

    g = GuessNum()
    period = 100000000000
    r = 0
    count = 0
    while True:
        count += 1
        r += period
        res = g.check_num_02(r)

        if res == '大了':
            r -= period
            period //= 10
            if period == 0:
                break

    return r, g.num, count


if __name__ == '__main__':
    # 8300  8301 - 1
    # 3 4 1 6 8 3 2 5
    r = func_08()
    print(r)













