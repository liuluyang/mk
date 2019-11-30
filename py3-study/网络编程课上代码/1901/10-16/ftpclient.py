# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/14 10:07


import socket
import os
import json
import time


class FTPClient:

    def __init__(self):

        while True:
            try:
                ip = '192.168.1.1' #input('IP:')
                port = 8000 #int(input('PORT:'))
                self.socket = socket.socket()
                self.socket.connect((ip, port))
                break
            except Exception as e:
                print('error:', e)

    def send_data(self, head_data):

        head_encode = json.dumps(head_data).encode()
        head_len = len(head_encode)
        print(head_len)

        # 发送头部信息数据的大小
        self.socket.send(str(head_len).zfill(20).encode())
        # 发送头部数据
        self.socket.send(head_encode)

    def main(self):

        data = {'msg':'a'*100000 + '111'}
        self.send_data(data)
        # time.sleep(1)
        data = {'msg': 'b' * 100000 + '222'}
        self.send_data(data)


if __name__ == '__main__':
    client = FTPClient()
    client.main()
    pass
