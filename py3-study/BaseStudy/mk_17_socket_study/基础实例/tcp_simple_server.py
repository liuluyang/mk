# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/28 12:10

import socket

sock = socket.socket()              # UDP类型的socket对象
sock.bind(('192.168.1.25', 9001))   # 绑定自己的IP、port
sock.listen(5)                      # 开始监听

conn, addr = sock.accept()       # 等待连接  阻塞状态
print('新连接', conn, addr)
# conn.close()
while True:

    data = conn.recv(1024)        # 等待数据  阻塞状态 ，如果对方异常关闭，这里会触发异常
    print(data.decode())

    if not data:
        print('对方断开', addr)
        conn.close()               # 关闭连接
        break
