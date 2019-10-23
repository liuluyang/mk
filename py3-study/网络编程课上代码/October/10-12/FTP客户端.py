# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/12 15:43

import socket
import struct
import subprocess
import os
import json
import time


class FTPClient:
    """
    命令：
    sign liu 123456
    login liu 123456
    put t.txt
    get t.txt

    cd
    dir
    mkdir
    """

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

    def sign(self):

        head_data = {'action_type':'sign',
                     'username':self.commands[1],
                     'password':self.commands[2]
                     }
        self.send_head(head_data)
        self.recv_data()
        pass

    def login(self):

        head_data = {'action_type': 'login',
                     'username': self.commands[1],
                     'password': self.commands[2]
                     }
        self.send_head(head_data)
        self.recv_data()
        pass

    def put(self):

        head_data = {'action_type': 'put',
                     'filename': None,
                     'filesize': None
                     }
        self.send_head(head_data)
        self.recv_data()
        pass

    def get(self):
        pass

    def cmd(self):



        pass

    def send_head(self, data):

        data_bytes = json.dumps(data).encode()
        head_len = struct.pack('i', len(data_bytes))
        self.socket.send(head_len)
        self.socket.send(data_bytes)

    def recv_data(self):

        head_struct = self.socket.recv(4)
        if not head_struct: return

        head_len = struct.unpack('i', head_struct)[0]
        head_json = self.socket.recv(head_len).decode()
        head_dict = json.loads(head_json)
        print(head_dict['msg'])

        return head_dict

    def main(self):

        while True:
            try:
                command = input('>>>').strip()
                if not command:
                    continue
                if command == 'q':
                    self.socket.close()
                    break

                self.commands = command.split()
                action_type = self.commands[0]
                if hasattr(self, action_type):
                    func = getattr(self, action_type)
                    func()
                else:
                    self.cmd()
            except Exception as e:
                print('error:', e)
        pass

    def run(self):
        pass


if __name__ == '__main__':
    client = FTPClient()
    client.main()
    pass

