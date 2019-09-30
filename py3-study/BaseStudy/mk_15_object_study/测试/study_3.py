
from typing import Iterable, Iterator
"""
内置方法：
hasattr()
getattr()
setattr()
delattr()

特殊属性方法:
__dir__ __dict__
__repr__  __str__
__getattr__ __setattr__ __delattr__
__call__
__len__ __contains__ __getitem__ __setitem__ __delitem__
数学运算符、比较运算符
类型转换、内建函数
上下文管理器的实现
"""

class Square(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # def __getattribute__(self, item):
    #     print('__getattribute__', item)
    #     return object.__getattribute__(self, item)
    #     # if item == 'size':
    #     #     return self.width * self.height
    #     # print('sss')
    #     # return self.__dict__.get(item)
    #     pass

    def __repr__(self):
        return '%s %s %s'%(Square.__name__, self.width, self.height)

    def __str__(self):
        return '%s %s'%(self.width, self.height)

    def __getattr__(self, item):
        """
        当所找的属性方法找不到时，会调用此方法
        :param item:
        :return:
        """
        print('__getattr__', item)
        if item == 'size':
            return self.width * self.height
        else:
            # raise AttributeError('没有此属性')
            return self.__dict__.get(item)

    def __setattr__(self, key, value):
        """
        设置属性的时候会调用此方法
        :param key:
        :param value:
        :return:
        """
        print('设置属性', key)
        self.__dict__[key] = value

    def __delattr__(self, item):
        print('删除属性 del self.item', item)
        self.__dict__.pop(item, None)

    def run(self):
        print('running')

    def __call__(self, *args, **kwargs):
        print('我可以向函数一样调用')

    def __len__(self):
        """
        决定序列中元素的个数
        :return:
        """
        return 1

    def __contains__(self, item):
        """
        判断是否包含指定元素
        :param item:
        :return:
        """
        pass

    def __getitem__(self, item):
        """
        获取指定元素
        :param item:
        :return:
        """
        pass

    def __setitem__(self, key, value):
        """
        更新或添加指定元素
        :param key:
        :param value:
        :return:
        """
        pass

    def __delitem__(self, key):
        """
        删除指定元素
        :param item:
        :return:
        """
        pass

    def __eq__(self, other):
        """
        相等判断 ==
        :param other:
        :return:
        """
        return self.size == other.size

    def __int__(self):
        """
        对int()函数提供支持
        :return:
        """
        return 1

    def __hash__(self):
        """
        对hash()函数提供支持
        :return:
        """
        return 11111111111

    def __enter__(self):
        print('enter')

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """类型 实例 回调"""
        print('exit')
        print(exc_type, exc_val, exc_tb, type(exc_val))
        print(exc_type is ValueError)
        return True   # 不传递异常

    def __iter__(self):
        """
        可迭代对象
        :return:
        """
        return self

    def __next__(self):
        """
        迭代器对象
        :return:
        """
        pass


# with Square(1, 3) as d:
#
#     raise ValueError('value')
#     pass
s = Square(20, 30)
# print(isinstance(s, Iterator))
# print([s], s)
# print(hash(Square))
# s2 = Square(20, 30)
# print(s == s2)
# print(len(s))
# s()
#s.size = 1
# print(s)

# print(hasattr(s, 'name'))
# print(getattr(s, 'name', None))
# setattr(s, 'name', 'lly')
# print(s.widt)
# del s.width
# print(s.__dir__())
# print(s.__dict__)

# r = getattr(s, 'run')
# print(callable(r))
# print(r)

# with Square(1, 3) as d:
#     print(d.run())
#     pass


"""
上下文管理器
自定义上下文管理器
@contextmanager
"""


from contextlib import contextmanager

"""利用上下文实现间隔打印"""

class Indenter(object):
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print_(self, text):
        print('    ' * self.level + text)

# with Indenter() as indent:
#     indent.print_('hi!')
#     with indent:
#         indent.print_('locke')
#         with indent:
#             indent.print_('cucumnber')
#     indent.print_('over')

"""
可参考 流畅的python
"""

# @contextmanager
def contentdemo():
    #try:
        print('start')
        n = yield 100

        print(n)
        print('ok')
        n = yield 101

        print(n)
        yield 102

    #except:
        #print('error')

@contextmanager
def contentdemo_02():
    #try:
        print('start')
        yield 100
        print('end')
    #except:
        #print('error')

# c = contentdemo_02()
#
# with contentdemo_02() as cc:
#     print(cc)
#     # print(111)
#     # raise ValueError
#     pass

# try:
#     y = next(c)
#     print(y)
# except:
#     print('first next')

# try:
#     y = next(c)
#     print(y)
# except (ValueError,StopIteration):
#     print('second next')
#
# try:
#     y = next(c)
#     print(y)
# except:
#     print('third next')

# with contentdemo() as n:
#     print(n)
#     print('do something')
#     raise TypeError

# c = contentdemo()
# try:
#     y = next(c)
#     print(y)
# except StopIteration:
#     print('第一次next')
# print('#'*20)
# try:
#     next(c)
# except StopIteration:
#     print('第二次next')

# y = next(c)
# print(y)
#
# y = next(c)
# print(y)
############################################
# y = next(c)
# print(y)

# y = c.send(1)
# print(y)

# c.send(11)
