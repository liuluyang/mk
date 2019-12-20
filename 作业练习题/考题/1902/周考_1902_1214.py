


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





