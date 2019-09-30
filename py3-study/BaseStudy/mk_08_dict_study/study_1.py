#coding:utf8

"""
字典学习
"""
"""
注：
字典为可变对象
列表里面的key需要是不可变对象，value值不做限制

d = {key1 : value1, key2 : value2 }
"""

dict_1 = {'name':'小绿', 'age':20, 'city':'河北', 'phone':'150'}
dict_2 = {}
dict_3 = dict()

print(dict_1, dict_2, dict_3)

# # 获取长度
# print(len(dict_1))

# # 取值
# print(dict_1['name'])
# # print(dict_1.get('name_'))

"""
删除、增加、修改元素
"""
# dict_1['age'] = 22
# dict_1['age_other'] = 22
# print(dict_1)
# del dict_1['name']  #删除键
# dict_1.clear()      #清空字典
# del dict_1          #删除字典
# name = dict_1.pop('nam', None)  #删除并返回
# print(name)
# print(dict_1)


# # 判断
# print('hello' in dict_1)

"""
字典的操作
"""
# dict_do_list = [func for func in dir(dict) if not func.startswith('__')]
# for index, f in enumerate(dict_do_list, start=1):
#     print(index, f)

# for k,v in dict_1.items():
#     print(k, v)
#
# for k in dict_1.keys():
#     print(k)


"""
字典方法
1 clear
2 copy
3 fromkeys
4 get
5 items
6 keys
7 pop
8 popitem
9 setdefault
10 update
11 values
"""



