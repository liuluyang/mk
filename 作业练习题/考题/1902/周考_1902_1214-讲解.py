# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/16 10:48



import socket
import time


bufsize = 1024

def recv_data(conn, data_size):
    """
    接收数据
    :param conn:
    :param data_size:
    :return:
    """
    data = b''

    while data_size:

        if data_size >= bufsize:
            d = conn.recv(bufsize)
        else:
            d = conn.recv(data_size)

        data += d
        data_size -= len(d)

    return data


def recv_data_02(conn, data_size, bufsize=1024 * 8):
    """
    接收数据
    迭代器方式
    :param conn:
    :param data_size:
    :return:
    """
    while data_size:
        bufsize = bufsize if data_size >= bufsize else data_size
        d = conn.recv(bufsize)
        if not d:
            break
        data_size -= len(d)

        yield d


def server():

    tcp = socket.socket(type=socket.SOCK_STREAM)

    tcp.bind(('192.168.1.1', 9000))

    tcp.listen(5)

    con, address = tcp.accept()

    while True:
        data_len = con.recv(10)
        if not data_len:
            print('断开连接')
            con.close()
            break

        data_len = int(data_len.decode())
        data_all = recv_data(con, data_len)

        print(data_all.decode())


if __name__ == '__main__':

    server()
    pass