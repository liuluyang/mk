

num = 0

# while True:
#
#     num += 1
#     print(num)
#     if num > 100:
#         break
#
#     pass

# 打印实心菱形
lst01 = list(range(40))
lst02 = list(range(39))[::-1]
print(lst01)
print(lst02)
import time
while True:
    for i in lst01 + lst02:
        if i % 2 == 1:
            print(('*'*i).center(80), i)
            time.sleep(0.02)


# for i in range(20):
#     if i % 2 == 1:
#         print(('*'*i).center(40))

# for i in range(20):
#     i = 20 - i
#     if i % 2 == 1:
#         print(('*'*i).center(40))