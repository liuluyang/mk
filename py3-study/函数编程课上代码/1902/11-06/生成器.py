

from typing import Iterable, Iterator, Generator


# lst = []
# num = 0
# while True:
#     lst.append(num)
#     num += 1
#     break


############################################## 有限数列


def make_num():

    lst = []
    num = 0
    while True:
        lst.append(num)
        num += 1

        if num > 10000:
            break

    return lst

# nums = make_num()
# print(nums)
# for i in nums:
#     print(i)

################################################ 无限数列

# generator
# 生成器函数 yield
# 一个函数里面包含yield,我们就认为他是一个生成器函数
def make_num_02():

    num = 0
    yield num

    while True:
        num += 1
        yield num

    # yield 0
    # yield 1
    # yield 2
    # yield 3


# 当调用一个生成器函数时，会得到一个生成器对象
nums = make_num_02()     # 生成器对象
# print(nums)
# print(make_num_02)

# 获取值的第一种方式
# print(next(nums))       # 调用生成器对象里面的值
# print(next(nums))
# print(next(nums))
# print(next(nums))
"""
当取不到值得时候，会出错（StopIteration）
"""
# print(next(nums))

# 获取值的第二种方式
# for i in nums:
#     print(i)

# for i in range(100):
#     print(next(nums))

"""
**顺序取值，直到取完为止, 取过的不能再去获取，不能用索引方式[]取值,
也不能用len()来计算长度
"""
# for i in nums:
#     print(i)

"""
**不要尝试用list()转换一个会产生无限数据的生成器对象，
这种做法可能会瞬间让内存占满，使电脑卡死
"""

# 判断是否是一个生成器对象
# print(isinstance(nums, Generator))
# print(isinstance(iter('abc'), Generator))


############################################## 其他迭代器对象

# e = enumerate('abc')
# print(e, list(e))
# print(isinstance(e, Iterator))

# m = map(lambda x:x*2, range(10))
# print(m, list(m))
# print(isinstance(m, Iterator))

# z = zip([1, 2, 3], 'abc')
# print(z, list(z))
# print(isinstance(z, Iterator))

# f = filter(lambda x:x>5, range(10))
# print(f, list(f))
# print(isinstance(f, Iterator))

# r = reversed('abc')
# print(r, list(r))
# print(isinstance(r, Iterator))

# 会出错 reversed只能翻转有限序列
# print(reversed(nums))


############################################# 简单模仿range函数的功能

# print(list(range(1, 1000, 2)))

def make_num_02(num):

    yield num

    while True:
        num += 2
        if num > 1000:
            break
        yield num

# for i in make_num_02(1):
#     print(i)

"""
注：
range函数不是迭代器对象
但是功能强大
"""
# print(isinstance(range(10), Iterable))
# print(range(1000)[100])
# print(range(1, 100000000000000000000, 2)[100000000000])


############################################# 生成器表达式

# t = (i for i in range(1000))
# print(t)


############################################# 斐波那契数列


############################################# 模仿map







