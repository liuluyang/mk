# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/10 9:01

import socket

ip, port = input('IP:'), int(input('port:'))
sock = socket.socket()
sock.connect((ip, port))

while True:
    send_data = input('请输入：').strip()

    if not send_data or send_data == 'q':
        sock.close()
        break

    sock.send(send_data.encode())

    print('等待消息。。。')
    recv_data = sock.recv(1024)
    print('收到：', recv_data.decode())