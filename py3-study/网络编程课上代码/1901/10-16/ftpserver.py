# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/12 12:43

from socketserver import ThreadingTCPServer
import threading
import multiprocessing
import socket
import struct
import subprocess
import os
import json
import time

"""
解决当头部数据较大时 如何准确接收头部数据
"""


BasePath = os.path.dirname(os.path.abspath(__file__))
HomePath = os.path.join(BasePath, 'home')
InfoPath = os.path.join(BasePath, 'info')
Address = ('0.0.0.0', 8000)
RecvSize = 2048


class FTPServer:

    def __init__(self):
        self.socket = socket.socket()
        self.socket.bind(Address)
        self.socket.listen(5)

    def run(self):
        if not os.path.exists(HomePath):
            os.makedirs(HomePath)
        if not os.path.exists(InfoPath):
            os.makedirs(InfoPath)
        print('服务已启动。。。', Address[0], Address[1])
        while True:
            conn, address = self.socket.accept()
            print('来客人了：', address)

            # 多进程版本
            # t = multiprocessing.Process(target=Connection, args=(conn, address))
            # t.start()

            # 多线程版本 有共享环境变量的问题
            # t = threading.Thread(target=Connection, args=(conn, address))
            # t.start()

            # 单线程版本
            Connection(conn, address)


class Connection:

    def __init__(self, conn, address):
        self.conn = conn
        self.address = address
        self.is_login = False
        self.path = None

        # 启动主函数
        self.main()

    def recv_data(self):

        # 接收头部信息数据的大小
        head_len = self.conn.recv(20)
        print(head_len)
        if not head_len: return

        head_len = int(head_len.decode())

        # 接收头部数据
        head_data = b''
        num, last_size = divmod(head_len, RecvSize)
        for i in range(num):
            recv_data = self.conn.recv(RecvSize)
            head_data += recv_data
        head_data += self.conn.recv(last_size)

        # head_data = self.conn.recv(head_len)
        # print(len(head_data))

        head_data = json.loads(head_data.decode())
        print(head_data['msg'])

        return head_data

    def main(self):

        while True:
            # try:
                data = self.recv_data()
                if not data:
                    print('断开连接', self.address)
                    self.conn.close()
                    break
            # except Exception as e:
            #     print('error', e)

        pass


if __name__ == '__main__':
    ftpserver = FTPServer()
    ftpserver.run()