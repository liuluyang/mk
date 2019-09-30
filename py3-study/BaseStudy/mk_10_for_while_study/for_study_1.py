

"""
for循环学习
"""

num_list = range(10)
print(num_list, list(num_list))
"""
基本循环
依次把num_list元素值赋给变量num
"""
# for num in num_list:
#     print(num)

"""
循环和判断
"""
# for num in num_list:
#     if num % 2 == 0:
#         print('偶数', num)
#     elif num % 2 != 0:
#         print('奇数', num)

"""
跳过单次循环continue
结束整个循环break
注意判断语句的顺序
"""
# for num in num_list:
#     if num % 2 == 0:
#         continue
#     print('奇数', num)
#     if num > 5:
#         break
#     # print('奇数', num)

"""
循环进阶之嵌套循环
"""

for num in num_list:
    print('我是第一层', num)
    for n in num_list:
        print('          我是第二层', n)


"""
九九乘法表
for循环、循环嵌套、字符串格式化
"""
for i in range(1,10):
    for y in range(1, i+1):
        text = '{} * {} = {}'.format(i, y, i*y)
        print(text, end='\t')
    print('\n')
