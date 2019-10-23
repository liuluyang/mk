

"""
第一题：10
tcp/ip五层模型分别指的哪几层
"""

"""
第二题：10
说一说tcp/ip五层模型里面你所知道的每层都有哪些协议
"""

"""
第三题：10
说一说IP跟port(端口)在网络中的作用分别是什么
"""

"""
第四题：10
说一说你对UDP、TCP协议的理解，以及他们的区别
"""

"""
第五题：10
创建两个UDP、TCP协议类型的socket实例化对象，并且写出这些对象都有哪些方法
"""

"""
第六题：10
什么是粘包问题？有什么样的解决方案？UDP有粘包问题吗？
"""

"""
第七题：10
写一个tcp协议的服务端和客户端，实现可以让两边一人一句的聊天
"""

"""
第八题：15
根据下面的客户端代码，写一个服务端，把数据准确的接收并打印
"""
import socket

def tcp_client():
    sock = socket.socket()
    sock.connect(('192.168.1.1', 9000))

    res_01 = ('你好哇'*1300 + '111').encode()
    res_02 = ('李银河'*2000 + '222').encode()

    sock.send(str(len(res_01)).zfill(20).encode())
    sock.send(res_01)
    sock.send(str(len(res_02)).zfill(20).encode())
    sock.send(res_02)

    sock.close()


"""
第九题：15
import struct
struct.pack('i', 2312)

说一下pack函数的作用，并写个算法找出该函数所能接收参数的最大值
提示：最大值的范围0 至 256**4-1
"""

"""
第十题：20
写个客户端把你的月考文件上传到服务端

服务端信息：
ip:192.168.1.1
port:8000
1.先接收头部长度信息20字节
2.在接收字典信息 {'filename':'', 'filesize':'', 'action_type':'put'}
3.接收文件数据
"""







