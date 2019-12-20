# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/17 10:34


import socket
import json
import os


class FTPServer:

    common_dir = '公共文件'
    ADDRESS = ('192.168.1.1', 9000)

    def __init__(self):

        if not os.path.exists(self.common_dir):
            os.mkdir(self.common_dir)

        self.socket = socket.socket()
        self.socket.bind(self.ADDRESS)
        self.socket.listen(5)
        print('服务已启动。。。', self.ADDRESS)

        while True:
            conn, address = self.socket.accept()
            print('新的连接：', address)
            self.main(conn, address)

    def recv_data(self, conn, data_size, bufsize=1024 * 8):
        """
        接收数据
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

    def main(self, conn, address):

        # 接收数据
        head_len = int(conn.recv(20).decode())

        head_data = self.recv_data(conn, head_len)
        head_dict = json.loads(b''.join(head_data).decode())

        filename = head_dict['filename']
        filepath = os.path.join(self.common_dir, filename)

        # 发送头部信息
        head = {'filename':filename, 'filesize':os.path.getsize(filepath)}
        head_json = json.dumps(head).encode()
        conn.send(str(len(head_json)).zfill(20).encode())
        conn.send(head_json)

        # 发送文件
        with open(filepath, 'rb') as f:
            for line in f:
                conn.send(line)

        print('文件发送完毕')


if __name__ == '__main__':
    ftp =FTPServer()
    # ftp.main()
    pass

























