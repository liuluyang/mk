# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/11 9:09


import socket

"""
第一步：
# 实例化一个socket对象  udp协议
"""
udp_sock = socket.socket(type=socket.SOCK_DGRAM)

"""
第二步：
# 服务端 绑定IP和端口
"""
udp_sock.bind(('192.168.1.1', 9000))
print('服务已启动。。。')

"""
第三步：
# 接收数据 是一个阻塞的操作
# bufsize:一次接收数据的大小 单位：字节
# 如果发送的数据大于接收的大小 服务端会出现错误
"""

while True:
    try:
        msg, address = udp_sock.recvfrom(1024*8)
        print('接收到的数据：', msg.decode(), address)
    except Exception as e:
        print('error:', e)