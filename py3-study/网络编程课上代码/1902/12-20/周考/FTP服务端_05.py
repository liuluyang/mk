# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/17 10:34


import socket
import json
import os
import subprocess
import re
import hashlib


BasePath = os.path.dirname(os.path.abspath(__file__))
common_dir = os.path.join(BasePath, '公共文件')
home_dir = os.path.join(BasePath, 'home')
info_dir = os.path.join(BasePath, 'info')

dir_list = [common_dir, home_dir, info_dir]
ADDRESS = ('192.168.1.1', 9000)


"""
路径问题：配置文件的路径都需要绝对路径
    建立连接：
        未登录：
            环境变量：公共文件夹
        登录之后：
            环境变量：自己的家目录
            
    与目录有关的操作：
        上传、下载文件 =》当前环境变量之下
        
        登录、注册 =》查询、写入信息文件（需要绝对路径）
"""


class FTPServer:

    def __init__(self):
        for dir in dir_list:
            if not os.path.exists(dir):
                os.mkdir(dir)

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


def check_login(is_login=1):
    """
    检查登录状态
    :param func:
    :return:
    """
    def outer(func):
        def inner(*args, **kwargs):
            self = args[0]
            if self.is_login != is_login:
                status = '登录' if self.is_login else '未登录'
                head = {'msg':'%s状态下，此功能不可用！'%(status)}
                self.send_head(head)
                return

            return func(*args, **kwargs)

        return inner

    return outer


class Connection:

    allowed_commands = [
        'cd', 'mkdir', 'ipconfig', 'dir'
    ]

    def __init__(self, conn, address):
        self.conn = conn
        self.address = address
        self.is_login = False
        self.username = None
        self.path = None

        # 切换路径到公共文件
        os.chdir(os.path.join(common_dir))

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
        print('等待数据。。。')
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
        filepath = filename

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
        filepath = filename
        with open(filepath, 'wb') as f:
            for line in self.recv_body(filesize):
                f.write(line)

        print('文件接收完毕')

    def parse_command(self, command):
        """
        检查命令
        :param command:
        :return:
        """
        if command.startswith('cd'):
            command += ' &dir'
            return command
        for c in self.allowed_commands:
            if command.startswith(c):
                return command

        return

    def cmd(self):
        """
        执行命令
        :return:
        """
        command = self.head['command']

        command = self.parse_command(command)
        if not command:
            head = {'msg': '此命令暂不支持！'}
            self.send_head(head)
            return

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
            path = path.groups()[0].strip()
            if path.startswith(str(self.path)) or path.startswith(common_dir):
                os.chdir(path)
            else:
                head = {'msg': '非法操作！'}
                self.send_head(head)
                return

        data = err if err else out
        data = data if data else '命令执行成功'

        head = {'msg':data}
        self.send_head(head)

    def change_path(self, name):
        """
        路径切换
        :param name:
        :return:
        """
        self.path = os.path.join(home_dir, name)
        os.chdir(self.path)

    @check_login(1)
    def logout(self):
        """
        注销
        :return:
        """
        self.is_login = False
        self.username = None
        self.path = None

        # 切换路径到公共文件
        os.chdir(os.path.join(common_dir))
        head = {'msg': '注销成功'}
        self.send_head(head)

    @check_login(0)
    def login(self):
        """
        登录
            统计已经注册的用户
                判断是否已注册
                    是：
                        判断密码是否正确
                            是：
                                改变登录状态 True
                                发送消息 登录成功
                            不是：
                                发送消息
                    否：
                        发送消息
        :return:
        """
        exist_username = set(os.listdir(info_dir))

        username, password = self.head['username'], self.head['password']
        if username in exist_username:
            with open(os.path.join(info_dir, username), 'r', encoding='utf8') as f:
                if self.md5_hex(password) == f.read().split()[-1]:
                    head = {'msg': '登录成功'}
                    self.is_login = True
                    self.username = username
                    # 修改环境变量
                    self.change_path(username)
                    self.send_head(head)
                    return

        head = {'msg': '账号或密码错误', 'status': 'ERROR'}
        self.send_head(head)

    @check_login(0)
    def sign(self):
        """
        注册：
            统计已经注册的用户
                判断是否已注册
                    是：
                        发送消息 已注册
                    否：
                        信息写入文件
                        发送消息 注册成功
        :return:
        """
        exist_username = set(os.listdir(info_dir))

        username, password = self.head['username'], self.head['password']
        if username in exist_username:
            head = {'msg': '用户名已被注册', 'status':'ERROR'}
            self.send_head(head)
        else:
            # 创建信息文件
            with open(os.path.join(info_dir, username), 'w', encoding='utf8') as f:
                f.write('%s %s'%(username, self.md5_hex(password)))
            # 创建用户的家目录
            os.mkdir(os.path.join(home_dir, username))

            head = {'msg':'注册成功'}
            self.send_head(head)

    def md5_hex(self, password):
        """
        密码加密
        :param password:
        :return:
        """
        r = hashlib.md5(password.encode()).hexdigest()

        return r

    def common(self):
        """
        切换到公共目录
        :return:
        """
        os.chdir(common_dir)
        head = {'msg':'切到公共目录'}
        self.send_head(head)

    @check_login()
    def home(self):
        """
        切换到家目录
        :return:
        """
        os.chdir(os.path.join(home_dir, self.username))
        head = {'msg':'切到家目录'}
        self.send_head(head)

    def help(self):
        """
        帮助信息
        :return:
        """
        head = {'msg': '这是帮助信息'}
        self.send_head(head)

    def main(self):
        """
        主函数
        :return:
        """
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
                else:
                    head = {'status':'ERROR', 'msg':'此功能未实现。。。'}
                    self.send_head(head)

            except Exception as e:
                print('服务器出错', e)
                self.conn.close()
                break


if __name__ == '__main__':
    ftp =FTPServer()
    ftp.run()
    pass