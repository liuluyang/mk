# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/9 15:56


import socket
import time

sock = socket.socket()

sock.connect(('192.168.1.1', 9000))
print(11111111111111111111)
sock.send('ipconfig'.encode())
print(2222222222222222222)
# time.sleep(10)
sock.close()