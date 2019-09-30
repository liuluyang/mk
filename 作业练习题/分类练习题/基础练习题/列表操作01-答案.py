


"""
1.计算列表中指定元素的个数，并列出它们的索引值
list_01 = ['h', 'e', 'l', 'l', '0', 'h', 'k']
tag =  'h'
"""
# list_01 = ['h', 'e', 'l', 'l', '0', 'h', 'k']
# print('原始列表:', list_01)
# count_num = 0
# index_list = []
# index = 0
# tag = 'h'
# for i in list_01:
#     if i == tag:
#         count_num += 1
#         index_list.append(index)
#     index += 1
#
# print(count_num, index_list)


"""
2.列表反转
list_01 = ['h', 'e', 'l', 'l', '0', 'h', 'k']
==> ['k', 'h', '0', 'l', 'l', 'e', 'h']
注：不能生成新的列表
"""
# list_01 = ['h', 'e', 'l', 'l', '0', 'h', 'k']
# for i in range(len(list_01)//2):
#     index_l = int(i/-1-1)
#     list_01[i], list_01[index_l] = list_01[index_l], list_01[i]
# print(list_01)


"""
nums = [1, 2, 3, 4, 5, 6, 14, 10, 13, 1]

注：不能用内置函数sum()/max()/min()
"""
nums = [1, 2, 3, 4, 5, 6, 14, 10, 13, 1]


"""
3.求列表nums所有元素的和     nums_all
4.求列表nums所有奇数元素的和 nums_ji
5.求列表nums所有偶数元素的和 nums_ou
"""
# nums_all = 0
# nums_ji = 0
# nums_ou = 0
# for num in nums:
#     nums_all += num
#     if num % 2 == 1:
#         nums_ji += num
#     else:
#         nums_ou += num
# print(nums_all, nums_ji, nums_ou)


"""
6.找出列表nums里面最大的数   nums_max 
7.找出列表nums里面最小的数   nums_min
"""
# nums_max = nums[0]
# nums_min = nums[0]
# for num in nums:
#     if num > nums_max:
#         nums_max = num
#     elif num < nums_min:
#         nums_min = num
# print(nums_max, nums_min)


"""
8.找出列表nums里面相同元素分别有多少个 nums_count
"""
# nums_count = dict()
# for num in nums:
#     if num in nums_count:
#         nums_count[num] += 1
#     else:
#         nums_count[num] = 1
# print(nums_count)


"""
9.对列表进行去重             nums_set
"""
# nums_set = set(nums)
# print(nums)


"""
10.删除列表nums里面所有大于10的数（注：不能创建新的列表，需在原列表基础上进行修改。）
"""
# 方法一
# none_nums = 0
# for index_ in range(len(nums)):
#     if nums[index_] > 10:
#         nums[index_] = None
#         none_nums += 1
# print(nums)
# for _ in range(none_nums):
#     nums.remove(None)
# print(nums)
# 方法二
# index_ = -1
# for n in range(len(nums)):
#     if nums[index_] > 10:
#         nums.pop(index_)
#     else:
#         index_ -= 1
# print(nums)