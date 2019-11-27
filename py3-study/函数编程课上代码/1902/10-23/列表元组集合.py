

"""
列表 元组 集合
"""

# 可变的数据类型
# 增删改查
students = ["冯亚尼", "曹泽涵", "张文哲", "曹怡", "张子涵",
            "李佳伦", "张灿武", "丁明宇", "张鱼洋", "郭利炜",
            "谷宣言", "彭子权", "屈晓明", "张家泽", "张丫丫",
            "高江涛", "尹梦许"]

# 创建
res = 'abcd'
lst = []
# print(list(res))
# print(len(students))

# 增
students.append('小绿')
students.insert(20, '小黑')  # 不报错
students.extend(['小绿', '小红'])
# print(students + ['小绿', '小红'])
# print(students)

# 删
students.remove('小绿')
p = students.pop()  # 不存在的索引位 出现错误
# print(p)
# print(students)

# 改
students[-1] = '小紫'
# print(students)

# 查
# print(students.index('小黑'))
# print(students[10])  # 不存在的索引位 出现错误
# print(students.count('小黑'))
#
# print(students[10:110])
# print(students)
# print(students[10:5:-2])
# print(list(range(10, 100, 5)))

# lst_new = []
# for name in students:
#     lst_new.insert(0, name)
# print(lst_new)


############################################# 元组

# 不可变的数据类型
# 特点：安全 稳定

tuple_new = tuple(students)
tuple_02 = (1,)  # 一个元素的元组 书写方式
print(type(tuple_02))
# print(tuple_new)


################################################ 集合

# 可变的数据类型
# 里面的元素是不可变的
# 去重
# & | - ^

set_new = set()
set_new02 = {1, 2, 1}
# print(set_new02)
# print(type(set_new))

f01 = {'小白', '小黑', '小绿', '小红'}

f02 = {'小蓝', '小黑', '小绿', '小紫'}

# # 差集
# # f01里面有的f02没有
# print(f01 - f02)
# # f02里面有的f01没有
# print(f02 - f01)
#
# # 并集
# print(f01 | f02)
#
# # 交集 共同的好友
# print(f01 & f02)
#
# # 对称差集
# print(f01 ^ f02)


# 增
f01.add('小雪')
f01.add('小白')
print(hash('小白'))
print(f01)

# 删
f01.remove('小白')
print(f01.pop())  # 随机删除一个
print(f01)

print('小白' in f01)
print(len(f01))
















