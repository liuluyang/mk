

from typing import Iterable, Iterator


"""
可迭代对象（可循环对象）(iterable object)
"""

"""
TypeError: 'int' object is not iterable 可迭代
"""

item = 'abc'
# for i in item:
#     print(i)


# 判断一个对象是否可迭代
# print(isinstance(item, Iterable))

############################################# __iter__/next()  iter() __next__

# print(item.split('a'))
# item.__iter__()
# [].__iter__()


"""
TypeError: 'str' object is not an iterator 迭代器对象
"""
# item_new = item.__iter__()
# item_new = iter(item)  # iter(iter) => item.__iter__()
#
# while True:
#     try:
#         print(next(item_new)) # next(item_new) => item_new.__next__()
#         # print(item_new.__next__())
#     except:
#         break
#         pass

# print(item_new)
#
# print(next(item_new))
# print(next(item_new))
# print(next(item_new))
#
# print(next(item_new))

################################################## dir()
"""
dir()查看一个对象拥有的所有方法，返回值是一个列表
"""

# method_lst = dir(1)
# print('__iter__' in method_lst)

# print(len(method_lst))
#
# count = 0
# for i in method_lst:
#     if not i.startswith('__'):
#         print(i)
#         count += 1
#
# print(count)


########################################### 总结

"""
可迭代对象：
    可以作用于for循环的都是可迭代对象（或者说是可以循环的都是可迭代对象）
    准确描述：拥有__iter__特殊方法的对象，是可迭代对象
判断的方法：
    item = 'abc'
    1. print(isinstance(item, Iterable)) # 常用的
    2. print('__iter__' in dir(item))
"""

"""
迭代器对象：
    可以被next()函数调用并不断返回下一个值的对象称之为迭代器对象
    准确描述：拥有__iter__和__next__特殊方法的对象，是迭代器对象
判断的方法：
    item = iter('abc')
    1. print(isinstance(f, Iterator)) # 常用的
    2. print('__iter__' in dir(item) and '__next__' in dir(item))
"""

"""
可迭代对象和迭代器对象的关系：
    1. 一个可迭代对象可通过iter()函数转换成迭代器对象
    
    2. 迭代器对象同时又是可迭代对象

"""
# print(isinstance([], Iterator))


class F:


    def __iter__(self):
        pass

    def __next__(self):
        pass


# f = F()
#
# for i in f:
#     print(i)
# print(isinstance(f, Iterator))
















