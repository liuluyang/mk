# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/20 14:53

"""
周考
"""


"""
第一题：
编写一个python程序，程序读入python_zen.txt文件，
把其中句子顺序倒排后输出到另外一个文件python_zen_reverse.txt中。
"""


"""
第二题：
编写一个python程序，程序读入python_zen.txt文件，
提取该文件中所用到的单词组成的列表（即该文件用到了哪些不同的单词），
并把该单词列表输出到另外一个文件vocabulary.txt中,以json格式存入，
需要用到json模块
"""


"""
第三题：
编写一个python程序，程序读入The Adventures of Tom Sawyer .txt文件，
提取该文件中所用到的单词组成的列表（即该文件用到了哪些不同的单词），
并统计每个单词的词频， 把该词频表输出到另外一个文件frequency.txt中,
以json格式存入，需要用到json模块
"""


"""
第四题：
某学校规定，若课程成绩大于等于85分，成绩等级为优秀；若成绩大于等于60分且小于85分，成绩为及格；
若成绩小于60分，成绩等级为不及格。读入第7题中创建的final_score.csv文件，
根据其中的成绩为同学评定成绩等级，并把附加了成绩等级的同学成绩列表输出到名为level.csv文件中.
"""


"""
第五题：
给一个字符串res和一个数字num
res = 'abcdefijkl'
num = 4
result = ['ae', 'bf', 'ci', 'dj']
把序列 平均分成 4等分，并返回结果result

例子2：
    res = '12345678'
    num = 3
    result = ['14', '25', '36']
列子3：
    res = '123456'
    num = 8
    result = []   # 不够分
注：
    注意字符是如何分配的
"""

def func_05_old():

    lst = ['a', 'b', 'c', 'd']
    num = 10

    r = []

    for i in range(num):
        index = i%len(lst)
        r.append(lst[index])

    return r

# r = func_05_old()
# print(r)

def func_05_new():


    res = 'abcdefijkl'
    num = 4
    result = ['ae', 'bf', 'ci', 'dj']

    r = ['']*num

    for index, per in enumerate(res[:-(len(res)%num)]):
        index_new = index%num
        r[index_new] += per

    return r

# r = func_05_new()
# print(r)


"""
第六题：
给FTP程序添加一个注销的功能
并且做一个限制，在未登录状态下，不可以使用此功能

提示：
    方法名称：logout
    方法作用：消除登录状态、操作目录切换到公共文件夹
"""


"""
第七题：
给FTP程序添加一个帮助的功能

提示：
    方法名称：help
    方法作用：获取帮助信息，比如该程序有哪些功能以及怎么使用，需要哪些参数等
"""


"""
第八题：
猜数字游戏
规则：
    实例化GuessNum会得到一个实例对象
    同时该对象拥有一个属性num，是一定范围内的随机数
    
    我们能做的是调用check_num_01这个方法，把猜测的数字传进去，
    来获取两个数字对比的结果， 从而来确定num的值
    
写个函数来完成此游戏，把猜测正确的数字返回

g = GuessNum()
r = g.check_num_01(32423432)
print(r)   # 大了、小了或等于
"""
# 10000000
# 41231232 => 10 * 8
# [0, 1, 2, 3, ...., 1000000]
num = 10000000
count = 0
while num > 1:
    num /= 2
    count += 1
    print(num, count)


class GuessNum:
    """
    一个猜数字的游戏
    """

    def __init__(self):

        self.num = self.make_num()

    def make_num(self):
        """
        产生一个随机数
        :return:
        """
        import random

        return random.randint(1000000, 100000000)

    def check_num_01(self, guess_num):
        """
        检查猜测的数字
        :param guess_num:
        :return:
        """
        if guess_num > self.num:
            return '大了'
        elif guess_num < self.num:
            return '小了'

        return '等于'

    def check_num_02(self, guess_num):
        """
        检查猜测的数字
        :param guess_num:
        :return:
        """
        if guess_num > self.num:
            return '大了'
        elif guess_num <= self.num:
            return '小了'


"""
第九题：
    把第八题猜测数字时调用的check_num_01改成调用check_num_02，其他条件不变
    来完成此游戏
    
"""


if __name__ == '__main__':
    g = GuessNum()
    r = g.check_num_01(32423432)
    # print(r)









