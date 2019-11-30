# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/11 13:43

class Pratice:

    def __func_02(self, s_father, s_child):
        """
        第二题：
        判断一个单个字符是否在一个字符串里面
        s_father = 'hello world'
        s_child = 'd'
        注：不能用in
        """
        print('d')
        for per in s_father:
            if per == s_child:
                return True

        return False

    def __func_03(self, s_father, s_child):
        """
        第三题：
        判断一个字符串是否在另一个字符串里面
        s_father = 'hello world'
        s_child = 'hello'
        注：不能用in
        """
        print('hello')
        s_len = len(s_child)
        for index_ in range(len(s_father) - s_len + 1):
            per = s_father[index_:index_ + s_len]
            if per == s_child:
                return True

        return False

    def main(self, s_father, s_child):
        if len(s_child) == 1:
            return self.__func_02(s_father, s_child)
        else:
            return self.__func_03(s_father, s_child)


# p = Pratice()
# print(p.main('dadas', 'aa'))