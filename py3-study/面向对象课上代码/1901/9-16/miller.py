# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/16 16:58


# class Foo(object):
#     def hobby_01(self):
#         print("sing", self)
#     def hobby_02(self):
#         print("jump", self)
#     def main(self):
#         print("这是self", self)
#         self.hobby_01()
#         self.hobby_02()
#
#     def __str__(self):
#         return "我是 Foo"


# class Sub(Foo):
#     def hobby_03(self):
#         print("rab", self)
#
#     def __str__(self):
#         return "我是 Sub"


# sub1 = Sub()
# f1 = Foo()


# print(Sub.mro())
# sub1.hobby_01()


# def say_hi():
#     print("hi")

# def say_hello():
#     print("hello")


# __dict__ = {"say_hi": say_hi, "say_hello": say_hello}
#
# __dict__.say_hello()


# for i in [<class '__main__.Sub'>, <class '__main__.Foo'>, <class 'object'>]:
#     if i.get("hobby_01"):
#         return i.get("hobby_01")
# else:
#     "报错"


class MyProperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(instance, "from instance")
        return self.func(instance)


class Director:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        def director(*args, **kwargs):
            self.func(instance, *args, **kwargs)
        return director

    def __set__(self, instance, value):
        pass


class Str(object):
    def __get__(self, instance, owner):
        print("调用__get__ from Str")
    def __set__(self, instance, value):
        print("调用__set__  from Str")

class Int(object):
    def __init__(self, age):
        self.age = age
    def __get__(self, instance, owner):
        print("调用__get__, from Int")
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("必须是整数")
        instance.__dict__[self.age] = value



class Foo:
    name = Str()
    age = Int("age")
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @MyProperty
    def name_age(self):
        return "%s is %s years old" % (self.name, self.age)

    @Director
    def talk(self, msg):
        print(msg)


f1 = Foo("miller", 26)
# print(f1, "from f1")
# print(f1.name_age)

# f1.talk("aljsdjslfhd")

# print(f1.__dict__)

f1.name
f1.age
