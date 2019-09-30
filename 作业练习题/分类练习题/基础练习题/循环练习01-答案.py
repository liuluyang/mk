


"""
1. 猜数游戏：
随机生一个1-10之间的数
最多可以猜三次，如果猜错，会提示猜大了还是猜小了
猜对 游戏直接结束
如果三次都没猜对，最后打印出那个随机数
"""
# import random
#
# num = random.randrange(1, 11)
# print('随机数已生成， 猜数游戏开始。。。')
# r = False
#
# for i in range(1, 4):
#     print('第%s次机会'%i)
#     n = int(input('请输入猜测的数字：'))
#     if n > num:
#         print('数猜大了')
#     elif n < num:
#         print('数猜小了')
#     else:
#         print('猜对了')
#         r = True
#         break
#     print('#'*20)
#
# if not r:
#     print('你要猜的数是%s'%num)
# print('游戏结束！')


"""
2. 生成一个符合要求的车牌号：
要求：
车牌号五位数，必须包含数字和大写字母 例如：RT038
"""
# import random
# import string
#
# params = string.ascii_uppercase + string.digits
# while True:
#     card = ''
#     for i in range(5):
#         card += random.choice(params)
#     if not card.isdigit() and not card.isalpha():
#         print(card, '符合')
#         break
#     else:
#         print(card, '不符合')


"""
3. 给出限号的号码，判断一个车牌是否被限号
限号规则：
从最后一位倒着找，如果是字母跳过，如果是数字就进行是否限号的判断
例如：
限号号码 limit_nums = [3, 8] 
车牌 RT008 被限号
车牌 RT800 不被限号
"""
# limit_nums = [3, 8]
# card = 'RT8HJ'
# for c in card[::-1]:
#     if c.isdigit():
#         if int(c) in limit_nums:
#             print(card, '被限号')
#         break
# else:
#     print(card, '不被限号')
