import random

"""
random模块学习
可查看一下方法的内部实现
"""
a = [1, 2, 3, 1]
# print(random.random())         #返回随机浮点数
# print(random.randint(1, 2))
# print(random.randrange(1, 3))  #返回range区间数值
# print(random.choice(a))        #返回给定集合随机数值

# random.shuffle(a)              #打乱顺序
# print(a)
# print(random.sample(a, 3))     # 随机选择不同的三个元素
# random.choices(a, k=3)         # 随机选择三个元素 可相同
