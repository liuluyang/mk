
# 解决模块找不到的问题
import sys
sys.path.append('E://project')

# 内置或三方模块的导入
import random                          # 导入模块
from random import *                   # 导入全部
from random import randint, randrange  # 指定导入某几个
from random import choice as ch        # 起别名
import random as rd                    # 起别名
import set_color
import sys

# 导入当前路径的模块
import hello

# 当导入模块的时候，模块里面的代码会被执行
from education.other.random_show import choice_04


# def choice():
#     pass

# print(random.choice([1, 2, 3, 4]))
# print(random.randint(1, 5))

# print(randint(1, 5))
# print(randrange(1, 5))

# print(set_color.set_color('hello'))

# print(sys.path)

# choice_04()

# hello.hello()


