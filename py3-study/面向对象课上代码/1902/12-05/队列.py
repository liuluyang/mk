# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/5 16:52



"""
队列
"""

class QueueError(ValueError):
    pass

class Queue:

    def __init__(self, init_len=8):
        self.__len = init_len
        self.__elems = [0]*init_len
        self.__head = 0
        self.__num = 0

    @property
    def is_empty(self):
        return self.__num == 0

    def head_elem(self):
        if self.is_empty:
            raise QueueError
        return self.__elems[self.__head]

    def pop(self):
        if self.is_empty:
            raise QueueError
        e = self.__elems[self.__head]
        self.__head = (self.__head + 1) % self.__len
        self.__num -= 1

        return e

    def push(self, e):
        if self.__num == self.__len:
            self.__extend()

        self.__elems[(self.__head + self.__num) % self.__len] = e
        self.__num += 1

    def __extend(self):
        old_len = self.__len
        self.__len *= 2
        new_elems = [0]*self.__len
        for i in range(old_len):
            new_elems[i] = self.__elems[(self.__head + i) % old_len]
        self.__elems, self.__head = new_elems, 0

    def info(self):

        return self.__elems

# que = Queue()
# for i in range(20):
#     que.push(i)
# print(que.pop())
# print(que.info())