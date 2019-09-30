# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/28 12:48

import socket


sock = socket.socket()
sock.connect(('192.168.1.25', 9001))

while True:
    data = input('>>>')
    if data == 'q':
        sock.close()
        break
    sock.send(data.encode())        # 如果连接已经断开，再发生数据会触发异常
