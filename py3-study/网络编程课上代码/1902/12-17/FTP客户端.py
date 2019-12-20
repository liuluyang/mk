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

    def recv_data(self, data_size, bufsize=1024 * 8):
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

    def main(self):

        command = input('请输入指令：')

        # 头部信息
        head = {'filename':command}

        # 发送头部信息
        head_json = json.dumps(head).encode()
        self.socket.send(str(len(head_json)).zfill(20).encode())
        self.socket.send(head_json)

        # 接收数据
        head_len = int(self.socket.recv(20).decode())

        head_data = self.recv_data(head_len)
        head_dict = json.loads(b''.join(head_data).decode())

        filename, filesize = head_dict['filename'], head_dict['filesize']
        filepath = os.path.join(self.download_dir, filename)

        with open(filepath, 'wb') as f:
            for line in self.recv_data(filesize):
                f.write(line)

        print('文件接收完毕')



if __name__ == '__main__':

    ftp = FTPClient()
    ftp.main()
    pass





















