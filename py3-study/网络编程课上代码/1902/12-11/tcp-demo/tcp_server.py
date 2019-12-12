# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/11 14:44


import socket


tcp_sock = socket.socket()

tcp_sock.bind(('192.168.1.1', 9005))

# 开始监听
# backlog:监听队列的数量 <=1时默认等待连接的队列长度是1
tcp_sock.listen(20)
print('服务已启动。。。')

# 等待连接 阻塞的操作
# 获取连接对象和远程地址
while True:
    print('#'*20)
    print('等客人。。。')
    con, address = tcp_sock.accept()
    print('来客了：', address)

    while True:
        try:
            # 注：接收到空数据 代表对方正常关闭连接
            data = con.recv(1024*3)
            if not data:
                print('客人走了。。。', address)
                con.close()
                break
            print('收到的数据：', data.decode())
            con.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
            con.send("<h1 style='color:red'>Hello, data</h1>".encode("utf8"))
            con.close()
            break
        except Exception as e:
            print('error', e)
            break















