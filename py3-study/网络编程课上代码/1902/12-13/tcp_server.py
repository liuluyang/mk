# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/13 10:05


import socket


tcp_socket = socket.socket()

tcp_socket.bind(('192.168.1.1', 9099))

tcp_socket.listen(10)
print('服务已启动。。。')

while True:
    conn, address = tcp_socket.accept()
    try:
        data = conn.recv(1024)
        print(data.decode(), address)
        conn.close()
    except Exception as e:
        print('错误：', e, address)