# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/5 14:21


class Base:
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A):
    pass

class D(B):
    pass

class Child(C, D):
    pass

# 多继承时的方法查找顺序
# print(Child.mro())