# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/23 15:16


import socket
import time


sock = socket.socket()                # 实例化对象
sock.connect(('192.168.1.25', 9001))  # 连接ip/port

# 任意一端等待数据时 如果一方异常断开(手动强制关闭服务) 另一方会抛出异常
# 所以如果要保证程序健壮 需要捕获异常
# 如果正常结束 对方会收到一个空字符串 可以通过这个判断对方结束连接 然后结束自己的连接

# 尽量不要主动发空字符串 虽然看似发送成功 但数据并未发送 所以对方不会收到数据
# 如果接下来两端都recv的话 两端都会处于等待接收数据状态

while True:
    data = input('>>>').strip()
    if not data:
        continue
    if data == 'q':
        sock.close()
        break
    sock.send(data.encode())

    recv = sock.recv(1024)          # 等待数据时 如果对方异常断开 会抛出异常
    print(recv.decode())