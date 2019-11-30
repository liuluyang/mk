# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/9 14:14

# print('老王开车去上班')

# def 函数名：
def func_01():
    # print('老王开车去上班')
    pass

# <function func_01 at 0x000000000208C1E0>
# print(func_01)
# #
# print(func_01())

# func_01()

# class 类名：
#  类名规范：单词首字母大写

class LaoWang:

    def func_01(self, name):
        print('老王开车去上班', name, self)

        return 100

    def func_02(self):
        print('老王去串门')

    def walk(self):
        """
        lw = LaoWang()
        当用lw.walk()调用方法的时候
        lw就是self
        :return:
        """
        print(self, '************')
        print('老王在走路。。。')
        self.func_02()
        self.func_01('xiaohei')


# <class '__main__.FileName'>
# print(LaoWang)
# # 类的实例化之后的对象
# print(LaoWang())

# 老王对象
# print(LaoWang.func_01())
# lw01 = LaoWang()
# lw01.walk()
# print(lw01, '###############')
# lw01.func_01('hello')

# print(LaoWang.func_01(lw01))
# lw01.walk()
# print('#'*20)
# lw02 = LaoWang()
# lw02.func_02()
# lw02.walk()

# print(lw01)
# lw02 = LaoWang()
# print(lw02)
# f.func_01()
# f.func_02()

# print(str)
# 参数
# s = str(13123)
# # # print(s, len(s))
# print(s.len())


# class StrNew(str):
#
#     def len(self):
#
#         return len(self)
#
# s = StrNew('hello')
# print(s.len())







