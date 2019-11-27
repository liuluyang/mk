

"""
1.计算列表中指定元素的个数，并列出它们的索引值
list_01 = ['h', 'e', 'l', 'l', '0', 'h', 'k']
tag =  'h'

nums = 0
index_list = []
"""
list_01 = ['h', 'e', 'l', 'l', '0', 'h', 'k']
tag =  'h'
nums = 0
index_list = []

# 第一种方法
# index = 0
# for i in list_01:
#     if i == tag:
#         nums += 1
#         index_list.append(index)
#     index += 1
# print(nums, index_list)

# 第二种方法
# enumerate(list_01)同时循环出索引和元素
# for index, i in enumerate(list_01):
#     if i == tag:
#         nums += 1
#         index_list.append(index)
#
# print(nums, index_list)


"""
2.列表反转
list_01 = ['德', '玛', '西', '亚']
==> ['亚', '西', '玛', '德']
注：不能生成新的列表，不能用[::-1]取反操作
"""
list_02 = ['德', '玛', '西', '亚']
# r = list_02.reverse()
# print(list_02)

for i in range(len(list_02)//2):
    # 分步
    # res01 = list_02[i] # 取出前边的元素
    # index = -(i + 1)   # 计算后边的索引
    # res02 = list_02[index] # 取出后边的元素
    #
    # list_02[index] = res01 # 替换后边的值
    # list_02[i] = res02     # 替换前边的值

    # 整合
    list_02[i], list_02[-(i + 1)] = list_02[-(i + 1)], list_02[i]

print(list_02)


"""
3.模拟判断字符串是否以指定的字符串开始或结束：
res = 'hello world'
print(res.startswith('hello '))  # True
print(res.endswith('ld'))      # True
"""
res = 'hello world'
tag01 = 'hello world '
tag02 = 'ld'
# if len(tag01) > len(res):
#     print(False)
# print(res.startswith(tag))

# 第一种方法
# print(res[0:len(tag01)] == tag01)
# print(res[-len(tag02):] == tag02)

# 第二种方法
# if len(tag01) <= len(res):
#     for index in range(len(tag01)):
#         if res[index] != tag01[index]:
#             print(False)
#             break
#     else: # 当循环正常结束时
#         print(True)
# else:
#     print(False)


"""
4. 猜数游戏：
随机生一个1-10之间的数
最多可以猜三次，如果猜错，会提示猜大了还是猜小了
猜对 游戏直接结束
如果三次都没猜对，最后打印出那个随机数
"""
import random
random_num = random.randrange(1, 11)

# 第一种方法
isTrue = False
for i in range(3):
    num = int(input('请猜数：'))
    if num > random_num:
        print('猜大了')
    elif num < random_num:
        print('猜小了')
    else:
        print('恭喜你猜对了！')
        isTrue = True
        break
if not isTrue:
    print('正确结果是：', random_num)

# 第二种方法
for i in range(3):
    num = int(input('请猜数：'))
    if num > random_num:
        print('猜大了')
    elif num < random_num:
        print('猜小了')
    else:
        print('恭喜你猜对了！')
        break
else: # 如果循环正常结束
    print('正确结果是：', random_num)


"""
5. 生成一个符合要求的车牌号：
要求：
车牌号五位数，必须包含数字和大写字母 例如：RT038
"""


"""
6. 给出限号的号码，判断一个车牌是否被限号
限号规则：
从最后一位倒着找，如果是字母跳过，如果是数字就进行是否限号的判断
例如：
限号号码 limit_nums = [3, 8] 
车牌 RT008 被限号
车牌 RT800 不被限号
"""


