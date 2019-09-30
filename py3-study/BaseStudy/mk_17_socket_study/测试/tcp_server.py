# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/23 15:12


import socket
import time

sock = socket.socket()            # 实例化对象
sock.bind(('192.168.1.25', 9001)) # 绑定ip/port
sock.listen(1)                    # 监听

while True:
    conn, addr = sock.accept()    # 等待连接
    print('来客人了',addr)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print('结束')
                break
            print('recv:', data.decode())        # 打印收到的数据
            conn.send('收到：'.encode() + data)  # 把数据发送给对方

            # conn.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
            # conn.send("<h1 style='color:red'>Hello, data</h1>".encode("utf8"))
            # conn.close()
            # break
        except Exception as e:
            print('error:', e)
            break

