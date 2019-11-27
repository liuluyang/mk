
import random
import string


"""
5. 生成一个符合要求的车牌号：
要求：
车牌号五位数，必须包含数字和大写字母 例如：RT038
"""
res = string.ascii_uppercase + string.digits
print(res)
count = 0

while True:
    count += 1
    num = ''
    for i in range(5):
        num += random.choice(res)

    print(count, num)
    if not num.isdigit() and not num.isalpha():
        break


"""
6. 给出限号的号码，判断一个车牌是否被限号
限号规则：
从最后一位倒着找，如果是字母跳过，如果是数字就进行是否限号的判断
例如：
限号号码 limit_nums = [3, 8] 
车牌 RT008 被限号
车牌 RT800 不被限号
"""
print('*'*20)
print(num)
limit_nums = ['3', '8']

for n in num[::-1]:

    if n.isdigit(): # 判断是否是数字
        if n in limit_nums:
            print(num, '限号')
        else:
            print('不限号', n)
        break
