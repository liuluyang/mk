# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/11/28 11:10



class ListNew(list):

    pass

lst = ListNew()

# 参数 must be a class
# print(issubclass(ListNew, list))

# print(isinstance(2, (str, list)))


################################################ hasattr
class P:


    count = 1

    def __init__(self):

        self.a = 1

    def w(self):
        print('this is w')
        pass


p = P()

# 检查一个对象有没有指定的方法或属性
# print(hasattr(lst, 'append'))
# print(hasattr(p, 'w'))

# 列出对象的所有属性或方法
# print(lst.__dir__())

####################################################### getattr


"""
获取一个对象指定的方法或属性 找不到的时候会报错
第三个参数选填 如果填入第三个参数 找不到时返回它
"""
# print(getattr(p, 'a'))
# print(getattr(p, 'w2', None))


# 获取对象的所有属性
# print(p.__dict__)
# print(P.__dict__)


###################################################### setattr


def new(self):

    print('this is new')

# 给一个对象添加属性或方法
# setattr(P, 'new', new)  # p.new = 1
# print(p.new())
# print(p.__dir__())


###################################################


class User:

    def __init__(self):

        self.name = 'xx'

    def login(self):
        print('欢迎来到登录页面')

    def register(self):
        print('欢迎来到注册页面')

    def save(self):
        print('欢迎来到存储页面')



# 之前
def choose_01():
    u = User()
    while True:
        choose = input('>>>').strip()
        if choose == 'login':
            u.login()
        elif choose == 'register':
            u.register()
        elif choose == 'save':
            u.save()

# choose_01()


# 之后
def choose_02():
    u = User()
    while True:
        choose = input('>>>').strip()
        if hasattr(u, choose):
            func = getattr(u, choose)
            if callable(func):
                func()
            else:
                print(func)

# choose_02()




