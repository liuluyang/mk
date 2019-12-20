# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/19 16:51


def f(tag):
    def denerator(func):

        def inner(*args, **kwargs):

            print(func.__name__, args, tag)


            return func(*args, **kwargs)

        return inner

    return denerator

class T:

    def __init__(self):

        self.tag = 1

    @f(1)
    def walk(self, name):

        print('walking.......', name)



t = T()
t.walk('tom')