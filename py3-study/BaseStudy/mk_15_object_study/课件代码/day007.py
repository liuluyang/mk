

################################################## __next__和__iter__实现迭代器协议 ##################
from typing import Iterable, Iterator, Generator

class Foo:

    def __init__(self, num):
        if not isinstance(num, int):
            raise TypeError
        self.num = num

    def __iter__(self):
        """
        1.只要实现了该方法的对象，那么就认为该对象是可迭代对象
        2.但是要让对象真正可迭代，必须返回实现了__next__和__iter__方法的对象
        3.iter()方法会调用该方法，for循环也会调用该方法
        :return:
        """
        print('__iter__ is calling')
        # return (i for i in range(self.num))

        # return [1, 2]

        return iter(range(self.num))

# f = Foo(5)
# print(f)
# print(list(f))
# print(isinstance(f, Iterable), isinstance(f, Iterator))
# print(iter(f))
# for i in f:
#     print(i)

####################################

class Foo:

    def __init__(self, num):
        self.num = num

    def __iter__(self):

        return self

    def __next__(self):

        self.num += 1
        if self.num > 10:
            raise StopIteration  # 当被for循环时会正常结束
            # raise TypeError                # 出现异常
        return self.num

# f = Foo(0)
# print(isinstance(f, Iterable), isinstance(f, Iterator))
# for i in f:
#     print(i)


################################################ 用__enter__和__exit__实现上下文管理器

######################################### 01认识

class Open:

    def __init__(self):
        self.f = open('t.txt', 'w', encoding='utf8')

    def __enter__(self):
        print('进入__enter__')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 捕获with语句块里面的异常
        print('结束__exit__')
        self.f.close()     # 关闭文件

        print('exc_type:', exc_type)
        print('exc_val:', exc_val, str(exc_val))
        print('exc_tb:', exc_tb)


        # return False     # 返回False,None 传递异常

        return True        # 当返回True时，不传递异常


# with Open() as f:
#     print('哈哈哈')
#
#     print(f)
#     f.write('你好哇')
#     # raise IOError('error')
#
#     print('嘿嘿嘿')
#
# print('文件是否关闭：', f.closed)


########################################  02进阶
from contextlib import contextmanager
from functools import wraps

class Manager:

    def __init__(self, func, args, kwargs):

        self.gen = func(*args, **kwargs)

    def __enter__(self):
        print('__enter__')
        try:
            return next(self.gen)
        except StopIteration:
            # 捕获StopIteration之后添加提示信息并抛出，其它异常正常传递
            # 如果self.gen函数里有捕获异常语句块，可能会捕获到StopIteration
            raise StopIteration("generator didn't yield")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

        try:
            next(self.gen)     # 执行self.gen函数yield之后的代码
        except StopIteration:
            # 忽略StopIteration异常
            pass
        except Exception as e:
            # 捕获StopIteration之外的其它异常，并抛出
            raise Exception(str(e))

        if exc_type:
            # 把with语句块里面的异常抛出
            return False

        return True

def contentM(func):

    @wraps(func)
    def inner(*args, **kwargs):

        return Manager(func, args, kwargs)

    return inner

@contentM
def cc_01(name='ufo'):
    # raise ValueError('cc error')
    print('start cc()', name)
    yield 'hello'
    print('end cc()')
    # raise ValueError('v')

@contentM
def cc_02():
    try:
        # raise ValueError('cc error')
        print('start cc()')
        yield 'hello'
        print('end cc()')
        # raise ValueError('v')
    except Exception as e:
        print('cc Exception:', e)

# with cc_01() as c:
#     print('this is c:', c)
#     # raise ValueError('with 语句块发生异常')


