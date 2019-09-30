import socket
import threading
import time
import json

"""
多人聊天客户端
"""

class Client:

    def __init__(self, name='匿名'):
        self.name = name
        self.soc = socket.socket()
        self.soc.connect(('192.168.1.25', 9001))
        self.sockname = list(self.soc.getsockname())
        self.soc.send(name.encode())

    def recv_message(self):
        """
        接收消息
        :return:
        """
        while True:
            recv_data = self.soc.recv(1024)
            recv_data = recv_data.decode()
            if recv_data:
                try:
                    data_json = json.loads(recv_data)
                    addr, name, message = data_json['addr'], data_json['name'], \
                                          data_json['message']
                    if addr != self.sockname:
                        print('来自:{}>>>{}'.format(name, message))
                except:
                    print(recv_data)

    def input_(self):
        """
        输入消息
        :return:
        """
        while True:
            s = input('')
            # if s == 'quit':
            #     self.soc.close()
            #     break
            self.soc.send(s.encode())
            time.sleep(0.5)


def main():
    """
    主函数入口
    :return:
    """
    name = input('请输入名字：')
    name = '匿名' if not name.strip() else name
    c = Client(name=name)
    t = threading.Thread(target=c.recv_message)
    t.start()
    c.input_()


if __name__ == '__main__':
    main()