

"""
while循环学习
"""

"""
初次认识
注：
    设置好循环停止条件
    如果条件设置不好 程序会永远执行下去
"""
# num = 0
# while True:
#     num += 1
#     print(num)
#     if num > 1000:
#         break

# num = 0
# while num < 1000:
#     num += 1
#     print(num)

"""
for和while的使用场景
"""

"""

"""
import time
t = 0.01
str_ = '*'
num_list = range(1, 61)
num_list_reverse = sorted(list(num_list), reverse=True)
while True:
    for i in num_list:
        if i % 2 != 0:
            time.sleep(t)
            text = str_*i
            print(text.center(80))
    for i in num_list_reverse:
        if i % 2 != 0:
            time.sleep(t)
            text = str_ * i
            print(text.center(80))



