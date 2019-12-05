

"""
周考
"""


"""10
第一题：
1、简述你对类和对象的理解
"""


"""10
第二题：
2、面向对象的三大特征？并简述自己的理解
"""


"""10
第三题：
3、__init__函数的作用？self是什么？
"""


"""10
第四题：
4、定义一个Person类：
    设置name/age都为私有属性
    对外提供 查看 修改 name的接口
    注：
        对name的类型进行限制，不管是初始化时还是修改时，
        name都必须是字符串，否则报错
"""
class Person:

    def __init__(self, name, age):

        # 方法一
        # if not isinstance(name, str):
        #     raise TypeError('name type must be str')
        # self.__name = name

        # 方法二
        self.name = name
        self.__age = age
        pass

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, name_new):

        if not isinstance(name_new, str):
            raise TypeError('name type must be str')

        self.__name = name_new


# p = Person(1, 20)
# p.name = 'xx'
# print(p.name)


"""10
第五题：
5、定义一个类：
    里面包括类方法和静态方法
"""
class F:

    @classmethod
    def count(cls):

        return cls

    @staticmethod
    def func():

        return 1


"""15
第六题：
6、实现map()函数或者解释map函数的作用
print(list(map(lambda x, y:x*y, [1, 2], (i for i in range(10)))))
"""
# print(list(map(lambda x, y:x*y, [1, 2], (i for i in range(10)))))
# print(list(map(lambda x, y:x*2 + y*2, [1, 2], [1, 2, 3])))
def map_new(func, item):

    for i in item:
        yield func(i)

# print(list(map_new(lambda x:x*2, [1, 2], [1, 2])))


def map_new_02(func, *item):

    for i in zip(*item):
        yield func(*i)

# print(list(map_new_02(lambda x, y:x + y, [1, 2], [1, 2, 3])))

"""10
第七题：
7、找出列表里面只出现了一次的那个数，把这个数和它的索引值返回
nums = [1, 2, 2, 3, 4, 4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 1, 2, 2, 3,
        4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 5, 2, 2, 2, 3, 4, 4, 3, 2,
        ]
注：
    1、不能用count()方法
    2、如果只用一次for循环可以求出结果的，总分再加5分
"""
def func_07():

    nums = [1, 2, 2, 3, 4, 4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 1, 2, 2, 3,
            4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 5, 2, 2, 2, 3, 4, 4, 3, 2,
            ]
    # nums = [1, 2, 2, 1, 4, 1]

    r = {}
    d = set()
    for index, num in enumerate(nums):

        if num in d:  # 把出现多次的数字的信息从字典里面删除
            # if num in r:
            try:
                r.pop(num)
            except:
                pass
        else:
            d.add(num)
            r[num] = index

    return r
# print(func_07())


"""15
第八题：
8、继承之前讲解的ATM程序，给该程序添加一个修改密码的功能，并修改主函数
"""


"""10
第九题：
9、写一个函数或者类，实现open()函数的所有功能，但可以借用open()函数
    最终效果：
    1、当打开一个文本文件(非二进制模式打开)，且不指定编码时，默认编码是utf8
    1、其它操作文件的功能一切正常，例如：当以二进制模式操作文件时，一切正常。
"""
# 偏函数
def openNew(file, mode='r', encoding='utf8'):

    if 'b' in mode:
        encoding = None

    f = open(file, mode=mode, encoding=encoding)

    return f


class OpenNew():

    def __init__(self, file, mode='r', encoding='utf8'):

        if 'b' in mode:
            encoding = None

        self.f = open(file, mode=mode, encoding=encoding)

    def __getattr__(self, item):

        return getattr(self.f, item)

# f = open('test.py', 'r')  # 默认编码为utf8
# print(f)
#
# f = openNew('test.py', 'r')  # 默认编码为utf8
# print(f)

# op = OpenNew('test.py', 'r')
# print(op.read())


"""20
第十题：
10、找出英文句子里面出现频率最高的单词,如果有多个全部找出来，
    但请把出现在limit列表里面的单词剔除
res = "what are you talking about, show me your code."
limit = ['are']
注：忽略大小写
"""

def func_10():

    import re
    res = "what are you talking about, show me your code."
    limit = ['are']
    words_list = re.findall('[a-zA-Z]+', res)

    dic = {}
    word = []
    max_num = 0
    for w in words_list:
        w = w.lower()
        if w in limit:
            continue

        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

        num = dic[w]
        if num > max_num:
            max_num = num
            word = [w]
        elif num == max_num:
            word.append(w)

    return word

# print(func_10())



