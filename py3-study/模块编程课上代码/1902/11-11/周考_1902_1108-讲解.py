

"""
周考
"""
"""
注：
每个题单独定义一个函数
如果标明需要返回值的，必须要有返回值
"""


"""
第一题：
lst = [1, 2, 'abc', [], (), {}, 'cba', 3]
计算列表lst里面有多少种数据类型（列表最多含六种数据类型）
"""
def func_01():

    isinstance(1, int)
    type(1)


"""
第二题：
s = '   李银河  你好哇  '
s_new = '李银河  你好哇'
把字符串s处理成一个新的字符串s_new并返回
注：不能用strip()方法
"""


"""
第三题：
lst = [['老王', 1], ['去', '上班!'], 2, [3, 4], 'abc']
求列表里面所有数字的和
"""


"""
第四题：
用循环打印出下面的空心菱形：大小不必完全一样
                   *
                  * *
                 *   *
                *     *
               *       *
              *         *
             *           *
            *             *
           *               *
          *                 *
           *               *
            *             *
             *           *
              *         *
               *       *
                *     *
                 *   *
                  * *
                   *
"""
def func_04():
    for i in range(1, 20, 2):
        s = '*'+ ' '*(i - 2)+ '*'
        if i == 1:
            s = '*'

        print(s.center(40))


"""
第五题：
工资信息
data = {'佩奇':15000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000}
把data数据处理成lst并返回
lst = [['佩奇', 15000], ['黑姑娘', 10000], ['老村长', 9000], ['马JJ', 8000], ['海峰', 7000], ['老男孩', 6000]]
"""
def func_05():

    data = {'佩奇': 15000, '老男孩': 6000, '海峰': 7000, '马JJ': 8000, '老村长': 9000,
            '黑姑娘': 10000}

    print([list(i) for i in sorted(list(data.items()), key=lambda x:x[-1], reverse=True)])
    pass

# func_05()


"""
第六题：
['佩奇', '老男孩', '海峰', '马JJ', '老村长', '黑姑娘', '白姑娘']
找出名字最长的，如果有多个全部找出来
"""
def func_06():

    names = ['佩奇', '老男孩', '海峰', '马JJ', '老村长', '黑姑娘', '白姑娘']

    num = max([len(i) for i in names])
    print([name for name in names if len(name) == num])

# func_06()

def func_06_02():

    names = ['佩奇', '老男孩', '海峰', '马JJ', '老村长', '黑姑娘', '白姑娘']

    names_filter = []
    max_num = 0
    data = {}
    for name in names:

        name_length = len(name)
        if name_length in data:
            data[name_length] += 1
        else:
            data[name_length] = 1

        print(data[name_length])

        if name_length > max_num:
            max_num = name_length
            names_filter = [name]
        elif name_length == max_num:
            names_filter.append(name)

    print(names_filter)

# func_06_02()


#
"""
第七题：
读取user_info.txt的信息
当输入某个人的姓名时，打印出这个人的电话号码
或者输入某个人的手机号码，打印出这个人的姓名
注：当查找的信息不存时程序不能出错，可以返回提示信息
"""


#
"""
第八题：
把我的作品.txt 按行数编号，打乱之后写入一个新的文件
"""


#
"""
第九题：
这里有一个 食堂账本.txt
统计一下各个菜品的售卖情况
注：有的菜品有大小份，但是算作一种菜品，也就是忽略大小份
"""


"""
第十题：
写个递归函数 求1-10的阶乘
1*2*3...10
"""
def func_10(num):

    if num >= 10:
        return 10

    return num * func_10(num + 1)

# print(func_10(1))
# print(sum(range(1, 11)))

"""
第十一题：
写个装饰器函数
"""
def func_11(func):

    def inner(*args, **kwargs):

        f = func(*args, **kwargs)
        return f

    return inner


"""
第十二题：
写一个生成器模仿enumerate函数的功能
"""
from typing import Iterator
for index, s in enumerate('abc', 2):
    print(index, s)
# print(isinstance(enumerate('abc'), Iterator))
# e = enumerate('abc')
# print(next(e))

def func_12(item, n = 0):

    for i in item:
        yield (n, i)
        n += 1

# f = func_12('abc', 2)
# print(f)
# print(next(f))
# for i in f:
#     print(i)






























