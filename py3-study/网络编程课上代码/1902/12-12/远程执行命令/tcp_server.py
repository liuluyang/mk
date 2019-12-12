# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/11 14:44


import socket
import subprocess
import os
import re
import time


def execut_cmd(cmd):

    cmd = cmd.strip()
    if cmd.startswith('cd'):
        cmd += ' &dir'

    # 第一个参数是执行的命令
    res = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                           )

    out = res.stdout.read().decode('GBK')   # 正确信息读取
    err = res.stderr.read().decode('GBK')   # 错误信息读取

    if cmd.startswith('cd') and out:
        path = re.search('(.+)的目录', out)
        os.chdir(path.groups()[0].strip())

    return err if err else out


tcp_sock = socket.socket()

tcp_sock.bind(('192.168.1.1', 9005))

# 开始监听
# backlog:监听队列的数量 <=1时默认等待连接的队列长度是1
tcp_sock.listen(20)
print('服务已启动。。。')

# 等待连接 阻塞的操作
# 获取连接对象和远程地址
while True:
    print('#'*20)
    print('等客人。。。')
    con, address = tcp_sock.accept()
    print('来客了：', address)

    while True:
        try:
            # 注：接收到空数据 代表对方正常关闭连接
            data = con.recv(1024*3)
            if not data:
                print('客人走了。。。', address)
                con.close()
                break
            print('收到的数据：', data.decode())
            send_data = execut_cmd(data.decode())
            if not send_data:
                send_data = '命令执行成功'

            data_encode = send_data.encode()

            con.send(str(len(data_encode)).zfill(20).encode())

            con.send(data_encode)
            # print(data_encode[:])
            # for index, i in enumerate(data_encode):
            #     con.send(data_encode[index:index+1])
            #     time.sleep(0.01)

        except Exception as e:
            print('error', e)
            break















