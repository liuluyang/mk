# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/9 14:25


import socket
import time

sock = socket.socket(type=socket.SOCK_DGRAM)
# sock.bind(('0.0.0.0', 9002))
while True:

    for i in range(1, 18):
        sock.sendto('哈喽'.encode(), ('192.168.1.%s'%(i), 9000))      # 数据需要编码， 地址 端口
        # d = sock.recvfrom(5024)
        # print(d[0].decode())
    time.sleep(1)