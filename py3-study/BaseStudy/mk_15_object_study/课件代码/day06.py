

"""
特殊方法
"""

############################################## __getattr__,__setattr__,__delattr__ ##################


class Foo:

    def __init__(self, name='xiaobai'):
        self.name = name
        pass

    def t(self):
        pass

    def __getattr__(self, item):
        """
        只有在使用点调用属性且属性不存在的时候才会触发
        :param item:
        :return:
        """
        print('正在查找不存在的%s'%item)

        return '%s不存在'%(item)

    def __setattr__(self, key, value):
        """
        添加/修改属性会触发它的执行
        :param key:
        :param value:
        :return:
        """
        # 因为你重写了__setattr__, 凡是赋值操作都会触发它的运行, 你啥都没写, 就是根本没赋值,
        # 除非你直接操作属性字典, 否则永远无法赋值
        print('正在添加或修改属性%s %s'%(key, value))

        # self.key = value             # 该操作会触发递归调用

        self.__dict__[key] = value     #  正确的操作方法

    def __delattr__(self, item):
        """
        删除属性的时候会触发
        :param item:
        :return:
        """
        print('将要删除属性%s'%(item))

        # del self.item                  #  递归了

        self.__dict__.pop(item)          #  正确操作




# f = Foo()
##################### 查看获取属性
# print(f.__dict__, f.__dir__())
# print(f.name)
# print(f.name_new)
# print(f.t)

##################### 添加修改属性
# print('#'*20)
# f.name_new = 'sb'
# print(f.__dict__)
# print(f.name_new)

##################### 删除属性
# print('#'*20)
# f.__dict__['k'] = 'v'
# del f.k
# print(f.k)
# print(hasattr(f, 'k'))
# print(getattr(f, 'k'))
# print(getattr(f, 'kfc'))
# setattr(f, 'kk', 'vv')


################################################# __getattribute__ ############################

class Foo:
    def __init__(self,x):
        self.x=x

    def __getattr__(self, item):
        print('属性不存在，执行的是我')
        # return self.__dict__[item]

    def __getattribute__(self, item):
        print('不管属性是否存在,我都会执行')
        # raise AttributeError('哈哈')          # 当抛出AttributeError异常，会去调用__getattr__
        # return self.__dict__[item]            # 错误操作 会触发递归调用
        # return 111111111
        return super().__getattribute__(item)   # 正确操作

    def t(self):
        pass

# f=Foo(10)
# print(f.x)
# print(f.t)
# print(hasattr(f, 't'))

##################################### __setitem__,__getitem__,__delitem__ #######################
# 当已括号[]的方式调用、赋值、删除时才会调用这些方法

class Foo:

    def __init__(self, name):
        self.name = name
        pass

    def __getitem__(self, item):
        print('__getitem__', item)
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('__delitem__', key)
        self.__dict__.pop(key)

    def t(self):
        pass

# f = Foo('xiaobai')
# print(f.name)         # 不会触发__getitem__方法
# print(f['name'])      # 触发__getitem__方法
# print(f['t'])         # 报错 只能获取属性
# f['k'] = 'v'          # 设置属性
# del f['k']            # 删除属性

############################################### __str__,__repr__ #####################
# 如果__str__没有被定义,那么就会使用__repr__来代替输出
# 如果两者都没定义 返回类似<__main__.Person object at 0x0000000005A28860>
# 注意:这俩方法的返回值必须是字符串,否则抛出异常
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):

        return '(%s, %s)'%(self.name, self.age)

    def __repr__(self):

        return 'Person(%s, %s)'%(self.name, self.age)

# p =Person('xx', 20)

# print(p)         # print()或者str()方法都会调用__str__()方法
# print(repr(p))   # repr()或者在交互式解释器都会调用__repr__()方法
# print(repr('hello'))

################################################ 类变量__slots__ ###########################
"""
1.__slots__是什么:是一个类变量,变量值可以是列表,元祖,或者可迭代对象,也可以是一个字符串(意味着所有实例只有一个数据属性)
2.引子:使用点来访问属性本质就是在访问类或者对象的__dict__属性字典(类的字典是共享的,而每个实例的是独立的)
3.为何使用__slots__:字典会占用大量内存,如果你有一个属性很少的类,但是有很多实例,为了节省内存可以使用__slots__取代实例的__dict__
当你定义__slots__后,__slots__就会为实例使用一种更加紧凑的内部表示。实例通过一个很小的固定大小的数组来构建,而不是为每个实例定义一个
字典,这跟元组或列表很类似。在__slots__中列出的属性名在内部被映射到这个数组的指定小标上。使用__slots__一个不好的地方就是我们不能再给
实例添加新的属性了,只能使用在__slots__中定义的那些属性名。
4.注意事项:__slots__的很多特性都依赖于普通的基于字典的实现。另外,定义了__slots__后的类不再 支持一些普通类特性了,比如多继承。
大多数情况下,你应该只在那些经常被使用到的用作数据结构的类上定义__slots__比如在程序中需要创建某个类的几百万个实例对象 。
关于__slots__的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属性。
尽管使用__slots__可以达到这样的目的,但是这个并不是它的初衷。
更多的是用来作为一个内存优化工具。
"""

class Foo:

    __slots__ = ('name', 'age')

f = Foo()
f.name = 'xx'
# print(f.__dict__)           # 会报错
# print('hello'.__dict__)     # 会报错

"""
__slots__对子类没有限制
如果要限制子类的实例动态添加属性和方法，则需要在子类中也定义 __slots__ 属性，这样，子
类的实例允许动态添加属性和方法就是子类的＿slots__ 元组加上父类的＿slots＿元组的和。
"""
class FooC(Foo):
    pass

# fc = FooC()
# fc.n = 1                 # __slots__对子类没有限制

##################################################### __doc__,__module__,__class__,__call__

# __doc__ 返回描述信息
# __module__ 返回当前操作的对象在那个模块
# __class__ 返回当前操作的对象的类是什么
# __call__ 让对象可以像函数一样调用

import random
class Foo:
    """大傻蛋
    """
    def __call__(self, *args, **kwargs):
        print('可以像函数一样调用')

# f = Foo()
# print(f.__doc__)            # 返回描述信息
# print(Foo.__doc__)
#
# r = random.randrange(1, 3)
# print(r.__doc__)
# print(random.randrange.__doc__)
# ####################################
# print(f.__module__)            # 表示当前操作的对象在那个模块
# print(Foo.__module__)          #
# print(f.__class__)             # 表示当前操作的对象的类是什么
# print(Foo.__class__)
# print(object.__class__)
# ####################################
#
# f = Foo()
# f()

################################################# __len__, __contains__, __int__, __hash__

class Square(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __len__(self):
        """
        决定序列中元素的个数
        :return:
        """
        return self.width

    def __contains__(self, item):
        """
        判断是否包含指定元素
        :param item:
        :return:
        """
        return  True

    def __int__(self):
        """
        对int()函数提供支持
        :return:
        """
        return int(self.width * self.height)

    def __hash__(self):
        """
        对hash()函数提供支持
        :return:
        """
        return 1111111111111111

# sq = Square(20, 10)
# print(len(sq))    # 20
# print(1 in sq)    # True
# print(int(sq))    # 200
# print(hash(sq))   # 11111111111111

################################################ 数学运算符、比较运算符 #############################

class Square(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        """
        支持对象的相加操作 +
        :param other:
        :return:
        """

        return self.size + other.size

    def __ge__(self, other):
        """
        支持对象的大于或等于操作 >=
        :param other:
        :return:
        """
        return self.size >= other.size

    @property
    def size(self):
        return self.width * self.height

# s1 = Square(10, 10)
# s2 = Square(20, 20)
#
# print(s1 + s2)
# print(s1 >= s2)