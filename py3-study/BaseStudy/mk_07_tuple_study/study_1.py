#coding:utf8

"""
元组学习
"""
"""
注：
元组为不可变对象
元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
"""

tuple_1 = ('hello', 'python', 'world', 'list')
tuple_2 = ()
tuple_3 = (1,)
tuple_4 = tuple()

# # 获取长度
# print(len(tuple_1))

# 取值
# print(tuple_1[0])
# print(tuple_1[1])
# print(tuple_1[0:8])
# print(tuple_1[:])
# print(tuple_1[:-1])
# print(tuple_1[::-1])

# 拼接
tuple_1_new = tuple_1 + ('new_word',)
print(tuple_1_new)

# # 判断
# print('hello' in tuple_1)

"""
元组的操作
"""
# tuple_do_list = [func for func in dir(tuple) if not func.startswith('__')]
# for index, f in enumerate(tuple_do_list, start=1):
#     print(index, f)

# print(tuple_1.count('a'))
# print(tuple_1.index('a'))

"""
元组方法
1 count
2 index
"""



