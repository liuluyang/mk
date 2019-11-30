# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/7 18:29

"""--"""

# ######################### 对 __dict__ 进行的测试 #######################
# 发现类在只继承 object 时,  和类在继承, 另一个继承了object的类时 的到的结果并不相同


# # 以下是继承了 另一个继承了object类时, 自身时并没有显示的继承object
# class Animal(object):
#     def __init__(self, type):
#         self.type = type
#
#
# class Person(Animal):
#     def __init__(self, name, age):
#         super().__init__("person")
#         self.name = name
#         self.age = age
#
#
# p1 = Person("alex", 12)
#
# print(Person.__dict__)  # __dict__ 中
# print(p1.__dict__)
#
# print("-" * 50)
# # {'__module__': '__main__', '__init__': <function Person.__init__ at 0x00000000021BC730>, '__doc__': None}
# # # {'type': 'person', 'name': 'alex', 'age': 12}
#
# # 以下是只继承 object 时
# class Person1:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p2 = Person1("alex", 12)
# print(Person1.__dict__)  # __dict__ 中
# print(p2.__dict__)
#
#
# # {'__module__': '__main__', '__init__': <function Person1.__init__ at 0x00000000021BC7B8>,
# # '__dict__': <attribute '__dict__' of 'Person1' objects>,
# # '__weakref__': <attribute '__weakref__' of 'Person1' objects>, '__doc__': None}
#
# # {'name': 'alex', 'age': 12}


"""--"""

# 测试 Form 组件中, Meta


class MyForm:
    class Meta:
        pass

# print(hasattr(MyForm, "Meta"))
#
# print(getattr(MyForm, "Meta", None))

n = type("Meta", (MyForm.Meta,), {'model': str})
print(n)


