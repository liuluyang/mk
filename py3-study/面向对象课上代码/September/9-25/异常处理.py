# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/25 11:03


"""
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError 语法错误
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
"""


"""
异常捕获的作用：
    使代码更加健壮，没那么脆弱
"""

"""
异常捕获的语法
"""

# try:
#     f = open('元类1.py', mode='r', encoding='utf8')
#     print(f)
# except: # 捕获所有的错误
#     # 只有try语句块里面出错时， 会执行这里的代码
#     print('出错了')
#     pass
# else:
#     # 只有try语句块里面没出错时， 会执行这里的代码
#     print('没出错')
# finally:
#     # 不管有没有错误， 最后都会执行
#     print('这是我')

# print(2)

############################################
"""
捕获错误 显示错误信息
"""

# try:
#     f = open('元类.py', mode='r', encoding='utf9')
#     print(f)
# except Exception as e: # 捕获所有错误 显示错误信息
#     print('出错了', e, type(e), str(e))
#     pass


#####################################################
"""
捕获指定错误
"""

# try:
#     f = open('元类.py', mode='r1', encoding='utf8')
#     print(f)
# except FileNotFoundError as e: # 捕获具体的错误 显示错误信息
#     print('出错了1', e)
# except LookupError as e:
#     print('出错了2', e)
# except Exception as e:
#     print('其他错误', e)

# f = open('元类1.py', mode='r', encoding='utf8')
# print(f)

# FileNotFoundError
# LookupError

###############################################
"""
1、异常的分类：自定义异常
2、主动触发异常
3、捕获指定异常时的顺序
"""

class MyError(Exception):
    pass

class ChileError(MyError):
    pass

class Chile02(MyError):
    pass

try:
    # raise ChileError('小错误')
    raise MyError('大错误')
except ChileError as e:
    print(e, 1)
except Chile02 as e:
    print(e, 2)
except MyError as e:
    print(e, 3)

# 主动触发异常
# raise MyError('我的异常')
# raise TypeError('你这个。。。')
# raise  ChileError