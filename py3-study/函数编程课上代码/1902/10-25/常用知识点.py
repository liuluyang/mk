

import random
import time

students = ["冯亚尼", "曹泽涵", "张文哲", "曹怡", "张子涵",
            "李佳伦", "张灿武", "丁明宇", "张鱼洋", "郭利炜",
            "谷宣言", "彭子权", "屈晓明", "张家泽", "张丫丫",
            "高江涛", "尹梦许"]
num = 'RRRR0'

print(random.choice(students))    # 随机的从一个序列 选出一个元素
time.sleep(0)                    # 让程序等待多长时间
print(random.randrange(1, 100))   # 随机从一个范围选一个数字

print(isinstance([], str))         # 判断一个数据的类型
print(type(1))                    # 查看一个数据的类型



