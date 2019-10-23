# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/14 10:37


import socket
import os
import json

basepath = os.path.dirname(os.path.abspath(__file__))
homepath = os.path.join(basepath, 'home')


class FTPServer:


    def __init__(self):

        if not os.path.exists(homepath):
            os.makedirs(homepath)

        self.socket = socket.socket()
        self.socket.bind(('0.0.0.0', 8000))
        self.socket.listen(5)
        print('服务已启动。。。')

    def accept(self):

        conn, address = self.socket.accept()

        return conn

    def main(self):

        conn = self.accept()

        # 接收头部信息数据的大小
        head_len = conn.recv(20)
        head_len = int(head_len.decode())
        # 接收头部数据
        head_data = conn.recv(head_len)
        head_data = json.loads(head_data.decode())
        filename = head_data['filename']
        filesize = head_data['filesize']
        # 接收文件
        recvd_len = 0
        with open(os.path.join(homepath, filename), 'wb') as f:
            while True:
                recv_data = conn.recv(1024)
                recvd_len += len(recv_data)
                f.write(recv_data)

                if recvd_len == filesize:
                    break
            print('接收完成')


if __name__ == '__main__':
    server = FTPServer()
    server.main()
    pass
