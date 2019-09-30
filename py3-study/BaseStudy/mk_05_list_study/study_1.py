#coding:utf8

"""
列表学习
"""
"""
注：
列表为可变对象
列表里面的每个元素可以是任何数据类型
"""

list_1 = ['hello', 'python', 'world', 'list']

# # 获取长度
# # print(len(list_1))

# # 取值
# print(list_1[0])
# print(list_1[1])
# print(list_1[0:8])
# print(list_1[:])
# print(list_1[:-1])
# print(list_1[::-1])

# # 拼接
# list_1_new = list_1 + ['new_word']
# print(list_1_new)

"""
删除、修改元素
"""
# list_1[0] = 'first'
# del list_1[0]
# print(list_1)

# 判断
# print('hello' in list_1)

"""
列表的操作
"""
# list_do_list = [func for func in dir(list) if not func.startswith('__')]
# for index, f in enumerate(list_do_list, start=1):
#     print(index, f)

# list_1.remove('hello')
# list_1.append('end')
# list_1.extend([1, 2, 3])
# list_1.pop()
#
# list_2 = [3, 4, 1, 9]
# list_2.sort()
# print(list_2)
# print(list_2.index(3))
#
# print(list_1)


"""
range()函数讲解

列表方法
1 append
2 clear
3 copy
4 count
5 extend
6 index
7 insert
8 pop
9 remove
10 reverse
11 sort

数字列表
sum(list)
min(list)
max(list)
list.sort()
"""



