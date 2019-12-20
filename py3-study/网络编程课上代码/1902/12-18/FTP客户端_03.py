# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/17 10:34





import socket
import json
import os


class FTPClient:

    download_dir = '下载文件'

    def __init__(self):

        if not os.path.exists(self.download_dir):
            os.mkdir(self.download_dir)

        self.socket = socket.socket()
        while True:
            ip = '192.168.1.1' # input('IP:')
            port = '9000' # input('PORT:')
            try:
                self.socket.connect((ip, int(port)))
                break
            except Exception as e:
                print('连接异常：', e)

    def recv_body(self, data_size, bufsize=1024 * 8):
        """
        接收数据
        :param data_size:
        :return:
        """
        while data_size:
            bufsize = bufsize if data_size >= bufsize else data_size
            d = self.socket.recv(bufsize)
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
        head_json = json.dumps(head).encode()
        # 发送长度信息
        self.socket.send(str(len(head_json)).zfill(20).encode())
        # 发送字典信息
        self.socket.send(head_json)

    def recv_head(self):
        """
        接收头部信息
        :return:
        """
        try:
            head_len = int(self.socket.recv(20).decode())
        except:
            raise ConnectionResetError('服务端关闭连接')

        head_data = self.recv_body(head_len)
        head_dict = json.loads(b''.join(head_data).decode())
        if head_dict.get('msg'):
            print(head_dict.get('msg'))

        return head_dict

    def get(self):
        """
        下载文件
        :return:
        """
        # 头部信息
        head = {'filename': self.commands[-1], 'action_type':'get'}
        self.send_head(head)

        # 接收数据
        head_dict = self.recv_head()

        if head_dict.get('status') != 'ERROR':
            filename, filesize = head_dict['filename'], head_dict['filesize']
            filepath = os.path.join(self.download_dir, filename)
            with open(filepath, 'wb') as f:
                for line in self.recv_body(filesize):
                    f.write(line)

            print('文件接收完毕')

    def put(self):
        """
        上传文件
        :return:
        """
        filepath = self.commands[-1]
        filename = os.path.basename(filepath)
        head = {'filename':filename, 'filesize':os.path.getsize(filepath), 'action_type':'put'}

        self.send_head(head)
        with open(filepath, 'rb') as f:
            for line in f:
                self.socket.send(line)

        print('文件发送完成')

    def cmd(self):
        """
        发送远程命令
        :return:
        """
        head = {'command':' '.join(self.commands), 'action_type':'cmd'}
        self.send_head(head)
        self.recv_head()

    def main(self):
        """
        get filename
        put filename

        :return:
        """
        while True:

            try:
                command = input('请输入指令：').strip()
                if not command:
                    continue
                elif command == 'q':
                    self.socket.close()
                    break

                self.commands = command.split()

                action_type = self.commands[0]
                if hasattr(self, action_type):
                    func = getattr(self, action_type)
                    func()
                else:
                    self.cmd()
            except ConnectionResetError as e:
                print('断开连接：', e)
                self.socket.close()
                break
            except Exception as e:
                print('客户端出错：', e)


if __name__ == '__main__':
    ftp = FTPClient()
    ftp.main()
    pass





















