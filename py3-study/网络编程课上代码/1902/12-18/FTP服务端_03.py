# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/17 10:34


import socket
import json
import os
import subprocess
import re


common_dir = '公共文件'
ADDRESS = ('192.168.1.1', 9000)


class FTPServer:

    def __init__(self):

        if not os.path.exists(common_dir):
            os.mkdir(common_dir)

        self.socket = socket.socket()
        self.socket.bind(ADDRESS)
        self.socket.listen(5)
        print('服务已启动。。。', ADDRESS)

    def run(self):
        """
        开始监听
        :return:
        """
        while True:
            conn, address = self.socket.accept()
            print('新的连接：', address)
            c = Connection(conn, address)
            c.main()

class Connection:

    def __init__(self, conn, address):
        self.conn = conn
        self.address = address

    def recv_body(self, data_size, bufsize=1024 * 8):
        """
        接收数据
        :param data_size:
        :return:
        """
        while data_size:
            bufsize = bufsize if data_size >= bufsize else data_size
            d = self.conn.recv(bufsize)
            if not d:
                break
            data_size -= len(d)

            yield d

    def send_head(self, head):
        """
        发送头部信息
        :param head:
        :return:
        """
        head.setdefault('status', 'OK')
        head.setdefault('msg', '')

        head_json = json.dumps(head).encode()
        # 发送长度信息
        self.conn.send(str(len(head_json)).zfill(20).encode())
        # 发送字典信息
        self.conn.send(head_json)

    def recv_head(self):
        """
        接收头部信息
        :return:
        """
        head_len = self.conn.recv(20)
        if not head_len:
            return
        head_len = int(head_len.decode())
        head_data = self.recv_body(head_len)
        head_dict = json.loads(b''.join(head_data).decode())

        return head_dict

    def get(self):
        """
        传输文件
        :return:
        """
        filename = self.head['filename']
        filepath = os.path.join(common_dir, filename)

        if os.path.isfile(filepath):
            head = {'filename': filename, 'filesize': os.path.getsize(filepath)}
            self.send_head(head)
            with open(filepath, 'rb') as f:
                for line in f:
                    self.conn.send(line)

            print('发送完成')
        else:
            head = {'status':'ERROR', 'msg':'文件找不到！'}
            self.send_head(head)

    def put(self):
        """
        接收文件
        :return:
        """
        filename, filesize = self.head['filename'], self.head['filesize']
        filepath = os.path.join(common_dir, filename)
        with open(filepath, 'wb') as f:
            for line in self.recv_body(filesize):
                f.write(line)

        print('文件接收完毕')

    def cmd(self):
        """
        执行命令
        :return:
        """
        command = self.head['command']

        if command.startswith('cd'):
            command += ' &dir'
        elif command.startswith('shutdown'):
            head = {'msg':'滚'}
            self.send_head(head)

        # 第一个参数是执行的命令
        res = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               )

        out = res.stdout.read().decode('GBK')  # 正确信息读取
        err = res.stderr.read().decode('GBK')  # 错误信息读取

        if command.startswith('cd') and out:
            path = re.search('(.+)的目录', out)
            os.chdir(path.groups()[0].strip())

        data = err if err else out
        data = data if data else '命令执行成功'

        head = {'msg':data}
        self.send_head(head)

    def main(self):

        while True:
            try:
                self.head = self.recv_head()
                if not self.head:
                    print('断开连接：', self.address)
                    self.conn.close()
                    break

                action_type = self.head.get('action_type')
                if hasattr(self, action_type):
                    func = getattr(self, action_type)
                    func()

            except Exception as e:
                print('服务器出错', e)
                self.conn.close()
                break


if __name__ == '__main__':

    ftp =FTPServer()
    ftp.run()
    pass

























