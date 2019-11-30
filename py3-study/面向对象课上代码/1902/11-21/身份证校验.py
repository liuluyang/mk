

"""

身份证号码由 17 位数字和 1 位校验码组成。校验码生成规则如下：将前面的
身份证号码 17 位数分别乘以不同的系数，
第 1—17 位的系数分别为：7，9，10， 5，8，4，2，1，6，3，7，9，10，5，8，4，2，将这 17 位数字和系数相乘的结
果相加，用相加的结果对 11 取模。余数对应结果从 0 到 10 共 11 个数字，他们
分别对应的最后一位身份证号码为 1，0，X，9，8，7，6，5，4，3，2。例如如
果余数是 2，最后一位数字就是罗马数字 X，如果余数是 10 最后一位就是 2.
设计程序实现输入 18 位身份证号码，辨别真伪，若为真则进一步判断性别，
"""


"""
1. 身份证号码 17 位数分别乘以不同的系数 系数分别为：7，9，10， 5，8，4，2，1，6，3，7，9，10，5，8，4，2
2. 用相加的结果对 11 取模
3. 他们分别对应的最后一位身份证号码为 1，0，X，9，8，7，6，5，4，3，2
"""

coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 系数
last_nums = '10X98765432'

card = '123111111111111111'

# 第一步
count = 0
for lst in zip(card, coefficient):
    count += int(lst[0]) * lst[1]

# 第二步
index = count % 11

# 第三步
valid_num = last_nums[index]
print(valid_num)

# 第四步
print(valid_num == card[-1])


