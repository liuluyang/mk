# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/18 14:35


import socket
import time

def tcp_client():
    sock = socket.socket()
    sock.connect(('192.168.1.1', 9000))

    res_01 = ('你好哇'*1200 + '111').encode()
    res_02 = ('李银河'*4000 + '222').encode()
    print(len(res_01), len(res_02))

    sock.send(str(len(res_01)).zfill(20).encode())
    # sock.send(res_01)
    for i in range(3):
        time.sleep(1)
        sock.send(('你好哇'*400 + '1').encode())
    sock.send(str(len(res_02)).zfill(20).encode())
    sock.send(res_02)

    sock.close()

if __name__ == '__main__':
    tcp_client()