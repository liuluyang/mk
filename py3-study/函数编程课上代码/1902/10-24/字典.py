

"""
字典

特性：
    可变的数据类型
    key是不可变的数据类型
    查询速度快

"""

staff_list = [
    
["miller", 23, "CEO", "88888"],
["黑姑娘", 24, "行政", "55555"],
["liuser", 25, "讲师", "44444"],
["egon", 33, "组长", "77777"],

]

# for info in staff_list:
#     if info[0] == '黑姑娘':
#         print(info)

# 创建 key:value

staff_dict = {

    "miller":["miller", 23, "CEO", "88888"],
    "黑姑娘":["黑姑娘", 24, "行政", "55555"],
    "liuser":["liuser", 25, "讲师", "44444"],
    "egon":["egon", 33, "组长", "77777"],

}
# 查找*
# print(staff_dict["黑姑娘"])    # key不存在会出错
# print(staff_dict.get("黑姑娘"))# key不存在不会出错

# 增 修改一个不存在的key 相当于增加*
staff_dict["黑姑娘2"] = ["黑姑娘2", 24, "行政", "66666"]
# print(staff_dict)

# 循环*
# for d in staff_dict:
#     print(d)
#
# for d in staff_dict.keys():
#     print(d)
#
# for d in staff_dict.values():
#     print(d)
#
# for name, info in staff_dict.items():
#     print(name, info)

# 创建
# print({}.fromkeys('1234', None))
# 删除
# print(staff_dict.pop("黑姑娘2"))
# print(staff_dict.popitem())

# 批量更新*
# data_new = {"黑姑娘3":["黑姑娘3", 24, "行政", "66666"], "黑姑娘4":["黑姑娘4", 24, "行政", "66666"]}
# staff_dict.update(data_new)

# 当设置的key存在时，修改不会生效，并且返回key对应的value
# 当设置的key不存在时，修改会生效，并且返回设置的值 默认是None
# print(staff_dict.setdefault("黑姑娘3", 111))
# print(staff_dict)










