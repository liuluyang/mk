


"""
第一题：
给出一个数 num  注意：给出的num大于1
生成一个列表 num_list = [1, 2, ... num, num-1, ...2, 1]
例1：
num = 9
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
例2：
num = 2
num_list = [1, 2, 1]
"""
def func_01(num):

    nums_01 = list(range(1, num + 1))
    nums_02 = nums_01[::-1][1:]

    return nums_01 + nums_02


"""
第二题：
给出列表lst
lst = [1, 2, 3, 4, 5, 6]
生成列表lst_new,至少用两种方法
lst_new = [2, 4, 6, 8, 10, 12]
"""
lst = [1, 2, 3, 4, 5, 6, 7]

def func_02(lst):

    lst_new = []
    for num in lst:
        lst_new.append(num * 2)

    return lst_new


def func_03(lst):

    lst_new = []
    for index, num in enumerate(lst):
        # lst[index] = num * 2
        lst_new.append(lst[index]*2)

    return lst_new


def func_04():

    # 列表生成式
    lst_new = [num*2  for num in lst]

    return lst_new


def func_05():

    # map函数 匿名函数
    lst_new = list(map(lambda x:x*2, lst))

    return lst_new