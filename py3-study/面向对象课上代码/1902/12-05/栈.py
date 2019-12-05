# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/5 14:36



"""
class Stack:
    pass


属性：
    栈的大小  stack_len

方法：
    压栈（入栈） push
    出栈         pop
    是否为空     is_empty
    查看最外面的元素  top

"""
class StackError(ValueError):
    pass

class Stack:

    def __init__(self, size=1000):
        self.__lst = []
        self.__size = size

    def push(self, obj):
        """
        压栈
        :param obj:
        :return:
        """
        if len(self.__lst) >= self.__size:
            raise StackError('栈已满')
        self.__lst.append(obj)

    def pop(self):
        """
        出栈
        :return:
        """
        if self.is_empty:
            raise StackError('栈为空')
        return self.__lst.pop()

    @property
    def top(self):
        """
        查看栈顶元素
        :return:
        """
        if self.is_empty:
            raise StackError('栈为空')
        return self.__lst[-1]

    @property
    def is_empty(self):
        """
        栈是否为空
        :return:
        """
        return self.__lst == []

    def __str__(self):
        """

        :return:
        """
        return str(self.__lst)
