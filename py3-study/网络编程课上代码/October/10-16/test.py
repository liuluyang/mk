# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/15 16:03



import struct


"""
找到num的最大值
"""

# num = 2147483647
num = 2147000000
while True:
    r = struct.pack('i', num)
    print(num, r)
    num += 1
