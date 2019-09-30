# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/20 9:10


class User:

    def login(self):
        print('欢迎来到登录页面')

    def register(self):
        print('欢迎来到注册页面')

    def save(self):
        print('欢迎来到存储页面')


# def choose_01():
#     u = User()
#     while True:
#         choose = input('>>>').strip()
#         if choose == 'login':
#             u.login()
#         elif choose == 'register':
#             u.register()
#         elif choose == 'save':
#             u.save()

# choose_01()

def choose_01():
    u = User()
    while True:
        choose = input('>>>').strip()
        if hasattr(u, choose):
            fun = getattr(u, choose)
            print(fun)
            fun()

# choose_01()