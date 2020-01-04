# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/31 16:26


from threading import Thread
import queue


# q = queue.Queue()
#
# q.maxsize = 1
#
# # 查看队列已存的数据个数
# print(q.qsize())
# # 是否为空
# print(q.empty())
# q.put(1)
# # 是否满了
# print(q.full())
# q.put(2)


q02 = queue.PriorityQueue()

q02.put((11, 'a'))
q02.put((2, 'b'))

print(q02.get())
