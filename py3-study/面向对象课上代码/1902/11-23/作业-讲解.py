


"""
小球落地
小球每次弹起的高度是下落的一半，小球从100米开始下落

1、10次下落之后弹起的高度是多少
2、下落多少次之后弹起的高度会小于1米
3、10次下落之后小球走过的总路程
"""
class Xq:

    def __init__(self):
        self.high = 100

    def func_01(self, n=10):
        """
        10次下落之后弹起的高度是多少
        :param n:
        :return:
        """

        high = self.high
        for i in range(n):
            high /= 2

        return high

    def func_02(self, h=1):
        """
        下落多少次之后弹起的高度会小于1米
        :param h:
        :return:
        """

        high = self.high
        count = 0

        while True:
            high /= 2
            count += 1

            if high < h:
                return count, high

    def func_03(self, n=10):
        """
        10次下落之后小球走过的总路程
        :return:
        """

        high = self.high
        way_all = 0

        for i in range(n):
            way_all += high    # 下落的路径
            high /= 2
            way_all += high     # 弹起的路径

        return way_all


"""
class Person:
    pass
    
属性：name, age  私有化
方法：birthday 生日, isadult 成年, info 信息
"""
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def birthday(self):

        self.__age += 1

    @property
    def isadult(self):

        return self.__age >= 18

    @property
    def info(self):

        return self.__name, self.__age


"""
判断一个字符串是否在另一个字符串里面
s_father = 'hello world'
s_child = 'hello'
注：不能用in
"""
import time
import re

def check_time(func):

    def inner(*args, **kwargs):

        t = time.time()
        f = func(*args, **kwargs)
        print('%s函数运行时间：%s'%(func.__name__, time.time() - t))

        return f

    return inner


res01 = 'abcde'*1000000 + 'f'
res02 = 'abcde'*100 + 'f'


@check_time
def check_00(s_father, s_child):
    """
    内置方法
    :param s_father:
    :param s_child:
    :return:
    """

    return s_child in s_father


@check_time
def check_01(s_father, s_child):
    """
    判断单个字符
    :param s_father:
    :param s_child:
    :return:
    """
    for s in s_father:
        if s == s_child:
            return True

    return False


@check_time
def check_02(s_father, s_child):
    """
    基础方法
    :param s_father:
    :param s_child:
    :return:
    """

    child_len = len(s_child)
    for index in range(len(s_father)):
        if s_father[index:index+child_len] == s_child:
            return True

    return False


@check_time
def check_03(s_father, s_child):
    """
    正则方法
    :param s_father:
    :param s_child:
    :return:
    """

    return bool(re.search(s_child, s_father))


# print(check_01(res01, res02))
# print(check_02(res01, res02))
# print(check_00(res01, res02))
# print(check_03(res01, res02))