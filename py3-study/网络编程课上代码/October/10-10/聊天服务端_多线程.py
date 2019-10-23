# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/10 8:51



import socket
import threading


sock = socket.socket()
# 绑定端口并监听
sock.bind(('0.0.0.0', 9000))
sock.listen(5)
print('服务已启动。。。')


def fun(conn, address):
    while True:
        # 等待消息 捕获异常
        try:
            # print('等待消息。。。')
            data = conn.recv(1024)
        except Exception as e:
            print('错误：', e)
            conn.close()
            break

        # 结束聊天
        if not data:
            print('聊天结束', address)
            break

        print('收到:', data.decode())
        # send_data = input('请回复：')
        conn.send(data)


while True:
    # 等待连接
    print('等待连接...')
    conn, address = sock.accept()
    print('来客人了', address)
    t = threading.Thread(target=fun, args=(conn, address))
    t.start()

