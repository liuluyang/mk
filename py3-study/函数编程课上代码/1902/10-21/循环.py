

"""
六种数据类型
"""
# 数字int
# 字符串str
# 列表list
# 字典dict
# 元组tuple
# 集合set


# 创建字符串
name01 = 'liu'
name02 = "laowang"
text = """
我是多行注释1,
我是多行注释2.
"""

"""
我是多行注释1
我是多行注释2
"""

# print(text)
# print(name02)

# 字符串拼接
res_new = name01 + name02
# print(res_new)


students = ["冯亚尼", "曹泽涵", "张文哲", "曹怡", "张子涵",
            "李佳伦", "张灿武", "丁明宇", "张鱼洋", "郭利炜",
            "谷宣言", "彭子权", "屈晓明", "张家泽", "张丫丫",
            "高江涛", "尹梦许"]
# 循环
# for stu in students:
#     print(stu)

# 字符串拼接
name_all = '*'.join(students)
# print(name_all)

# 索引取值
# print(students[len(students) - 1])
# print(students[-1])

# 模拟join操作
name_all = ''
tag = '*'
num = 0
for stu in students:
    # print('第%s次循环'%(num))
    # print(stu)
    name_all += stu + tag
    # print(name_all)
    num += 1
name_all = name_all[:-1]
# print(name_all)


# 字典操作

new_dict = {2:12, 1:1, 100:1}

# print(new_dict.keys())
# print(new_dict[2])

# v = new_dict[2]
# v += 1
# new_dict[2] = v

# v = new_dict[2]
# v += 1
new_dict[2] = new_dict[2] + 1  # new_dict[2] += 1

print(new_dict)













