import socket

# 服务端

sock = socket.socket(type=socket.SOCK_DGRAM)     # UDP类型的socket对象
sock.bind(('127.0.0.1', 9001))                   # 绑定自己的IP、port
print('服务已启动。。。')
while True:
    data, addr = sock.recvfrom(1024)              # 等待接受数据 当设置的接收数据的大小 小于用户发送的数据大小 会出错
    print(addr, data.decode())


