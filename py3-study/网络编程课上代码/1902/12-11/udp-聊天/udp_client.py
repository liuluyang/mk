# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/11 8:55


import socket


"""
第一步：
# 实例化一个socket对象  udp协议
"""
udp_sock = socket.socket(type=socket.SOCK_DGRAM)

"""
第二步：
# 发送数据 数据类型：字节  大小不能超过65535
"""

def send_data_01():

    while True:
        address = ('192.168.1.1', 9000)
        send_data = input('>>>')
        # 发送给服务端
        udp_sock.sendto(send_data.encode(), address)

        # 接收服务端返回的信息
        recv_data, address_from = udp_sock.recvfrom(1024*8)
        print('来自%s回话：'%(address_from[0]), recv_data.decode())


def send_data_02():

    import time
    f = open('红楼梦.txt', 'r', encoding='utf8')
    while True:
        send_data = f.readline().strip()
        if not send_data:
            continue
        for i in range(1, 255):
            address = ('192.168.1.%s'%(i), 9000)
            # send_data = '这是一条来自未知星球的消息。。。'
            udp_sock.sendto(send_data.encode(), address)

        time.sleep(1)

if __name__ == '__main__':
    pass
    # send_data_02()
    send_data_01()






