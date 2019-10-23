# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/10 11:30


import socket

ip_port = ('192.168.1.1', 9000)
s = socket.socket()
s.connect(ip_port)

while True:
    msg = input('>>: ').strip()

    if len(msg) == 0: continue
    if msg == 'quit': break

    s.send(msg.encode('utf-8'))

    # 接收数据长度
    data_length = s.recv(20)
    data_length = int(data_length.decode())
    # 等待执行结果
    data_all = b''
    while True:
        recv_data = s.recv(1024)
        data_all += recv_data
        if len(data_all) == data_length:
            break
    print(data_all.decode())
