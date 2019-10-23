# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/14 10:07


import socket
import os
import json


class FTPClient:

    def __init__(self):

        while True:
            try:
                ip = input('IP:')
                port = int(input('PORT:'))
                self.socket = socket.socket()
                self.socket.connect((ip, port))
                break
            except Exception as e:
                print('error:', e)

    def send_data(self, head_data):

        head_encode = json.dumps(head_data).encode()
        head_len = len(head_encode)

        # 发送头部信息数据的大小
        self.socket.send(str(head_len).zfill(20).encode())
        # 发送头部数据
        self.socket.send(head_encode)

    def recv_data(self):

        # 接收头部信息数据的大小
        head_len = self.socket.recv(20)
        head_len = int(head_len.decode())
        # 接收头部数据
        head_data = self.socket.recv(head_len)
        head_data = json.loads(head_data.decode())
        print(head_data['msg'])

        return head_data

    def get(self):

        filename = self.commands[1]

        # 发送头部信息
        head_data = {'filename': filename, 'action_type':'get'}
        self.send_data(head_data)

        # 接收头部信息
        head_dict = self.recv_data()
        if head_dict['status'] != 'OK':
            return
        filename = head_dict['filename']
        filesize = head_dict['filesize']

        recvd_len = 0
        with open(filename, 'wb') as f:
            while True:
                recv_data = self.socket.recv(1024)
                f.write(recv_data)
                recvd_len += len(recv_data)
                if recvd_len == filesize:
                    break
            print('文件接收完毕')

    def put(self):

        filepath = self.commands[1]
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        # print(filename, filesize, filepath)

        # 发送头部信息
        head_data = {'filename': filename, 'filesize': filesize, 'action_type':'put'}
        self.send_data(head_data)

        # 发送文件
        with open(filepath, 'rb') as f:
            for line in f:
                self.socket.send(line)
            print('发送完毕')

        self.recv_data()

    def login(self):

        # 发送头部信息
        username = self.commands[1]
        password = self.commands[2]
        head_data = {'username': username, 'password': password, 'action_type': 'login'}
        self.send_data(head_data)

        self.recv_data()

    def sign(self):

        # 发送头部信息
        username = self.commands[1]
        password = self.commands[2]
        head_data = {'username': username, 'password': password, 'action_type': 'sign'}
        self.send_data(head_data)

        self.recv_data()

    def cmd(self):

        head_data = {'action_type': 'cmd', 'command':' '.join(self.commands)}
        self.send_data(head_data)

        self.recv_data()

    def zip(self):

        dirname = self.commands[1]
        head_data = {'action_type': 'zip', 'dirname': dirname}
        self.send_data(head_data)

        self.recv_data()

    def unzip(self):

        zipname = self.commands[1]
        head_data = {'action_type': 'unzip', 'zipname': zipname}
        self.send_data(head_data)

        self.recv_data()

    def main(self):

        while True:
            try:
                cmd = input('>>>').strip()
                if cmd == 'q':
                    self.socket.close()
                    break

                self.commands = cmd.split()

                action_type = self.commands[0]
                if hasattr(self, action_type):
                    fun = getattr(self, action_type)
                    fun()
                else:
                    self.cmd()
            except Exception as e:
                print('客户端出错：', e)


if __name__ == '__main__':
    client = FTPClient()
    client.main()
    pass
