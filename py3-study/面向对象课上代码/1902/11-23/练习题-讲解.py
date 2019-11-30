


"""
判断一个字符串是否在另一个字符串里面
s_father = 'hello world'
s_child = 'hello'
注：不能用in
"""
import time

def check_time(func):

    def inner(*args, **kwargs):

        t = time.time()
        f = func(*args, **kwargs)
        print('%s函数运行时间：%s'%(func.__name__, time.time() - t))

        return f

    return inner


res01 = 'abcde'*100000 + 'f'
res02 = 'f'

@check_time
def check_00(s_father, s_child):

    return s_child in s_father


@check_time
def check_01(s_father, s_child):

    for s in s_father:
        if s == s_child:
            return True

    return False


@check_time
def check_02(s_father, s_child):

    child_len = len(s_child)
    for index in range(len(s_father)):
        if s_father[index:index+child_len] == s_child:
            return True

    return False


# print(check_01(res01, res02))
# print(check_02(res01, res02))
# print(check_00(res01, res02))


##############################################  字符串检查


class CheckStr:


    def __init__(self, s_father):

        self.s_father = s_father

    def __check_01(self, s_child):

        for s in self.s_father:
            if s == s_child:
                return True

        return False

    def __check_02(self, s_child):

        child_len = len(s_child)
        for index in range(len(self.s_father)):
            if self.s_father[index:index + child_len] == s_child:
                return True

        return False

    def check(self, s_child):
        """
        统一接口调用
        :param s_child:
        :return:
        """

        if len(s_child) > 1:
            self.__check_02(s_child)
        else:
            self.__check_01(s_child)


c = CheckStr(res01)

# print(c.check_01('a'))
# print(c.check_02('a'))

#
# print(c.check('a'))

################################################## print()


"""
完全模仿print()
"""
import sys

def print_new(*args, sep='-', end='\n', file=None):

    obj = file if file else sys.stdout
    obj.write(sep.join(str(i) for i in args))
    obj.write(end)


f = open('test.txt', 'a', encoding='utf8')
# print('hello', 'world', file=f)

# print_new('hello', 'world')
# print_new('hello', 'world', [1, 2])










