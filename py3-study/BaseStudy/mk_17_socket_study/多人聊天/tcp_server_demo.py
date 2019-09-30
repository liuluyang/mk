import socket
import threading
import queue
import json
import time

"""
多人聊天服务端
"""

soc = socket.socket()
soc.bind(('0.0.0.0', 9001))
soc.listen(0)
print('服务已启动。。。')


conn_set = set()
q = queue.Queue()


def send_message(q):
    """
    发送消息
    :param q:
    :return:
    """
    global conn_set
    while True:
        data = q.get()
        close_obj = set()
        for c in conn_set:
            try:
                c.send(json.dumps(data).encode())
            except:
                close_obj.add(c)
        conn_set -= close_obj
        print('当前连接数：{}'.format(len(conn_set)))


def recv_message(conn, addr, name, q):
    """
    接收消息
    :param conn:
    :param addr:
    :param name:
    :return:
    """
    data_send = {'addr':addr, 'name':name, 'message':None}
    while True:
        try:
            recv_data = conn.recv(1024)
            data_send['message'] = recv_data.decode()
            q.put(data_send)
        except ConnectionResetError:
            print('{}连接断开'.format(data_send))
            data_send['message'] = '下线'
            q.put(data_send)
            break


t = threading.Thread(target=send_message, args=(q,))
t.start()


while True:
    conn, addr = soc.accept()
    conn_set.add(conn)

    name = conn.recv(1024).decode()
    conn.send('欢迎<{}>加入群聊'.format(name).encode())
    print(addr, name)

    time.sleep(0.5)
    data_send = {'addr': addr, 'name': name, 'message': '上线'}
    q.put(data_send)

    t = threading.Thread(target=recv_message, args=(conn, addr, name, q))
    t.start()
