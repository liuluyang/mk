

"""
第一题：
给出一个数字num 找规律 然后返回相应的列表
num = 3
1. nums = [3, 6, 12, 24]
2. nums = [3, 6, 9, 15, 24, 39]
"""
def func_01(num, length):
    """
    第一题 第一个列表
    :param num:
    :param length:
    :return:
    """

    nums = [num]
    for i in range(length-1):
        num *= 2
        nums.append(num)

    return nums


def func_02(num):
    """
    第一题 第二个列表
    :param num:
    :return:
    """
    nums = [num, num*2]
    for i in range(10):
        nums.append(nums[-1] + nums[-2])

    return nums


"""
第二题：
根据给出的字符串res，生成res_new
res = 'ccdddaafllppppee'
res_new = 'c2d3a2f1'
"""

def func_03(res):
    """
    第二题 方法一
    :param res:
    :return:
    """
    data = {}
    res_new = ''
    for s in res:
        if s not in data:
            data[s] = 1
        else:
            data[s] += 1

    for k,v in data.items():
        res_new += k + str(v)

    return res_new


def func_04(res):
    """
    第二题 方法二
    :param res:
    :return:
    """
    res_new = ''
    for s in set(res):
        c = res.count(s)
        res_new += s + str(c)

    return res_new


"""
第三题：
找规律打印相应的列表
n01 = [1]
n02 = [1, 1]
n03 = [1, 2, 1]
n04 = [1, 3, 3, 1]
n05 = [1, 4, 6, 4, 1]
n06 = [1, 5, 10, 10, 5, 1]
"""

def fun_05(nums):
    """
    给出一个列表，按规律生成下一个列表
    :param nums:
    :return:
    """
    lst = []
    for index in range(len(nums)-1):
        lst.append(nums[index]+nums[index+1])
    lst = [1] + lst + [1]

    return lst

def fun_06(num):
    """
    主函数
    num : 控制生成多少行
    :return:
    """
    lst = []
    nums_last = [1]

    for i in range(num):
        # yield nums_last                # 可变成生成器函数
        lst.append(nums_last)
        nums_last = fun_05(nums_last)

    return lst












