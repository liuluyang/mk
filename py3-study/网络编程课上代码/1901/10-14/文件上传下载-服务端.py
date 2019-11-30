# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/14 10:37

import multiprocessing
import socket
import os
import json
import time

"""
文件上传下载服务端流程的实现 未做异常处理
"""

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

    def run(self):

        while True:
            conn, address = self.socket.accept()
            print('来客人了：', address)

            t = multiprocessing.Process(target=Connection, args=(conn, address))
            t.start()


class Connection:

    def __init__(self, conn, address):
        self.conn = conn
        self.address = address

        self.main()

    def put(self, head_dict):

        filename = head_dict['filename']
        filesize = head_dict['filesize']
        # 接收文件
        recvd_len = 0
        # time.sleep(10)
        with open(os.path.join(homepath, filename), 'wb') as f:
            while True:
                recv_data = self.conn.recv(1024)
                recvd_len += len(recv_data)
                f.write(recv_data)

                if recvd_len == filesize:
                    break
            print('接收完成')

        head_data = {'status':'OK', 'msg':'文件上传成功'}
        self.send_data(head_data)

    def get(self, head_dict):

        filename = head_dict['filename']
        filepath = os.path.join(homepath, filename)

        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        print(filename, filesize, filepath)

        head_data = {'filename': filename, 'filesize': filesize, 'status':'OK', 'msg':''}
        self.send_data(head_data)

        with open(filepath, 'rb') as f:
            for line in f:
                self.conn.send(line)

    def send_data(self, head_data):

        head_encode = json.dumps(head_data).encode()
        head_len = len(head_encode)

        # 发送头部信息数据的大小
        self.conn.send(str(head_len).zfill(20).encode())
        # 发送头部数据
        self.conn.send(head_encode)

    def recv_data(self):

        # 接收头部信息数据的大小
        head_len = self.conn.recv(20)
        head_len = int(head_len.decode())
        # 接收头部数据
        head_data = self.conn.recv(head_len)
        head_data = json.loads(head_data.decode())

        return head_data

    def main(self):

        while True:
            try:
                head_dict = self.recv_data()

                action_type = head_dict['action_type']

                if hasattr(self, action_type):
                    fun = getattr(self, action_type)
                    fun(head_dict)
            except Exception as e:
                print('error:', e)
                try:
                    head_data = {'status': 'ERROR', 'msg': '服务错误'}
                    self.send_data(head_data)
                except:
                    pass
                break


if __name__ == '__main__':
    server = FTPServer()
    server.run()
    pass
