


############################################# 类方法 ##########################

class Student:

    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.__count += 1

    @classmethod
    def getCount(cls):       # cls比Student的可读性、扩展性好
        return cls.__count

    def getNums(self):
        return Student.__count


# s1 = Student('老王', 40)
# s2 = Student('小绿', 20)
# print(s1.getNums())
# print(Student.getCount())

############################################ 静态方法 ###############################
import uuid

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.uid = self.getUid()

    @staticmethod
    def getUid():
        uid = str(uuid.uuid1()).replace('-', '')
        return uid

# s = Student('小白', 19)
# print(s.uid)

##################################### 类的约束 ##############################
# 老王和小白的故事

class QQpay:
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)

# a = Alipay()
# a.pay(100)
# b = QQpay()
# b.pay(200)


###################################### 02
# 老王把功能完善

class QQpay:
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)

def pay(obj,money):  # 这个函数就是统一支付规则，这个叫做： 归一化设计。
    obj.pay(money)

# a = Alipay()
# b = QQpay()
# pay(a,100)
# pay(b,200)

############################################# 03 新的需求
# 小白来写新的需求

class QQpay:
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:
    def pay(self,money):
        print('使用支付宝支付%s元' % money)

class Wechatpay:  # 野生程序员一般不会看别人怎么写，自己才是最好，结果......
    def zhifu(self,money):
        print('使用微信支付%s元' % money)

def pay(obj,money):
    obj.pay(money)

# a = Alipay()
# b = QQpay()
# pay(a,100)
# pay(b,200)
# c = Wechatpay()
# c.zhifu(300)

############################################ 04 完善限制
# 老王加班

class Payment:
    """
    此类什么都不做，就是制定一个标准，谁继承我，必须定义我里面的方法。
    """
    def pay(self,money):
        pass

class QQpay(Payment):
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay(Payment):
    def pay(self,money):
        print('使用支付宝支付%s元' % money)

class Wechatpay(Payment):  # 小白没看文档直接继承了Payment
    def zhifu(self,money):
        print('使用微信支付%s元' % money)

def pay(obj,money):
    obj.pay(money)

# a = Alipay()
# b = QQpay()
# c = Wechatpay()
# pay(a,100)
# pay(b,200)
# pay(c,300)       # 测试未发现异常，但付款没成功

############################################ 05 继续完善

class Payment:
    """
    此类什么都不做，就是制定一个标准，谁继承我，必须定义我里面的方法。
    """
    def pay(self,money):
        raise Exception("你没有实现pay方法")    # 老王想到一个绝妙的方法。。。

class QQpay(Payment):
    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay(Payment):
    def pay(self,money):
        print('使用支付宝支付%s元' % money)

class Wechatpay(Payment):
    def zhifu(self,money):
        print('使用微信支付%s元' % money)

    def pay(self,money):
        print('使用微信支付%s元' % money)

def pay(obj,money):
    obj.pay(money)

# a = Alipay()
# b = QQpay()
# c = Wechatpay()
# pay(a,100)
# pay(b,200)
# pay(c,300)

######################################## 抽象类

from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):    # 抽象类 接口类  规范和约束  metaclass指定的是一个元类
    @abstractmethod
    def pay(self, m): # 抽象方法
        pass

class Alipay(Payment):
    def pay(self,money):
        print('使用支付宝支付了%s元'%money)

class QQpay(Payment):
    def pay(self,money):
        print('使用qq支付了%s元'%money)

class Wechatpay(Payment):
    def pay(self,money):
        print('使用微信支付了%s元'%money)
    def recharge(self):
        pass

def pay(a,money):
    a.pay(money)

# a = Alipay()
# b = QQpay()
# c = Wechatpay()
# pay(a,100)
# pay(b,200)
# pay(c,300)

###################################### isinstance issubclass ###############

class StrNew(str):

    @property
    def len(self):
        return len(self)

# s = StrNew('老王上山去砍柴')
# print(s.len)
# print(s, type(s))              # type查看该对象是谁的实例
# isinstance检查该实例对象是否是由某个类（或者某类的父类、父类的父类等）实例化出来的
# 第一个参数是实例化对象，第二个参数是类对象
# print(isinstance(s, StrNew), isinstance(s, str), isinstance(s, object))
# 检查两个类是否有继承关系
# 两个参数传入的都是类对象
# print(issubclass(StrNew, str), issubclass(StrNew, object), issubclass(str, object))
#
# from typing import Iterable, Iterator
# print(isinstance('abc', Iterable))
# print(isinstance('abc', Iterator), isinstance(iter('abc'), Iterator))

################################################### 反射 #####################################

class Foo:
    f = '类的静态变量'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hi(self):
        print('hi,%s'%self.name)

# obj=Foo('小白',23)
#################################检测是否含有某属性
# print(hasattr(obj,'name'))
# print(hasattr(obj,'say_hi'))
# print(hasattr(obj, 'hihi'))
##################################获取属性
# n=getattr(obj,'name')
# print(n)
# func=getattr(obj,'say_hi')
# func()
# # print(getattr(obj,'aaaaaaaa')) #报错
# print(getattr(obj,'aaaaaaaa','不存在啊')) #不报错,返回错误信息
###################################设置属性
# def fun(self):
#     print(self.name*20)
# Foo.ff = fun         # 动态绑定方法
# obj.ff()
# setattr(obj,'is_boy',True)
# setattr(obj,'show_name',lambda self:self.name+'去小黑家串门')
# print(obj.__dict__)
# print(obj.show_name(obj))
###################################删除属性
# delattr(obj,'age')
# delattr(obj,'show_name')
# # delattr(obj,'show_name111') #不存在,则报错
# print(obj.__dict__)
################################### 获取类属性和方法
# print(getattr(Foo, 'say_hi'))
# print(getattr(Foo, 'f'))

#################################################### 反射应用 #####################

class User:
    def login(self):
        print('欢迎来到登录页面')

    def register(self):
        print('欢迎来到注册页面')

    def save(self):
        print('欢迎来到存储页面')

# 之前
def choose_01():
    u = User()
    while True:
        choose = input('>>>').strip()
        if choose == 'login':
            u.login()
        elif choose == 'register':
            u.register()
        elif choose == 'save':
            u.save()

# 之后
def choose_02():
    u = User()
    while True:
        choose = input('>>>').strip()
        if hasattr(u, choose):
            func = getattr(u, choose)
            func()