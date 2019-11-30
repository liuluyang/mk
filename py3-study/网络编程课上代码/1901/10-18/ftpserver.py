# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/18 14:34

import socket


"""
精确接收数据
"""

# def server():
#     sock = socket.socket()
#     sock.bind(("0.0.0.0", 9000))
#     sock.listen(1)
#
#     conn, addr = sock.accept()
#     print("welcome...", addr)
#     head_len = conn.recv(20).decode()
#     head_len = int(head_len)
#     print(head_len)
#
#     head_data = conn.recv(head_len)
#     print(len(head_data))
#     print(head_data.decode())
#
#     head_len = conn.recv(20).decode()
#     head_len = int(head_len)
#     print(head_len)
#
#     head_data = conn.recv(head_len)
#     print(len(head_data))
#     print(head_data)

def func():
    sock=socket.socket()
    sock.bind(('0.0.0.0',9000))
    sock.listen(5)
    try:
        conn,address=sock.accept()
        print('连接成功',address)
        while True:
            date=conn.recv(20)
            date_len=int(date.decode())
            details=b""
            while True:
                date_details=conn.recv(1024)
                print(date_details)
                details += date_details
                if len(details)==date_len:
                    break
            print(details.decode())

    except:pass


def tcp_server():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 9000))
    sock.listen(5)
    print('服务已启动。。。')
    while True:
        print('等待连接...')
        conn, address = sock.accept()
        print('来客人了', address)
        while True:
            try:
                print('等待消息。。。')
                data_size = conn.recv(20)
                if not data_size:
                    conn.close()
                    print('断开连接', address)
                    break
                datasize=int(data_size.decode())
                time,remainder=divmod(datasize,1024)
                data=b''
                for i in range(time):
                    msg=conn.recv(1024)
                    # print(len(msg), msg)
                    data+=msg
                else:
                    data+=conn.recv(remainder)
                    # print(len(data), data)
                print(data.decode())
            except Exception as e:
                print('错误：', e)
                conn.close()
                break

def tcp_server_new():
    sock = socket.socket()
    sock.bind(('0.0.0.0', 9000))
    sock.listen(5)
    print('服务已启动。。。')
    while True:
        print('等待连接...')
        conn, address = sock.accept()
        print('来客人了', address)
        while True:
            try:
                print('等待消息。。。')
                data_size = conn.recv(20)
                if not data_size:
                    print('断开连接', address)
                    break
                datasize=int(data_size.decode())

                data = b''
                recv_size = 1024
                last_size = datasize
                while True:
                    if last_size <= recv_size:
                        recv_size = last_size
                    if last_size == 0:
                        break
                    recv_data = conn.recv(recv_size)
                    last_size -= len(recv_data)
                    data += recv_data

                print(data.decode())
            except Exception as e:
                print('错误：', e)
                conn.close()
                break

if __name__ == '__main__':
    tcp_server_new()
    # tcp_server()
    # func()
    # server()