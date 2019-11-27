


"""10
1、简述你对类和对象的理解
"""


"""10
2、面向对象的三大特征？并简述自己的理解
"""


"""10
3、__init__函数的作用？self是什么？
"""


"""10
4、定义一个Person类：
    设置name/age都为私有属性
    对外提供查看修改name的接口
"""


"""10
5、定义一个类：
    里面包括类方法和静态方法
"""

"""15
6、实现map()函数
print(list(map(lambda x, y:x*y, [1, 2], (i for i in range(10)))))
"""


"""15
7、扩展一下list类
    限制通过append方法添加的元素必须是字符串，否则报错
"""

"""20
8、完善OpenNew类
    要求以下代码正常执行：
    1. f = OpenNew('t.txt', 'wb') 
    2. f.write('你好哇 李银河') 
    3. f.write(b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x93\x87 \xe6\x9d\x8e\xe9\x93\xb6\xe6\xb2\xb3')
"""

import time
import datetime

class OpenNew:

    def __init__(self, file, mode='r', encoding='utf8'):
        self.f = open(file, mode=mode, encoding=encoding)

    def write(self, msg):
        time_now = time.strftime('%Y-%m-%d %X')
        self.f.write(time_now + msg + '\n')

    def __getattr__(self, item):
        print('找不到方法', item)

        return getattr(self.f, item)


"""20
附加题：可做可不做
8、实现cycle类
"""
from itertools import cycle
import time

# for i in cycle(range(2)):
#     print(i)
#     time.sleep(0.5)