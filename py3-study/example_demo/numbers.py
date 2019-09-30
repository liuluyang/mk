import string
from itertools import combinations, permutations

az = string.ascii_uppercase + '0123456789'
print(az)

# print(len(list(permutations(az, 5))))

# nums = list(az)
# n = 0
# print(nums)
# while n < 5:
#     n += 1
#     nums_new = []
#     for num in nums:
#         for a in az:
#             nums_new.append(num+a)
#     nums = nums_new
# print(nums)