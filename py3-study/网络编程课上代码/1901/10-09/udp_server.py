# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/9 14:16

import socket
import time

sock = socket.socket(type=socket.SOCK_DGRAM)    # UDP协议
sock.bind(('0.0.0.0', 9000))                  # 绑定监听的地址
print('服务启动。。。')
while True:
    try:
        data, address = sock.recvfrom(5024)                      # 等待接收数据 接收大小小于发送数据大小会出错
        print(data.decode(), address)
        # time.sleep(5)
        # sock.sendto(data, address)
    except:
        pass

