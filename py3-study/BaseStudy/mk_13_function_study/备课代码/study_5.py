


"""

列表生成式
"""
# 练习一
# 把下面列表里每个字典元素的所有key放到一个新的列表里面
# d_list = [
#     {'name':'python', 'class':1},
#     {'name':'java', 'class':2},
#     {'name':'php', 'class':3},
# ]

# 练习二
# 每个元素加一
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 方法一
# b = []
# for i in a:
#     b.append(i+1)
#
# print(b)

# 方法二
# for index, n in enumerate(a):
#     a[index] += 1
#
# print(a)

# 方法三

a = map(lambda x:x+1, a)
# print(a)

# 方法四
# a = [n+1 for n in a]
# print(a)

#
# tuple_ = ((1, 2), (3, 4))
# dict_ = dict(tuple_)
# print(dict_)

"""
字典生成式
"""
# dict_ = {n:n+1 for n in a}
# print(dict_)
# print(dict_[1])

# 练习一
word = 'hello python'
w_dict = {}

# 方法一
# for w in word:
#     if w in w_dict:
#         w_dict[w] += 1
#     else:
#         w_dict[w] = 1
# print(w_dict)

# 方法二
# w_dict = {w:word.count(w) for w in word}
# print(w_dict)

# 方法三
# w_dict = {w:word.count(w) for w in set(word)}
# print(w_dict)


"""
集合生成式
"""

# w_set = {w for w in word}
# print(w_set)

"""
生成器(generator)
1.生成器的作用
2.在Python中，一边循环一边计算后面元素的机制，称为生成器：generator
(保存的是计算方法， 而不是数据)
3.函数生成器
4.判断一个对象是否是生成器对象以及如何调用生成器对象
5.特性：所有元素只能调用一次
"""
from typing import Generator, Iterable, Iterator

w_generator = (w for w in word)
# 转成元组
# w_generator = tuple(w for w in word)
# print(w_generator)
# for index, i in enumerate(w_generator):
#     if index > 5:
#         break
#     print(index, i)
#
# print(list(w_generator))

def t(n):
    print('start')
    while n < 100:
        n += 1
        yield n
        print('next')
    print('end')
    # yield n+1
    pass

# t = t(1)
# print(t)
# print(isinstance(t, Generator))
# print(t.__next__())
# print(t.__next__())
#
# for i in range(100):
#     try:
#         print(next(t))
#     except StopIteration:
#         print('end')
#         break

# for i in t:
#     print(i)
#     print('*'*20)

"""
生产消费简单模型
"""

def test():
    n = 0
    print('开始')
    while n < 5:
        n += 1
        #print(n)
        data = yield n
        if data == 'q':
            print('结束')
            break
        # print(n)
        print('外部数据', data)

# t = test()
#
# next(t)
# print(t.send('hello'))
# t.send('hello')
# t.send('hello')
# t.send('hello')
# t.send('hello')
# next(t)

"""
可迭代：
可以直接作用于for循环的对象统称为可迭代对象：Iterable，可迭代的意思就是可遍历、可循环
迭代器：
实现了__iter__()、__next__()方法的对象
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
生成器对象都是迭代器对象
迭代器不一定是生成器
iter()
"""
# print(isinstance(t, Generator))
# print(isinstance(t, Iterator))
# print(isinstance(t, Iterable))

# 转成迭代器对象
# text = iter('ad')
# print(isinstance(text, Iterator))
# print(next(text))
# print(next(text))







