

import random


# 随机产生一个浮点数 0<=  <1
# print(random.random())

# 产生一个指定范围的整数 [ )
# print(random.randrange(1, 15, 2))

# 产生一个指定范围的整数 [a, b]
# print(random.randint(1, 5))

# 随机的从一个序列选一个元素
# print(random.choice('abc'))

# 随机的从一个序列选指定个数的元素，也可以指定权重值
# print(random.choices('abc', weights=[1, 1, 6], k=2))

# 随机的从一个序列选指定个数的元素, 每个元素只能被选一次
# print(random.sample('aabc', 3))

# 打乱一个列表，在源列表上面
nums = [1, 2, 3]
# random.shuffle(nums)
# print(nums)