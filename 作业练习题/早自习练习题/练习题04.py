

import sys

"""
第一题：
实现print、input函数

提示：
import sys
# 输出
# sys.stdout.write('输出')
# 接收输入
# input_ = sys.stdin.readline()
"""
def input_new(*args, **kwargs):
    """
    input()
    :param args:
    :param kwargs:
    :return:
    """
    # 输出提示信息
    if args:
        sys.stdout.write(args[0])

    # 接收用户输入
    txt = sys.stdin.readline()

    return txt


def print_new(*args, sep=' ', end='\n', file=None):
    """
    print()
    :param args:
    :param sep:
    :param end:
    :param file:
    :return:
    """
    length = len(args) - 1

    # 未简化版本
    if not file:
        for index, a in enumerate(args):
            sys.stdout.write(a)
            if index != length:
                sys.stdout.write(sep)

        sys.stdout.write(end)
    else:
        for index, a in enumerate(args):
            file.write(a)
            if index != length:
                file.write(sep)

        file.write(end)

    # 简化版本
    # obj = file if file else sys.stdout
    # for index, a in enumerate(args):
    #     obj.write(a)
    #     if index != length:
    #         obj.write(sep)
    #
    # obj.write(end)


"""
第二题：
实现一个List
通过append方法添加元素时，只能存数字
"""
class ListNew(list):
    """
    第二题
    """

    def __init__(self, seq):
        for s in seq:
            self.append(s)

    def append(self, *args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError('请输入数字')

        list.append(self, *args, **kwargs)










