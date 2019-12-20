# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/14 8:49


import socket


"""
OverflowError: getsockaddrarg: port must be 0-65535.
OSError: [WinError 10022] 提供了一个无效的参数。
OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，
或该用户用于接收数据报的缓冲区比数据报小。

ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
OSError: [WinError 10056] 在一个已经连接的套接字上做了一个连接请求。
OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。
"""

tcp_sock = socket.socket()
tcp_sock.bind(('192.168.1.1', 9000))

tcp_sock.listen(1)


conn, address = tcp_sock.accept()

print(conn.recv(1023))




