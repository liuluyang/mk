# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/10 13:54

from tkinter import *
from tkinter import font
import threading
import time

import socket

hostname = socket.gethostname()
host_list = socket.gethostbyname_ex(hostname)
ip = [ip for ip in host_list[-1] if '192.168.1.' in ip][0]
ADDRESS = (ip, 1902)

udp = socket.socket(type=socket.SOCK_DGRAM)
udp.bind(ADDRESS)
for i in range(1, 255):
    udp.sendto('上线'.encode(), ('192.168.1.%s' % (i), 1902))
# udp.sendto('你好'.encode(), ADDRESS)

root = Tk()
root.title("群聊")
root.geometry("800x600+100+100")


# 滚动条设置
s1 = Scrollbar(root)
s1.pack(side=RIGHT, fill=Y)
# HORIZONTAL 设置水平方向的滚动条，默认是竖直
s2 = Scrollbar(root, orient=HORIZONTAL)
s2.pack(side=BOTTOM, fill=X)

# 创建文本框 显示聊天内容
# wrap 设置不自动换行
ft1 = font.Font(size=20)
textpad = Text(root, width=50, height=10, yscrollcommand=s1.set, xscrollcommand=s2.set, wrap='none', font=ft1)
textpad.pack()

s1.config(command=textpad.yview)
s2.config(command=textpad.xview)

def clear_text():
    """
    清除内容
    :return:
    """

    textpad.delete('1.0', 'end')

# 清除文本框按钮
bu = Button(root, text='清空', command=clear_text)
bu.pack(side=TOP)


# 创建文本框 输入聊天内容
# wrap 设置不自动换行
textpad2 = Text(root, width=50, height=5, wrap='none', font=ft1)
textpad2.pack(pady=5)

def send_text():
    """
    发送内容
    :return:
    """
    msg = textpad2.get('1.0', 'end')
    textpad2.delete('1.0', 'end')

    for i in range(1, 255):
        udp.sendto(msg.encode(), ('192.168.1.%s'%(i), 1902))


# 清除文本框按钮
bu2 = Button(root, text='发送', command=send_text)
bu2.pack(side=TOP)

############################################
def push_text(text, udp):
    """
    显示聊天内容
    :param text:
    :return:
    """

    # index = 0
    # while True:
    #     text.insert(INSERT, '%s你好 李银河'%(str(index).zfill(3))+'\n')
    #     text.see(END)  # 一直显示最新的一行
    #     # text.update()
    #     time.sleep(0.8)
    #     index += 1
    #     # if index%2 == 0:
    #     #     text.delete('1.0', 'end')

    while True:
        try:
            msg, address = udp.recvfrom(1024*8)
            msg = msg.decode()
            msg = '%s>>>'%(address[0]) + msg + '\n'

            text.insert(INSERT, msg)
            text.see(END)  # 一直显示最新的一行
        except Exception as e:
            pass
            # print('error', e)

t = threading.Thread(target=push_text, args=(textpad, udp))
t.daemon = True
t.start()
##############################################


if __name__ == '__main__':
    root.mainloop()
    udp.close()