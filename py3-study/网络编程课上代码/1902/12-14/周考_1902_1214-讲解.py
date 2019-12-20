


"""
周考
"""

"""
第一题：10
tcp/ip五层模型分别指的哪几层
"""


"""
第二题：10
说一说tcp/ip五层模型里面你所知道的每层都有哪些协议或者设备
"""


"""
第三题：10
说一说IP跟port(端口)在网络通信中的作用分别是什么
"""


"""
第四题：10
说一说你对UDP、TCP协议的理解，以及他们的区别
"""


"""
第五题：10
1、创建两个UDP、TCP协议类型的socket实例化对象，
2、写出这两个对象都有哪些学过的方法，并简单解释它们的作用
"""
import socket

udp_socket = socket.socket(type=socket.SOCK_DGRAM)
# udp_socket.bind(('192.168.1.1', 9000))
# udp_socket.sendto(b'1', ('192.168.1.1', 9000))
# udp_socket.recvfrom(1024)

tcp_socket = socket.socket()
# tcp_socket.settimeout(5)
# tcp_socket.bind(('192.168.1.1', 9000))
# tcp_socket.listen(5)
# tcp_socket.connect(('192.168.1.1', 9000))
# tcp_socket.accept()
# tcp_socket.recv(1024)
# tcp_socket.send(b'1')


"""
第七题：10
写一个tcp协议的服务端和客户端，实现可以让两边一人一句的聊天
注：
    服务需要做异常处理
"""


"""
第八题：10
根据下面的客户端代码，写一个服务端，把数据准确的接收并打印
注：只可以修改IP
"""
import socket

def tcp_client_08():

    sock = socket.socket()
    sock.connect(('192.168.1.1', 9000))

    res_01 = ('你好哇'*1300 + '111').encode()

    sock.send(str(len(res_01)).zfill(10).encode())
    sock.send(res_01)

    sock.close()


"""
第九题：10
根据下面的客户端代码，写一个服务端，把数据准确的接收并打印
注：只可以修改IP
"""
import socket

def tcp_client_09():

    sock = socket.socket()
    sock.connect(('192.168.1.1', 9000))

    res_01 = ('你好哇'*1300 + '111').encode()
    res_02 = ('李银河'*2000 + '222').encode()

    sock.send(str(len(res_01)).zfill(10).encode())
    sock.send(res_01)
    sock.send(str(len(res_02)).zfill(10).encode())
    sock.send(res_02)

    sock.close()


"""
第十题：10
至少写三个在socket编程过程中常见的异常，
写出异常类型及异常内容，并解释异常发生的原因
"""
"""
OverflowError: getsockaddrarg: port must be 0-65535.
OSError: [WinError 10022] 提供了一个无效的参数。
OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，
或该用户用于接收数据报的缓冲区比数据报小。

ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
ConnectionResetError: [WinError 10054] 远程主机强迫关闭了一个现有的连接。
OSError: [WinError 10056] 在一个已经连接的套接字上做了一个连接请求。
OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。
"""

"""
附加题：20
根据下面的客户端代码，写一个服务端，把数据准确的接收并打印
注：只可以修改IP
"""
import socket
import time

def tcp_client_11():
    sock = socket.socket()
    sock.connect(('192.168.1.1', 9000))

    res_01 = (('你好哇'*400 + '1')*3).encode()
    res_02 = ('李银河'*2000 + '222').encode()

    sock.send(str(len(res_01)).zfill(10).encode())
    sock.send(res_01)
    for i in range(3):
        time.sleep(1)
        sock.send(('你好哇'*400 + '1').encode())
    sock.send(str(len(res_02)).zfill(10).encode())
    sock.send(res_02)

    sock.close()





