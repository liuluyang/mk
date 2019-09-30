

"""
class第二阶段学习
面向对象的三大特征：封装、继承和多态
"""

"""
私有属性和方法

作用：
限制属性和方法的随意调用和修改,使代码更加健壮
"""

"""
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__age__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，
请把我视为私有变量，不要随意访问”。
"""
class Person:

    def __init__(self, name, age, role):
        if not 0<=age<=200:
            raise ValueError('年龄输入错误')
        self.__name = name
        self.__age = age
        self.__role = role
        self.IQ = 200
        pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not 0<=age<=200:
            raise ValueError('年龄输入错误')
        self.__age = age

    def info(self):
        """
        获取个人信息
        :return:
        """
        data = (self.__name, self.__age, self.__role)
        return data

    def birthday(self):
        """
        过生日
        :return:
        """
        self.__age += 1
        print('{}又长了一岁'.format(self.__name))

        return self.__age

    # 把该方法当做属性调用
    @property
    def isAdult(self):
        """
        判断是否成年
        :return:
        """
        if self.__age >= 18:
            print('年龄{}岁,已成年'.format(self.__age))
            return True
        else:
            print('年龄{}岁,未成年'.format(self.__age))
            return False

# p = Person('小绿', 20, '学生')
# # print(p.__name)
# print(p.isAdult)


"""
继承和多态
继承：
1、继承父类所有方法属性
2、子类可以添加新的方法
3、使用super()显式的调用父类方法
多态：
相同的方法作用在不同对象上返回不同的结果
"""

class Girl(Person):

    # def __init__(self, name, age, role):
    #     self.name = name
    #     self.age = age
    #     self.role = role
    #     pass

    def __init__(self, name, age, role):
        super().__init__(name, age, role)
        pass

    def hz(self):
        print('化妆之后更漂亮了')

    #
    # def info(self):
    #     data = (self.__name, self.__role)  # 无法调用父类私有属性 只能通过公开方法
    #     return data

g = Girl('小新', 200, '学生')
# print(g.isAdult)  # 调用父类方法
# print(g.IQ)
# g.name = 10
# print(g.name)
# print(g.info())
# print(dir(g))

"""
多态:
可以对不同的对象调用同名的操作（方法）
"""
class Test1:

    def read(self):
        return '我正在写代码。。。'

class Test2:

    def read(self):
        return '我不知道在干吗。。。'

f = open('readme.md', 'r', encoding='utf8')
t1 = Test1()
t2 = Test2()

def run(obj):
    print(obj.read())

# run(f)
# run(t1)
# run(t2)


"""
类的方法和属性
以及静态方法
"""

class D:
    nums = 0

    def __init__(self, nums):
        self.nums = nums
        D.nums += 1

    # 这是一个类方法
    @classmethod
    def addnums(cls):
        cls.nums += 1
        return cls.nums

    # 静态方法
    @staticmethod
    def other():

        return 2**10

    @staticmethod
    def newcls():
        return D(110)

    # @classmethod
    # def newcls(cls):
    #     return cls(110)

    def __str__(self):
        return 'I am D'


# d1 = D(10)
# d2 = D(11)
# print(d1.nums)
# print(D.nums)
# print(D.addnums())
# print(D.other())

class DD(D):

    def __str__(self):
        return 'I am DD'

# obj = DD.newcls()
# print(obj)

"""

"""

class Employe:

    def __init__(self, name):
        self.name = name

    def info(self):
        print('我是%s'%self.name)

class Customer:

    def __init__(self, age):
        self.age = age

    def work(self):
        print('正在工作', self.age)

class Manager(Customer, Employe):

    def __init__(self, age, name):
        super().__init__(age)
        # self.name = name
        # super().__init__(name)
        Employe.__init__(self, name)
        pass
    pass

def other(self):
    print('this is other func')

m = Manager(12, 'lly')
# m.work()
# m.info()

# Manager.other = other


"""
限制动态添加属性和方法
"""
from types import MethodType


"""
__slots__ 属性指定的限制只对当前类的实例对象起作用。
如果要限制子类的实例动态添加属性和方法，则需要在子类中也定义 slots 属性，这样，子
类的实例允许动态添加属性和方法就是子类的＿slots__ 元组加上父类的＿slots＿元组的和。

"""

class M:
    """
    只可以限制实例对象动态添加某些方法
    """
    __slots__ = ('name', 'other')

class MM(M):
    """
    如果有继承同时子类也进行了限制
    """
    __slots__ = ('age', 'sex')  # 没有了__dict__属性

# m = MM()
# m.name = lambda x:print(x)
# m.name(1)


"""
元类metaclass
用来控制类的创建
"""

class CheckMethodName(type):

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        attrs = args[-1]
        print(attrs.get('read'))
        return type.__new__(cls, *args, **kwargs)

class Ne(metaclass=CheckMethodName):

    is_check = True

    def __init__(self, text):
        self.text = text

    def read(self):
        print(self.text)

# n = Ne('hello world')
# n.read()