


"""
练习题
"""


"""
第一题：
给出一个数 num  注意：给出的num大于0
生成一个列表 num_list
例1：
num = 9
num_list = [9, 9, 18, 27, 45, 72, 117]
例2：
num = 2
num_list = [2, 2, 4, 6, 10, 16, 26]
"""

def func_01(num, size):

    num_list = [num, num]

    for i in range(size - 2):

        last_num = num_list[-1] + num_list[-2]
        num_list.append(last_num)

    return num_list


"""
第二题：
给出一个只含有数字的列表num_list， 和一个数字num
判断这个数字num是否在这个列表num_list里面
如果在返回True 否则返回False
注：不能用in
"""

def func_02(lst, num):

    isTrue = False

    for n in lst:
       if num == n:
           isTrue = True
           break


    return isTrue


def func_03(lst, num):

    for n in lst:
       if num == n:
           # 函数里面遇到return 函数结束
           return True

    return False


"""
第三题：
描述或者展示一下zip函数的用法
如果可以写一个函数来模仿zip函数的功能
"""
