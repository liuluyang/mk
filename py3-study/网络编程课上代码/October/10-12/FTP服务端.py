# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/12 12:43

from socketserver import ThreadingTCPServer
import socket
import struct
import subprocess
import os
import json
import time


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
            conn_obj = Connection(conn, address)
            conn_obj.main()


class Connection:

    def __init__(self, conn, address):
        self.conn = conn
        self.address = address
        self.is_login = False
        self.path = None

    def switch_path(self, username):

        self.path = os.path.join(HomePath, username)
        os.chdir(self.path)
        pass

    def sign(self, head_dict):

        users = os.listdir(InfoPath)
        username = head_dict['username']
        password = head_dict['password']
        if username in users:
            head_data = {'status': 'ERROR', 'msg': '用户已存在'}
            self.send_head(head_data)
            return

        with open(os.path.join(InfoPath, username), 'w', encoding='utf8') as f:
            f.write(username+' '+password)

        self.is_login = True
        os.makedirs(os.path.join(HomePath, username))
        head_data = {'status': 'OK', 'msg': '注册成功并登陆'}
        self.send_head(head_data)
        self.switch_path(username)
        pass

    def login(self, head_dict):

        username = head_dict['username']
        password = head_dict['password']

        try:
            with open(os.path.join(InfoPath, username), 'r', encoding='utf8') as f:
                u, p = f.read().split()
                if username==u and password==p:
                    self.is_login = True
                    head_data = {'status': 'OK', 'msg': '登陆成功'}
                    self.send_head(head_data)
                    self.switch_path(username)
                    return
        except:
            pass

        head_data = {'status': 'ERROR', 'msg': '用户名或密码错误'}
        self.send_head(head_data)

    def put(self, head_dict):

        filename = head_dict['filename']
        filesize = head_dict['filesize']

        recv_size = 0
        with open(filename, 'rb') as f:
            while recv_size < filesize:
                recv_data = self.conn.recv(RecvSize)
                recv_size += len(recv_data)
                f.write(recv_data)
            print('文件上传成功')

        head_data = {'status': 'OK', 'msg': '文件上传成功'}
        self.send_head(head_data)

    def get(self, head_dict):

        filename = head_dict['filename']
        filepath = os.path.join(os.getcwd(), filename)
        if os.path.exists(filepath):
            filesize = os.path.getsize(filepath)
            head_data = {'status': 'OK', 'msg': '', 'filename':filename, 'filesize':filesize}
            self.send_head(head_data)
        else:
            head_data = {'status': 'ERROR', 'msg': '下载的文件不存在'}
            self.send_head(head_data)
            return

        with open(filepath, 'rb') as f:
            for line in f:
                self.conn.send(line)
            print('文件下载成功')

    def cmd(self, head_dict):

        cmd = head_dict['command']

        if cmd.startswith('shutdown'):
            head_data = {'status': 'ERROR', 'msg': '滚犊子'}
            self.send_head(head_data)
            return
        elif cmd == 'cd':
            cmd = 'dir'
        elif cmd.startswith('cd'):
            cmd += ' & dir'

        res = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               cwd = os.getcwd()
                               )

        stderr = res.stderr.read().decode('GBK')
        stdout = res.stdout.read().decode('GBK')

        # 切换路径
        if cmd.startswith('cd') and stdout:
            path = stdout.split('\r\n')[3].split()[0]
            os.chdir(path)

        send_data = stderr if stderr else stdout
        send_data = '命令执行成功' if not send_data else send_data  # 处理命令执行成功但是没有返回值的情况
        head_data = {'status': 'OK', 'msg': send_data}
        self.send_head(head_data)

    def send_head(self, data):

        data_bytes = json.dumps(data).encode()
        head_len = struct.pack('i', len(data_bytes))
        self.conn.send(head_len)
        self.conn.send(data_bytes)

    def recv_data(self):

        head_struct = self.conn.recv(4)
        if not head_struct: return

        head_len = struct.unpack('i', head_struct)[0]
        head_json = self.conn.recv(head_len).decode()
        head_dict = json.loads(head_json)

        return head_dict

    def main(self):

        while True:
            try:
                # head_struct = self.conn.recv(4)
                # if not head_struct: break
                #
                # head_len = struct.unpack('i', head_struct)[0]
                # head_json = self.conn.recv(head_len).decode()
                # head_dict = json.loads(head_json)

                head_dict = self.recv_data()
                if not head_dict:
                    break

                action_type = head_dict['action_type']
                if not self.is_login and action_type not in ('sign', 'login'):
                    head_data = {'status': 'ERROR', 'msg': '请先登录'}
                    self.send_head(head_data)
                elif hasattr(self, action_type):
                    func = getattr(self, action_type)
                    func(head_dict)
            except Exception as e:
                print('服务出错：', e)
                head_data = {'status':'ERROR', 'msg':'服务出错'}
                try:
                    self.send_head(head_data)
                    self.conn.close()
                except:
                    pass
                break


if __name__ == '__main__':
    ftpserver = FTPServer()
    ftpserver.run()