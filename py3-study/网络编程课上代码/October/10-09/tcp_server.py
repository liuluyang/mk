# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/9 15:53


import socket

sock = socket.socket()
sock.bind(('0.0.0.0', 9000))        # 绑定IP、端口
sock.listen(1)                      # 监听
print('服务启动。。。')

while True:
    conn, address = sock.accept()   # 等待连接
    print('来客了。。', address)

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                print('结束')
                conn.close()
                break
            else:
                print(data.decode(), 'recv')
        except Exception as e:
            print('error', e)
            break
        # try:
        #     data = conn.recv(1024)
        #     print(data.decode(), '1111111111')
        #     # conn.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
        #     # conn.send("<h1 style='color:red'>Hello, data</h1>".encode("utf8"))
        # except Exception as e:
        #     print(e)
        #     pass
        # conn.close()
        # break