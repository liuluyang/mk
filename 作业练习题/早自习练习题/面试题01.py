


"""
1.把下面两个变量值交换，不借助新的变量

a = 1
b = 2
"""
# a = 1
# b = 2
# a, b = (b, a)


"""
2.下面代码的执行结果？

a = [1, 2, 3]
b = a
a = 1
print(b)
"""
# a = [1, 2, 3]
# b = a
# a = 1
# print(b)


"""
3.下面代码的执行结果？

class Person:
    x = 1

class Child_01(Person):
    pass

class Child_02(Person):
    pass

print(Person.x, Child_01.x, Child_02.x)

Child_01.x = 2
print(Person.x, Child_01.x, Child_02.x)

Person.x = 3
print(Person.x, Child_01.x, Child_02.x)
"""

# class Person:
#     x = 1
#
# class Child_01(Person):
#     pass
#
# class Child_02(Person):
#     pass
# # 1 1 1
# print(Person.x, Child_01.x, Child_02.x)
#
# Child_01.x = 2
# # 1 2 1
# print(Person.x, Child_01.x, Child_02.x)
#
# Person.x = 3
# # 3 2 3
# print(Person.x, Child_01.x, Child_02.x)


"""
4.print()/input()函数的底层实现？
实现这两个函数
"""


"""
5.说出A0到A6的结果

A0 = dict(zip(('a'，'b'，'c'，'d'，'e')，(1，2，3，4，5)))
2. A1 = range(10)                   # 0-9
3. A2 = [i for i in A1 if i in A0]  # []
4. A3 = [A0[s] for s in A0]         # [1，2，3，4，5]
5. A4 = [i for i in A1 if i in A3]  # [1，2，3，4，5]
6. A5 = {i:i*i for i in A1}         #
7. A6 = dict([[i，i*i] for i in A1])#
"""


"""
6.说出下面代码的执行结果
for i in range(5, 0, -1):
    print(i)
"""
# for i in range(5, 0, 1):
#     print(i)


"""
7.写一个生成器函数
来实现range()函数的功能

range(10)
range(2, 22) range(22, 2)
range(2, 22, 2) range(2, 22, -2)
range(22, 2, -2) range(22, 2, 2)
"""


"""
8.说出下面代码的执行结果

lst = []
for i in range(10):
    lst.append({'num':i})
print(lst)

lst = []
dic = {'num':0}
for i in range(10):
    dic['num'] = i
    lst.append(dic)
print(lst)
"""
# lst = []
# for i in range(10):
#     lst.append({'num':i})
# print(lst)

# lst = []
# dic = {'num': 0}
# for i in range(10):
#     dic['num'] = i
#     lst.append(dic)
# print(lst)


"""
9.实现int()函数
"""

