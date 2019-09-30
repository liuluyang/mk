

"""

程序异常处理
"""

name = '小绿'
age = 20

# result = name + age
# # result = age + name
# print(result)

"""
简单异常处理
"""
# try:
#     result = name + age
#     print('程序执行成功')
# except:
#     print('程序错误')

"""
捕获指定的异常
"""
# try:
#     #result = name + age
#     # print('h'[1])
#     print('程序执行成功')
# except TypeError:
#     print('类型错误')
# except IndexError:
#     print('取值错误')

"""
捕获所有异常并打印异常信息
"""

# try:
#     print('h'[1])
#     print('程序执行成功')
# except Exception as e:
#     print('错误信息：', e)

"""
自定义异常类
异常的传递过程
"""
class MyException(Exception):
    pass

try:
    raise MyException('我的自定义异常')
except Exception as e:
    print(e)
    print(e.args)

"""
不要过度使用异常，不用用它代替正常流程控制
try里面的代码块不宜过大
不可忽略异常
"""
