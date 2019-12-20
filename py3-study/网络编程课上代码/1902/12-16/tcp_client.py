# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/16 10:49

import socket
import time

tcp = socket.socket(type=socket.SOCK_STREAM)

tcp.connect(('192.168.1.1', 9000))

# tcp.send('你好哇'.encode())

tcp.send('9'.zfill(10).encode())
for i in '你好':
    time.sleep(1)
    tcp.send(i.encode())

tcp.send('哇'.encode() + '9'.zfill(10).encode())
for i in '李银河':
    tcp.send(i.encode())
    time.sleep(1)

tcp.close()