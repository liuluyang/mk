# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/11 14:44


import socket
import time

# 创建TCP协议的socket对象
tcp_sock = socket.socket()

# 建立连接
# ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
tcp_sock.connect(('192.168.1.1', 9005))

# 发送数据
# 注：空数据发送不出去
tcp_sock.send('我是黑寡妇'.encode())

time.sleep(10)
# 关闭连接
tcp_sock.close()

