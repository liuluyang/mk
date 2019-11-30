# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/7 20:14

"""--"""

# ################# 测试 __setattr__, __getattr__, __delattr__ ##################
"""--"""

# class Person(object):
#     name = "alex"
#
#     def __init__(self, position, age):
#         self._position = position
#         self.age = age
#
#     def __setattr__(self, key, value):  # (实例对象.属性名 = 值)在进行赋值操作的时候, 才会触发 __setattr__ 这个方法
#         # 每一次赋值都会优先触发一次该方法的执行。
#         super().__setattr__(key, value)
#
#     def __getattribute__(self, item):  # 只要通过 实例对象.key 取值就会触发这里的执行。
#         # 而为了避免递归调用, 所以需要 使用父类的 __getattribute__ 方法进行返回值。
#         return super().__getattribute__(item)
#
#     def __getattr__(self, item):  # 只有在 (实例对象.属性名) 并且属性名不存在时才会触发该方法的执行
#         return "你要找的 %s 不存在" % item
#
#     # 在 __getattribute__ 和 __getattr__ 同事出现的时候, 只会执行 __getattribute__ 除非该方法在执行过程当中
#     # 抛出 AttributeError 就会自动的转向 __getattr__
#
#     def __delattr__(self, item):  # 在使用 del (实例对象.属性名) 的时候被触发
#         self.__dict__.pop(item)
#         print("from __delattr__", self.__dict__)
#
#
# p1 = Person(123, 23)
#
# print(p1.position)
# print(p1.__dict__)


'''
总结:
    __setattr__ 在 (实例对象.key = value) 时，触发执行。
    (使用 = 赋值时就会执行, 不论是在 __init__ 中，还是在其他地方进行赋值, 都会触发)
    
    __getattr__ 在 (实例对象.key) 查找属性, 并且没有找到的时候才会触发, 这个方法的执行。
    __getattribute__  在使用 "." 运算符时，就会无条件被调用。
    __delattr__ 只在使用 del 关键字进行删除属性时，才会被调用。
'''

# class Person(object):
#     def __init__(self, position, age):
#         self._position = position
#         self.age = age
#
#     @property
#     def position(self):
#         return self._position
#
#     # 这种方式的赋值操作, 在程序运行过程中, 对实例对象的属性的更改行为会触发  @属性名.setter 装饰器的执行
#     @position.setter  # 此方法的优先级, 低于 __setattr__, 并且 __init__ 中的赋值操作, 不会触发该方法的执行。
#     def position(self, val):
#         if not isinstance(val, str):
#             raise TypeError("必须是字符串类型")
#         self._position = val


"""--"""
# ################# 测试 __set__, __get__, __delete__ ##################
'''描述符的本质就是一个 新式类, 在这个新式类中,至少实现了__set__(), __get__(), __delete__() 中的一个。
 这三种也被称作为 描述协议。
 __set__(), 为一个属性赋值时触发
 __get__(), 调用一个属性时触发
 __delete__() 采用del 删除一个属性时，触发。'''


# class Foo(object):
#     def __set__(self, instance, value):
#         print("调用了 __set__", self, instance, value)
#
#     def __get__(self, instance, owner):
#         print("调用了 __get__", self, instance, owner)
#
#     def __delete__(self, instance):
#         print("调用了 __delete__", self, instance)


'''描述符的作用就是,带另外一个类中的属性的(必须将描述符作为类的 类属性, 不能定义到 构造函数中)
并且 描述符类自身的实例对象，是不会触发这三个方法的执行的：  请看下面的例子：'''

# f1 = Foo()
# # f1.name = "miller"
# # print(f1.name)
# # del f1.name


'''以下演示何时被调用'''


# class Str(object):
#     def __set__(self, instance, value):
#         print("Str调用了 __set__")
#     def __get__(self, instance, owner):
#         print("Str调用了 __get__")
#     def __delete__(self, instance):
#         print("Str调用了 __delete__")
#
# class Int(object):
#     def __set__(self, instance, value):
#         print("Int调用了 __set__")
#     def __get__(self, instance, owner):
#         print("Int调用了 __get__")
#     def __delete__(self, instance):
#         print("Int调用了 __delete__")
#
#
# class Person(object):
#     name = Str()
#     age = Int()
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("miller", 123)
#
# p1.name
# p1.name = "liusir"
# del p1.name

# print(p1.__dict__)
# print(Person.__dict__)
# 查看实例的属性字典  和  查看类的属性字典。 可以看得出在一个类中定义 描述符就会被定义到 类的属性字典中。
'''
描述符分为两类：
    一、 至少实现了 __get__ 和 __set__ 的叫做， 数据描述符
    二、 没有实现  __set__  的叫做  非数据描述符
使用数据描述符的时候, 需要严格的遵循 他们的优先级。
1. 类属性
2. 数据描述符
3. 实例属性
4. 非数据描述符
5. 找不到的属性 触发调用 __getattr__
'''

'''1. 类属性 > 数据描述符'''

# class Str(object):
#     def __set__(self, instance, value):
#         print("调用了 __set__")
#     def __get__(self, instance, owner):
#         print("调用了 __get__",)
#     def __delete__(self, instance):
#         print("调用了 __delete__")
#
# class Person(object):
#     name = Str()
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
#
# Person.name  # 调用了 __get__
# # 描述符被定义成了一个类属性, 直接通过类名调用 name .本质就是在调用 描述符Str, 触发 __get__ 的执行
# Person.name = "alex"
# del Person.name
# # 但是 赋值操作 和 删除 操作！  并不会触发
# print(Person.__dict__)

'''原因：
描述符在使用的时候, 被定义成另外一个类的类属性。
而 类属性 是要比  二次加工的描述符伪装而来的类属性有更高的优先级。
所以:
Person.name  #调用类属性name 没有找到， 找不到就去找描述符伪装的类属性name. 从而触发 __get__() 的执行。

Person.name = "alex"  # 赋值操作也是如此, 直接赋值了一个类属性, 相当于覆盖了描述符. 所以不会触发 __set__()
del Person.name  # 删除的操作同样是如此

'''


'''2. 数据描述符 > 实例属性'''

# class Str(object):
#     def __set__(self, instance, value):
#         '''
#         :param self:   描述符自身的实例,
#         :param instance:  被代理的 类的实例
#         :param value:  要设置的值
#         '''
#         print("调用了 __set__", instance)
#     def __get__(self, instance, owner):
#         '''
#         :param self:   描述符自身的实例,
#         :param instance:  被代理的 类的实例
#         :param owner:  被代理的类自身
#         '''
#         print("调用了 __get__")
#     def __delete__(self, instance):
#         print("调用了 __delete__")
#
# class Person(object):
#     name = Str()
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("miller", 23)
#
# print(p1.__dict__)  # {'age': 23} 可以看出实例字典中并没有, name 这个属性。 因为他被数据描述符覆盖掉了。
# p1.name
# p1.name = "liuser"
# print(Person.__dict__)  # name 成为了一个 类属性(伪装的类属性)
# del p1.name


'''3. 实例属性 > 非数据描述符(只实现了 __get__() 方法)'''

# class Str(object):
#     def __get__(self, instance, owner):
#         print("调用了 __get__")
#
# class Person(object):
#     name = Str()
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("miller", 23)
#
# print(p1.__dict__)
# # 这时就可以看出, 非数据描述符的优先级要  低于实例属性。 所以对属性的操作, 都是对实例属性的操作, 而不是描述符
# print(p1.name)
# p1.name = "alex"
# del p1.name

'''函数 也是一个描述符， 而且函数是一个非数据描述符'''
# class Foo:
#     # 描述符都是类, 函数为什么也算是一个 非数据描述符呢？
#     # 1. 描述符确确实实 是一个类, 但是描述符使用的时候, 都是实例化成一个类属性。
#     # 2. 函数就是由一个 非数据描述符类，实例化而得到的对象。  字符串也一样。
#
#     # 所以调用函数 其实就是调用了一个 非数据描述符
#     def func(self):
#         print("调用了非数据描述符")
#
# f1 = Foo()
# f1.func()
# f1.func = "miller"
# print(f1.func)
# del f1.func



'''4. 非数据描述符(只实现了 __get__() 方法) > __getatter__'''

# class Str(object):
#     def __get__(self, instance, owner):
#         print("调用了 __get__")
#
# class Person(object):
#     name = Str()
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __getattr__(self, item):
#         print("%s 找不到时, 触发该方法的执行" % item)
#
# p1 = Person("miller", 23)
# # print(p1.__dict__)  # {'age': 23} 可以看出实例字典中并没有, name 这个属性。 因为他被数据描述符覆盖掉了。
# p1.name
# p1.liusir  # 没有这个属性时， 触发 __getatter__ 方法

'''使用数据描述符进行类型限制'''

class Str(object):
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, owner):
        print("调用 __get__ 方法")
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        instance.__dict__.pop(self.name)


class People(object):
    name = Str("xxxx")
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = People("miller", 23)

# print(p1.name)  # 通过__get__ 方法, 得到了我想要的

print(p1.__dict__)
print(People.__dict__["name"].__get__(p1, People))














