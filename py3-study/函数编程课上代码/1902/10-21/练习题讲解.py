



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


# 1.求列表nums所有元素的和    nums_all
# 2.求列表nums所有奇数元素的和 nums_ji
# 3.求列表nums所有偶数元素的和 nums_ou

nums_all = 0
nums_ou = 0
nums_ji = 0
for n in nums:
    nums_all += n

    if n % 2 == 0:
        nums_ou += n
    else:
        nums_ji += n

nums_ou = 0
nums_ji = 0
for n in nums:
    if n % 2 == 0:
        nums_ou += n
    if n % 2 == 1:
        nums_ji += n

print('总和：', nums_all)
print('偶数和：',nums_ou)
print('奇数和：',nums_ji)


# 4.找出列表nums里面最大的数   nums_max
# 5.找出列表nums里面最小的数   nums_min

nums_max = nums[0]
nums_min = nums[0]
for n in nums:

    if n > nums_max:
        nums_max = n

    if n < nums_min:
        nums_min = n

print('最大数：',nums_max)
print('最小数：',nums_min)


# 6.找出列表nums里面相同元素分别有多少个 nums_count


# 找到num在列表里面出现的次数
num = 10
times = 0
for n in nums:
    if n == num:
        times += 1
print('数字%s出现的次数：%s'%(num, times))


# 无限循环直到列表里面出现num这个数
num = 10
times = 0
count = 0
# while True:
#     count += 1
#     nums = [random.randrange(1, 101) for _ in range(10)]
#     print(nums)
#     for n in nums:
#         if n == num:
#             times += 1
#     print(num, times, count)
#     if times != 0:
#         break

# 找出列表nums里面相同元素分别有多少个
nums_count = {}
for n in nums:
    if n in nums_count:
        nums_count[n] += 1
    else:
        nums_count[n] = 1
print('每个元素出现的次数：', nums_count)


# 找出姓张的同学有多少个，分别是谁
# 找出名字里面带‘明’的同学有多少个，分别是谁

students = []
first_name = '张'
tag = '文'
for name in students:
    if name.startswith(first_name):
        print('姓张的：', name)

    if tag in name:
        print('名字里面带“文”的：', name)




