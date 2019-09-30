#coding:utf8


"""
基础学习
"""

"""
变量赋值
变量名 = 变量值
命名规则：
1.变量名只能是 字母、数字或下划线的任意组合

2.变量名的第一个字符不能是数字

3.大小写敏感

4.以下关键字不能声明为变量名
[‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, 
‘del’, ‘elif’, ‘else’, ‘except’, ‘exec’, ‘finally’, ‘for’, 
‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, 
‘not’, ‘or’, ‘pass’, ‘print’, ‘raise’, ‘return’, ‘try’, 
‘while’, ‘with’, ‘yield’]
"""
import keyword

# 正确的命名
name = 1
_name = 2
name_1 = 3
N2 = 4
# 错误命名
# and = 1
# 2t = 1

# 我是单行注释
"""
我是注释
第二行
描述某行、某段、某块代码的作用
"""

"""
整数int
浮点float
"""
# a = 10
# b = 30
# result = a * b  # 求积
# print(a * b)
#
# f = 10.3
# print(f)

"""
布尔值bool
True => 非零以及非空字符串、字典、元组、列表、集合
False => 0以及空字符串、字典、元组、列表、集合
"""
# result_2 = True
# result_3 = False
# print(result_2, result_3)

"""
空值：None
"""
# result_4 = None
# print(result_4)

"""
输入函数
"""
# my_name = input('输入名字：')
# print(my_name)
# my_age = input('输入年龄：')
# print(my_age)


"""
注意：
单行执行代码前面无空格
代码执行顺序-由上至下依次执行
"""
