import socket
import time

sock = socket.socket(type=socket.SOCK_DGRAM)  # UDP类型的socket对象
ip_port = ('127.0.0.1', 9001)                 # 服务方IP、port

while True:

    with open('python之禅.txt', 'rb') as f:
        data = f.read()
        print(len(data))
        sock.sendto(data, ip_port)
    while True:
        data = input('请输入：')
        sock.sendto(data.encode(), ip_port)


