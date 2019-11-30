# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/10/10 11:30


import socket
import subprocess

ip_port = ('0.0.0.0', 9000)
tcp_socket_server = socket.socket()
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

while True:
    conn, addr = tcp_socket_server.accept()
    print('客户端', addr)

    while True:
        try:
            cmd = conn.recv(1024).decode().strip()
        except:
            break

        print("recv cmd:", cmd)

        if not cmd: break

        if cmd.startswith('shutdown'):
            conn.send('3'.zfill(20).encode())
            conn.send('滚'.encode())
            continue

        res = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        stderr = res.stderr.read().decode('GBK')
        stdout = res.stdout.read().decode('GBK')

        send_data = stderr if stderr else stdout
        send_data = send_data.encode()
        data_length = len(send_data)

        # 发送数据长度
        conn.send(str(data_length).zfill(20).encode())
        # 发送数据
        conn.send(send_data)