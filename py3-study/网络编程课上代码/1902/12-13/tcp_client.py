# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/13 10:11


import socket
import threading


def connect(port):
    try:
        tcp_socket = socket.socket()
        tcp_socket.connect(('192.168.1.1', port))
        tcp_socket.send(('黑旋风' + str(port)).encode())
        tcp_socket.close()
        print(port)
    except:
        print(port, 'pass')
        pass


for port in range(9090, 60000):

    # 多线程版本
    t = threading.Thread(target=connect, args=(port,))
    t.start()
    # 单线程版本
    # connect(port)