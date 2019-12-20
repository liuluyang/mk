# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/14 9:00


import socket


tcp_socket = socket.socket()

tcp_socket.connect(('192.168.1.1', 9000))
# tcp_socket.connect(('192.168.1.1', 9000))

tcp_socket.send(b'111111111')
tcp_socket.close()

while True:
    pass