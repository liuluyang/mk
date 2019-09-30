#coding:utf8


# s_01 = 'hello'
# s_01_new = ','.join(s_01)
# print(s_01, s_01_new)
#
# print(s_01_new.split('h'))

"""
模拟单个字符切分
"""
# s_new_list = []
# s_new = ''
# tag = 'h'
# s_len = len(s_01_new)
# index = 0
# for s in s_01_new:
#     if s == tag:
#         s_new_list.append(s_new)
#         s_new = ''
#     else:
#         s_new += s
#
#     if index == s_len-1:
#         s_new_list.append(s_new)
#
#     index += 1
#
# print(s_new_list)


"""
模拟消除字符串两边空格
"""

# s_02 = '  he llo  '
# s_02_strip = s_02.strip()
# print(s_02, len(s_02))
# print(s_02_strip, len(s_02_strip))
#
#
# for i in range(len(s_02)):
#     if s_02[i] != ' ':
#         s_02 = s_02[i:]
#         break
# for i in range(len(s_02)):
#     index = int((i+1)/-1)
#     if s_02[index] != ' ':
#         s_02 = s_02[:index+1]
#         break
# print(s_02, len(s_02))


"""
模拟字符串拼接
"""
# tag = ','
# s_03 = 'hello'
# s_03_join = tag.join(s_03)
# print(s_03_join)
#
# s_03_new = ''
# for s in s_03:
#     s_03_new += s + tag
#
# s_03_new = s_03_new[:-len(tag)]
# print(s_03_new)


"""
模拟判断字符串是否以指定的字符串开始或结束
"""
# s_04 = '__end_gg'
# tag_01 = '__'
# tag_02 = '_gg'
# print(s_04.startswith(tag_01))
# print(s_04[:len(tag_01)] == tag_01)
# print(s_04.endswith(tag_02))
# print(s_04[-len(tag_02):] == tag_02)


"""
九九乘法表变形
考察对for循环的嵌套理解
"""
# for i in range(1,5):
#     for y in range(1, 6+i):
#         print('%s*%s=%s '%(i, y, i*y), end='')
#     print()


"""
猜数游戏：
随机生一个1-10之间的数
最多可以猜三次，如果猜错，会提示猜大了还是猜小了
猜对游戏直接结束
如果三次都没猜对，最后打印出那个随机数

"""

# import random
#
# num = random.randrange(1, 11)
# print('随机数已生成， 猜数游戏开始。。。')
# r = False
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
打印菱形
"""

import time
n = 30
nums = list(range(n)) + list(range(n-2, 0, -1))

"""
版本一
"""
# for i in nums:
#     if i % 2 == 1:
#         s = ('*' * i)
#         print(s.center(n * 2))

"""
版本二
"""
# for i in nums:
#     if i % 2 == 1:
#         s = ('*'*i)
#         if i != 1:
#             s = '*' + ' '*(i-2) + '*'
#         print(s.center(n*2))

"""
版本三
"""
# while True:
#     for i in nums:
#         if i % 2 == 1:
#             s = ('*'*i)
#             if i != 1:
#                 s = '*' + ' '*(i-2) + '*'
#             print(s.center(n*2))
#             time.sleep(0.02)


# while True:
#     for i in list(range(20))+list(range(20, 0, -1)):
#         print((' '*i).ljust(200, '*'))
#         time.sleep(0.04)


