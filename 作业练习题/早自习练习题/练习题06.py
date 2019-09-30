


"""
实现一个类：
1.让这个类可以像open()函数一样使用
2.文件默认编码是utf8
3.当文件里写入数据时，把写入时间和数据一同写入文件
4.这个类的实例化对象拥有文件对象的所有方法
"""
def open_01(file, mode='r', encoding='utf8'):

    f = open(file, mode=mode, encoding=encoding)

    return f


import time
import datetime

class OpenNew:

    def __init__(self, file, mode='r', encoding='utf8'):
        self.f = open(file, mode=mode, encoding=encoding)

    def write(self, msg):
        time_now = time.strftime('%Y-%m-%d %X')
        self.f.write(time_now + msg)

    def __getattr__(self, item):

        return getattr(self.f, item)


# f = OpenNew('t.txt', 'w')
# f.write('你好哇 李银河')



