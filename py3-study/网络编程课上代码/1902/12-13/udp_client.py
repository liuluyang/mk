# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/13 9:06

import socket



sock = socket.socket(type=socket.SOCK_DGRAM)

for i in range(1024, 2**16):

    sock.sendto('乔治'.encode(), ('192.168.1.1', i))

