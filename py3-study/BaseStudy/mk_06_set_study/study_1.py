#coding:utf8

"""
集合学习
"""
"""
注：
集合为可变对象
集合（set）是一个无序的不重复元素序列。
主要作用：数据去重

可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

set_1 = {1, 2, 3, 4, 'hello', 'python', 'python'}
set_2 = set()
list_new = [1, 2, 1, 'word']
set_3 = set(list_new)

print(set_1, set_2, set_3)

# # 获取长度
# print(len(set_1))

"""
增加、删除元素
"""
# set_1.add(5)
# set_1.update((4,7))
# set_1.pop()
# print(set_1)
# set_1.remove(5)  #删除不存在的元素会报错
# print(set_1)

# # 判断
# print('hello' in set_1)

# # 差集、合集、交集
# print(set_1 - set_3)  #差集
# print(set_1 | set_3)  #合集
# print(set_1 & set_3)  #交集

"""
集合的操作
"""
# dict_do_list = [func for func in dir(set) if not func.startswith('__')]
# for index, f in enumerate(dict_do_list, start=1):
#     print(index, f)

# print(set_1.difference(set_3))


"""
集合方法
1 add
2 clear
3 copy
4 difference
5 difference_update
6 discard
7 intersection
8 intersection_update
9 isdisjoint
10 issubset
11 issuperset
12 pop
13 remove
14 symmetric_difference
15 symmetric_difference_update
16 union
17 update
"""



