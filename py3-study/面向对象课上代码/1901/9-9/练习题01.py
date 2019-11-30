# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/9 9:00


"""
第一题：
num = 3
nums = [3, 6, 12, 24]
nums = [3, 6, 9, 15, 24, 39]
"""
def func_00():
    num = 3
    nums = [num, num*2]
    for i in range(10):
        nums.append(nums[-1] + nums[-2])
    print(nums)
    pass
func_00()

def func_01(num, length):

    nums = [num]
    for i in range(length-1):
        num *= 2
        nums.append(num)

    return nums

# func_01(3, 4)


"""
第二题：
s = 'ccdddaafllppppee'
s_new = 'c2d3a2f1'
"""

def func_02(res):

    data = {}
    s_new = ''
    for s in res:
        if s not in data:
            data[s] = 1
        else:
            data[s] += 1

    for k,v in data.items():
        s_new += k + str(v)
    print(s_new)
    return s_new

def func_03(res):

    s_new = ''
    for s in set(res):
        c = res.count(s)
        s_new += s + str(c)
    print(s_new)

# s = 'jfahfdjkashfjkahuiewhuasfjkasjkdhn'
# s = '你ccdddaafllppppee我+'
# # func_02(s)

"""
第三题：
n01 = [1]
n02 = [1, 1]
n03 = [1, 2, 1]
n04 = [1, 3, 3, 1]
n05 = [1, 4, 6, 4, 1]
n06 = [1, 5, 10, 10, 5, 1]
"""

def fun_04(nums):
    """
    :param nums:
    :return:
    """
    lst = []
    for index in range(len(nums)-1):
        lst.append(nums[index]+nums[index+1])
    lst = [1] + lst + [1]

    return lst

def fun_05(num):
    """
    :return:
    """
    lst = []
    n01 = [1]

    for i in range(num-1):
        # yield n01
        lst.append(n01)
        r = fun_04(n01)
        n01 = r

    return lst

# f = fun_05(500)
# print(f)












