#coding:utf8


"""
运算符学习
"""

"""
+ - * /  加减乘除(乘数有浮点结果为浮点，除法结果为浮点)
// %     整除 取余
**       幂运算
"""
a = 15
b = 3
c = 4
# print(a + b + c)
# print(a - b)
# print(a * b)
# print(a / b)
# # 重点
# print(a // c)
# print(a % c)
# print(b ** c)

"""
数字比较运算
== != > < >= <=
注：
== != 也可用于其他类型比较
"""
# print(a >= b)
# print(a != b)

"""
赋值运算
+= -= *= /=  
//= %=    
**=
"""
# a += 10  # a = a + 10  计算之后给a重新赋值
# print(a)

"""
逻辑运算
and or not
not > and > or
如果要改变执行的顺序 那就把低优先级的括起来先执行
"""
# h = 4
# k = 5
# j = 6
# print(1 + 3 * 4 + 6)
# print(h == 5 or k == 9 and k == 5 or j == 6) # h == 5 or (k == 9 and k == 5) or j == 6
# print(h == 5 or k == 9 and (k == 5 or j == 6))
# print((h == 5 or k == 9) and (k == 5 or j == 6))
#
# print(h == 4 or not h == 4 and k == 15)  # h == 4 or ((not h == 4) and k == 5)
# print((h == 4 or not h == 4) and k == 15)

"""
成员运算
in 
not in
"""
# text = 'abc'
# print('a' in text)

"""
身份运算
is # ==
is not # !=
"""
# name = None
# print('a' is 'a')
# print(name is None)







