

import multiprocessing
import socket
import struct
import subprocess
import os
import json
import shutil
import zipfile

# 项目根目录
BasePath = os.path.dirname(os.path.abspath(__file__))
# 所有用户的家目录
HomePath = os.path.join(BasePath, 'home')
# 所有用户信息文件的目录
InfoPath = os.path.join(BasePath, 'info')
# 公共文件目录
CommonPath = os.path.join(BasePath, 'common')
DirPaths = [HomePath, InfoPath, CommonPath]
Address = ('0.0.0.0', 9000)
RecvSize = 2048
# 是否检测登录
IsCheckLogin = False
# 头部长度信息的类型
HeadLenType = 1
# 是否启用多进程
IsMultiprocessing = True


class FTPServer:

    def __init__(self):
        """
        实例化 绑定 监听
        """
        self.socket = socket.socket()
        self.socket.bind(Address)
        self.socket.listen(5)

    def run(self):
        """
        启动函数
        :return:
        """
        for dirpath in DirPaths:
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)
        print('服务已启动。。。', Address[0], Address[1])
        while True:
            conn, address = self.socket.accept()
            print('来客人了：', address)

            if IsMultiprocessing:
                # 多进程版本
                t = multiprocessing.Process(target=Connection, args=(conn, address))
                t.start()
            else:
                # 单线程版本
                Connection(conn, address)


class BaseConnection:

    def __init__(self, conn, address):
        """
        初始化
        :param conn:
        :param address:
        """
        self.conn = conn
        self.address = address
        self.is_login = False
        if IsCheckLogin:
            self.path = None
        else:
            self.path = CommonPath
            os.chdir(self.path)

        # 启动主函数
        self.main()

    def send_head_01(self, head_data):
        """

        :param head_data:
        :return:
        """
        head_encode = json.dumps(head_data).encode()
        head_len = len(head_encode)
        self.conn.send(str(head_len).zfill(20).encode())
        self.conn.send(head_encode)

    def recv_head_01(self):
        """

        :return:
        """
        head_len = self.conn.recv(20)
        if not head_len: return

        head_len = int(head_len.decode())
        head_data = b''.join(self.recv_body(head_len))
        head_data = json.loads(head_data.decode())

        return head_data

    def send_head_02(self, head_data):
        """

        :param head_data:
        :return:
        """
        data_bytes = json.dumps(head_data).encode()
        head_len = struct.pack('i', len(data_bytes))
        self.conn.send(head_len)
        self.conn.send(data_bytes)

    def recv_head_02(self):
        """

        :return:
        """
        head_struct = self.conn.recv(4)
        if not head_struct: return

        head_len = struct.unpack('i', head_struct)[0]
        head_data = b''.join(self.recv_body(head_len))
        head_data = json.loads(head_data.decode())

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
            recv_data = self.conn.recv(recv_size)
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

    def main(self):
        """
        主函数
        :return:
        """
        while True:
            try:
                self.head_dict = self.recv_head()
                if not self.head_dict:
                    print('客人走了：', self.address)
                    self.conn.close()
                    break

                action_type = self.head_dict['action_type']

                if not self.is_login and action_type not in ('sign', 'login') and IsCheckLogin:
                    head_data = {'status': 'ERROR', 'msg': '请先登录'}
                    self.send_head(head_data)
                elif hasattr(self, action_type):
                    func = getattr(self, action_type)
                    func()
                else:
                    head_data = {'status': 'ERROR', 'msg': '错误指令'}
                    self.send_head(head_data)

            except Exception as e:
                print('服务出错：', e)
                head_data = {'status':'ERROR', 'msg':'服务出错'}
                try:
                    self.send_head(head_data)
                    self.conn.close()
                except:
                    pass
                break


class Connection(BaseConnection):

    def switch_path(self, username):
        """
        切换到用户家目录
        :param username:
        :return:
        """
        self.path = os.path.join(HomePath, username)
        os.chdir(self.path)

    def sign(self):
        """
        注册
        :return:
        """
        users = os.listdir(InfoPath)
        username = self.head_dict['username']
        password = self.head_dict['password']

        # 判断账户是否存在
        if username in users:
            head_data = {'status': 'ERROR', 'msg': '用户已存在'}
            self.send_head(head_data)
            return
        # 添加用户信息
        with open(os.path.join(InfoPath, username), 'w', encoding='utf8') as f:
            f.write(username+' '+password)
        # 改变登录状态
        self.is_login = True
        # 创建用户文件夹
        os.makedirs(os.path.join(HomePath, username))
        # 发送成功信息
        head_data = {'status': 'OK', 'msg': '注册成功并登陆'}
        self.send_head(head_data)
        # 切换路径
        self.switch_path(username)

    def login(self):
        """
        登录
        :return:
        """
        # 获取用户名、密码
        username = self.head_dict['username']
        password = self.head_dict['password']

        try:
            # 读取账户信息
            with open(os.path.join(InfoPath, username), 'r', encoding='utf8') as f:
                u, p = f.read().split()
                # 判断账户信息
                if username == u and password == p:
                    self.is_login = True
                    # 发消息
                    head_data = {'status': 'OK', 'msg': '登陆成功'}
                    self.send_head(head_data)
                    # 切换路径
                    self.switch_path(username)
                else:
                    head_data = {'status': 'ERROR', 'msg': '用户名或密码错误'}
                    self.send_head(head_data)
        except:
            head_data = {'status': 'ERROR', 'msg': '用户不存在'}
            self.send_head(head_data)

    def put(self):
        """
        接收上传的文件
        :return:
        """
        filename = self.head_dict['filename']
        filesize = self.head_dict['filesize']

        with open(filename, 'wb') as f:
            for recv_data in self.recv_body(filesize):
                f.write(recv_data)
            print('文件接收成功')

        head_data = {'status': 'OK', 'msg': '文件上传成功'}
        self.send_head(head_data)

    def get(self):
        """
        传输下载的文件
        :return:
        """
        filename = self.head_dict['filename']
        filepath = os.path.join(os.getcwd(), filename)

        if os.path.isfile(filepath):
            filesize = os.path.getsize(filepath)
            head_data = {'status': 'OK', 'msg': '', 'filename':filename, 'filesize':filesize}
            self.send_head(head_data)

            with open(filepath, 'rb') as f:
                for line in f:
                    self.conn.send(line)
                print('文件发送成功')
        else:
            head_data = {'status': 'ERROR', 'msg': '下载的文件不存在'}
            self.send_head(head_data)

    def cmd(self):
        """
        远程cmd命令执行
        :return:
        """
        cmd = self.head_dict['command']

        if cmd.startswith('shutdown'):
            head_data = {'status': 'ERROR', 'msg': '滚犊子'}
            self.send_head(head_data)
            return
        elif cmd == 'cd':
            cmd = 'dir'
        elif cmd == 'cd home':
            cmd = 'cd ' + self.path + ' & dir'
        elif cmd == 'cd common':
            cmd = 'cd ' + CommonPath + '& dir'
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
            # 路径切换限制
            if not path.startswith(self.path) and not path.startswith(CommonPath):
                head_data = {'status': 'ERROR', 'msg': '非法操作'}
                self.send_head(head_data)
                return
            os.chdir(path)

        send_data = stderr if stderr else stdout
        send_data = '命令执行成功' if not send_data else send_data  # 处理命令执行成功但是没有返回值的情况
        head_data = {'status': 'OK', 'msg': send_data}
        self.send_head(head_data)

    def zip(self):
        """
        在线压缩
        :return:
        """
        dirname = self.head_dict['dirname']

        try:
            shutil.make_archive(dirname, 'zip', root_dir=dirname)
            head_data = {'status': 'OK', 'msg': '压缩成功'}
            self.send_head(head_data)
        except Exception as e:
            head_data = {'status': 'ERROR', 'msg': str(e)}
            self.send_head(head_data)

    def unzip(self):
        """
        在线解压
        :return:
        """
        zipname = self.head_dict['zipname']

        try:
            r = zipfile.ZipFile(zipname, 'r')
            r.extractall(zipname.split('.')[0])
            head_data = {'status': 'OK', 'msg': '解压成功'}
            self.send_head(head_data)
        except Exception as e:
            head_data = {'status': 'ERROR', 'msg': str(e)}
            self.send_head(head_data)


if __name__ == '__main__':
    ftpserver = FTPServer()
    ftpserver.run()