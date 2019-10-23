# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/9 15:56


import socket
import time

sock = socket.socket()

sock.connect(('192.168.1.1', 9000))           # 建立连接

sock.send('哈喽1'.encode())                   # 发送数据

time.sleep(10000)
sock.close()