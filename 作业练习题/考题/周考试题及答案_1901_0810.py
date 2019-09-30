import random


nums = [random.randrange(1, 101) for _ in range(100)]
print(nums)
"""
1.求列表nums所有元素的和    nums_all
2.求列表nums所有奇数元素的和 nums_ji
3.求列表nums所有偶数元素的和 nums_ou
4.找出列表nums里面最大的数   nums_max 
5.找出列表nums里面最小的数   nums_min
6.找出列表nums里面相同元素分别有多少个 nums_count
7.对列表进行去重             nums_set

8.删除列表nums里面所有大于10的数（注：不能创建新的列表，需在原列表基础上进行修改。）
9.打印九九乘法表
"""
t = """
1.求列表nums所有元素的和    nums_all
2.求列表nums所有奇数元素的和 nums_ji
3.求列表nums所有偶数元素的和 nums_ou
"""
print(t)
# 方法一
# nums_all = 0
# nums_ji = 0
# nums_ou = 0
# for num in nums:
#     nums_all += num
#     if num % 2 == 1:
#         nums_ji += num
#     else:
#         nums_ou += num
# print('总和：', nums_all)
# # 方法二
# print('总和：', sum(nums))
# print('奇数和：', nums_ji)
# print('偶数和：', nums_ou)


t = """
4.找出列表nums里面最大的数   nums_max 
5.找出列表nums里面最小的数   nums_min
"""
print(t)
# 方法一
# nums_max = nums[0]
# nums_min = nums[0]
# for num in nums:
#     if num > nums_max:
#         nums_max = num
#     elif num < nums_min:
#         nums_min = num
# print(nums_max, nums_min)
# # 方法二
# print(max(nums), min(nums))
# # 方法三
# nums_new = list(set(nums))
# print(nums_new[0], nums_new[-1])


t = """
6.找出列表nums里面相同元素分别有多少个 nums_count
"""
print(t)
# 方法一
# nums_count = dict()
# for num in nums:
#     if num in nums_count:
#         nums_count[num] += 1
#     else:
#         nums_count[num] = 1
# print(len(nums_count), nums_count)
# # 方法二
# nums_count_02 = dict()
# for num in set(nums):
#     nums_count_02[num] = nums.count(num)
# print(len(nums_count_02), nums_count_02)
# print(nums_count == nums_count_02)


t = """
7.对列表进行去重             nums_set
"""
print(t)
# nums_set = set(nums)
# print(nums)


t = """
8.删除列表nums里面所有大于10的数（注：不能创建新的列表，需在原列表基础上进行修改。）
"""
print(t)
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

t = """
9.打印九九乘法表
"""
print(t)
# for i in range(1,10):
#     for y in range(1, i+1):
#         text = '{} * {} = {}'.format(i, y, i*y)
#         print(text, end='\t')
#     print('\n')

