# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/5 9:10


"""


"""


def add(a, b):


    r = a + b

    return r

# print(add(1, 'v'))

# f = open('test', 'r', encoding='utf8')

"""
简单的异常处理
"""

try:
    f = open('test.py', 'r', encoding='utf8')
except:
    # 如果出错 会执行这里面的代码
    print('出错了')

###########################################

"""
捕获所有可能的错误
以及异常信息
"""

try:
    f = open('test.py', 'r', encoding='utf8')
except Exception as e:
    # 如果出错 会执行这里面的代码
    # [Errno 2] No such file or directory: 'test'
    print('出错了', e, type(e), str(e))

"""
捕获相对具体的错误
以及异常信息

捕获异常的顺序：
    小范围
    大范围
"""


try:
    f = open('test.py', 'rhf', encoding='utf8')
    f.read()
except UnicodeDecodeError as e:
    # 如果出错 会执行这里面的代码
    # [Errno 2] No such file or directory: 'test'
    print('出错了', e)
except ValueError as e:
    print('其他错误', e)
except Exception as e:
    print('Exception', e)
else:
    # 没有出错时 会执行这里的代码
    print('没有出错')
finally:
    # 不管出没出错 最后都会执行
    print('到我了')

##########################################


"""
触发异常
"""
# raise ValueError('内容错误')


"""
自定义异常
"""

class MyError(Exception):
    pass

class Child(MyError):

    pass

# raise Child
# raise MyError('自己的异常')
import traceback

try:
    raise AttributeError('属性错误')
except Child:
    print('aaaaaaaa')
except MyError:
    print('bbbbbbbb')
except Exception as e:
    print('ccccccccc', e)
    error_info = traceback.format_exc()
    print(error_info, type(error_info))

















