# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/11 13:44

import socket
import uuid

for i in range(100):
    print(uuid.uuid1())


hostname = socket.gethostname()
print(hostname)
print(socket.gethostbyname(hostname))
host_list = socket.gethostbyname_ex(hostname)
print(host_list)
#
# ip = [ip for ip in host_list[-1] if '192.168.1.' in ip][0]
# print(ip)

# sock = socket.socket(type=socket.SOCK_DGRAM)
# address = (ip, 1902)
#
# sock.bind(address)
#
#
# sock.sendto('上线'.encode(), address)
#
# print(sock.recvfrom(1024))