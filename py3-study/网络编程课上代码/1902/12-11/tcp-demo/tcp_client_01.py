# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/11 14:44


import socket
import time

# 创建TCP协议的socket对象
tcp_sock = socket.socket()

# 建立连接
tcp_sock.connect(('192.168.1.1', 9005))

# 发送数据
# 注：空数据发送不出去
for i in range(100):
    tcp_sock.send('我是王大锤'.encode())
    time.sleep(1)

time.sleep(10)

# 关闭连接
tcp_sock.close()

