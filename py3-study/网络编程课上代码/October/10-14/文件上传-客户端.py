# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/14 10:07


import socket
import os
import json


class FTPClient:


    def __init__(self):

        self.socket = socket.socket()
        self.socket.connect(('192.168.1.1', 8000))

        # while True:
        #     try:
        #         ip = input('IP:')
        #         port = int(input('PORT:'))
        #         self.socket = socket.socket()
        #         self.socket.connect((ip, port))
        #         break
        #     except Exception as e:
        #         print('error:', e)

        pass

    def main(self):

        cmd = input('>>>').strip()

        filepath = cmd.split()[1]
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        print(filename, filesize, filepath)

        head_data = {'filename':filename, 'filesize':filesize}
        head_encode = json.dumps(head_data).encode()
        head_len = len(head_encode)
        print(head_len)

        # 发送头部信息数据的大小
        self.socket.send(str(head_len).zfill(20).encode())
        # 发送头部数据
        self.socket.send(head_encode)
        # 发送文件
        with open(filepath, 'rb') as f:
            for line in f:
                self.socket.send(line)



if __name__ == '__main__':
    client = FTPClient()
    client.main()
    pass
