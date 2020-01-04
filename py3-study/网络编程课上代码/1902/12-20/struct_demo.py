# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/20 9:15


import struct

print(str(1000000).zfill(20).encode())
print(int(2**64/2)-1)
print(2**63-1)
# 把一个一定范围的整数 编码成四个字节
r = struct.pack('q', 2**63-1)

print(r, len(r), type(r))

# 反解
# print(struct.unpack('i', r)[0])


"""
00000000 00000000 00000000 00000000
"""
print(2**32-1)

