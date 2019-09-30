# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/26 10:40


def gcd(num, den):
    # if den == 0:
    #     num, den = den, num
    while num != 0:
        print(num, den)
        num, den = den % num, num

    return den


# print(gcd(124, 4))


"""
栈
class Stack:

    def __init__(self): pass

    def pop(self): 拿
    
    def push(self): 放

last in first out
LIFO
"""
class StackError(ValueError):
    pass

class Stack:

    def __init__(self):
        self.lst = []

    def push(self, obj):
        """
        压栈
        :param obj:
        :return:
        """
        self.lst.append(obj)

    def pop(self):
        """
        出栈
        :return:
        """
        if self.is_empty:
            raise StackError('栈为空')
        return self.lst.pop()

    @property
    def is_empty(self):
        return self.lst == []

    def __str__(self):
        return str(self.lst)


# stack = Stack()
# for i in range(1, 7):
#     stack.push(i)
# print(stack.is_empty)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack)








