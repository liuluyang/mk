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
# for i in range(100):
#     tcp_sock.send('我是王大锤'.encode())
#     time.sleep(1)
#
# time.sleep(10)


while True:
    cmd = input('请输入指令：')

    tcp_sock.send(cmd.encode())

    data_len = tcp_sock.recv(20)
    data_len = int(data_len.decode())
    print('需要接收的数据的大小：', data_len)

    all = b''

    while True:
        recv_data = tcp_sock.recv(1024)
        all += recv_data
        print(len(recv_data))
        if len(all) >= data_len:
            break
    print(all.decode())


# 关闭连接
# tcp_sock.close()

