


"""
列表生成式
map函数
匿名函数
高阶函数
"""


########################################### 列表生成式

# 生成新列表
# lst_new = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         lst_new.append(i)


# 生成新列表的另一种方式
# lst_new = [i for i in range(1, 101) if i % 2 == 0]
#
# print(lst_new)


############################################ map 内置函数 高阶函数

"""
模仿map函数的功能
"""
lst = [1, 2, 3]

def func_test(x):

    return x * 2


def map_new(func, item):

    lst_new = []
    for i in item:
        i_new = func(i)
        lst_new.append(i_new)

    return lst_new


# print(callable(func_test))
lst_new = map_new(func_test, lst)
print(lst_new)


# lst_new = map(func_test, lst)
# print(list(lst_new))


############################################ 匿名函数 功能简单


func_mini = lambda x, y : x * y

func_mini_02 = lambda item : item[0]

# print(func_mini(2, 3))

# print(func_mini_02([1, 2, 3]))


info = [['a小黑', 170], ['z小白', 180], ['b小红', 165], ['c刘海柱', 185]]
nums = [1, 2, 3, 5, 4]
# reverse默认是False 正序   True代表倒序
# key参数需要传一个函数 来制定排序的规则
# info.sort(key=lambda x:x[-1], reverse=True)
# info.sort()
# nums.sort(reverse=True)
# print(info)
# print(nums)




