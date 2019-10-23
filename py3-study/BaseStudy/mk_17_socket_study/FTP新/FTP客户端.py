

import socket
import os
import json
import struct


RecvSize = 2048
# 头部长度信息的类型
HeadLenType = 1


class BaseFTPClient:

    def __init__(self):
        """
        连接服务端
        """
        while True:
            try:
                ip = input('IP:')
                port = int(input('PORT:'))
                self.socket = socket.socket()
                self.socket.connect((ip, port))
                break
            except Exception as e:
                print('error:', e)

    def send_head_01(self, head_data):
        """

        :param head_data:
        :return:
        """
        head_encode = json.dumps(head_data).encode()
        head_len = len(head_encode)
        self.socket.send(str(head_len).zfill(20).encode())
        self.socket.send(head_encode)

    def recv_head_01(self):
        """

        :return:
        """
        head_len = self.socket.recv(20)
        if not head_len: return

        head_len = int(head_len.decode())
        head_data = b''.join(self.recv_body(head_len))
        head_data = json.loads(head_data.decode())
        # 打印返回信息
        msg = head_data.get('msg')
        if msg:
            print(msg)

        return head_data

    def send_head_02(self, head_data):
        """

        :param head_data:
        :return:
        """
        data_bytes = json.dumps(head_data).encode()
        head_len = struct.pack('i', len(data_bytes))
        self.socket.send(head_len)
        self.socket.send(data_bytes)

    def recv_head_02(self):
        """

        :return:
        """
        head_struct = self.socket.recv(4)
        if not head_struct: return

        head_len = struct.unpack('i', head_struct)[0]
        head_data = b''.join(self.recv_body(head_len))
        head_data = json.loads(head_data.decode())
        # 打印返回信息
        msg = head_data.get('msg')
        if msg:
            print(msg)

        return head_data

    def recv_body(self, bodysize):
        """
        数据接收
        :param bodysize:
        :return:
        """
        recv_size = RecvSize
        last_size = bodysize
        while True:
            if last_size <= recv_size:
                recv_size = last_size
            if last_size == 0:
                break
            recv_data = self.socket.recv(recv_size)
            yield recv_data
            last_size -= len(recv_data)

    def send_head(self, head_data):
        """
        发送头部信息
        :param head_data:
        :return:
        """
        if HeadLenType == 1:
            self.send_head_01(head_data)
        elif HeadLenType == 2:
            self.send_head_02(head_data)

    def recv_head(self):
        """
        接收头部信息
        :return:
        """
        if HeadLenType == 1:
            return self.recv_head_01()
        elif HeadLenType == 2:
            return self.recv_head_02()

    def cmd(self):
        """
        发送cmd命令
        :return:
        """
        head_data = {'command':' '.join(self.commands), 'action_type': 'cmd'}
        self.send_head(head_data)
        self.recv_head()

    def main(self):
        """
        主函数
        :return:
        """
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


class FTPClient(BaseFTPClient):

    def get(self):
        """
        下载文件
        :return:
        """
        filename = self.commands[1]

        # 发送头部信息
        head_data = {'filename': filename, 'action_type':'get'}
        self.send_head(head_data)

        # 接收头部信息
        head_dict = self.recv_head()
        if head_dict['status'] == 'OK':
            filename = head_dict['filename']
            filesize = head_dict['filesize']

            with open(filename, 'wb') as f:
                for recv_data in self.recv_body(filesize):
                    f.write(recv_data)
                print('文件接收完毕')

    def put(self):
        """
        上传文件
        :return:
        """
        filepath = self.commands[1]
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        # 发送头部信息
        head_data = {'filename': filename, 'filesize': filesize, 'action_type':'put'}
        self.send_head(head_data)

        # 发送文件
        with open(filepath, 'rb') as f:
            for line in f:
                self.socket.send(line)
            print('文件发送完毕')

        self.recv_head()

    def login(self):
        """
        登录
        :return:
        """
        username = self.commands[1]
        password = self.commands[2]

        # 发送头部信息
        head_data = {'username': username, 'password': password, 'action_type': 'login'}
        self.send_head(head_data)
        self.recv_head()

    def sign(self):
        """
        注册
        :return:
        """
        username = self.commands[1]
        password = self.commands[2]

        # 发送头部信息
        head_data = {'username': username, 'password': password, 'action_type': 'sign'}
        self.send_head(head_data)
        self.recv_head()

    def zip(self):
        """
        压缩
        :return:
        """
        dirname = self.commands[1]

        # 发送头部信息
        head_data = {'dirname': dirname, 'action_type': 'zip'}
        self.send_head(head_data)
        self.recv_head()

    def unzip(self):
        """
        解压
        :return:
        """
        zipname = self.commands[1]

        # 发送头部信息
        head_data = {'zipname': zipname, 'action_type': 'unzip'}
        self.send_head(head_data)
        self.recv_head()


if __name__ == '__main__':
    client = FTPClient()
    client.main()
