



import random

# print(random.randrange(1, 10))

nums = [random.randrange(1, 101) for _ in range(10)]
print(nums)


"""
1.求列表nums所有元素的和     nums_all
2.求列表nums所有奇数元素的和 nums_ji
3.求列表nums所有偶数元素的和 nums_ou
4.找出列表nums里面最大的数   nums_max
5.找出列表nums里面最小的数   nums_min
6.找出列表nums里面相同元素分别有多少个 nums_count
7.对列表进行去重             nums_set list(set(nums))
8.删除列表nums里面所有大于10的数（注：不能创建新的列表，需在原列表基础上进行修改。）
9.打印九九乘法表
"""

# 8.删除列表nums里面所有大于10的数（注：不能创建新的列表，需在原列表基础上进行修改。）

# 错误方法
# for n in nums:
#     if n > 10:
#         print(n)
#         nums.remove(n)


# # 第一种方法

# remove_nums = []
# for i in nums:
#     if i > 10:
#         remove_nums.append(i)
# print(remove_nums)
#
# for i in remove_nums:
#     nums.remove(i)


# # 第二种方法

# count = 0
# index = 0
# for i in nums:
#     if i > 10:
#         nums[index] = None
#         count += 1
#     index += 1
#
# print(nums)
# for i in range(count):
#     nums.remove(None)

## 第三种方法

index = 0
for i in range(len(nums)):

    if nums[index] > 10:
        nums.pop(index)
    else:
        index += 1

    print(nums, index)


print(nums)







