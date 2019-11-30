

import uuid

def uid():

    # 生成唯一的一段字符串
    return uuid.uuid1()


class Person:

    country = '中国'
    __count = 0

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Person.__count += 1
        self.id = self.make_uid()

    # 把一个方法变成类方法
    # 类方法尽量通过类来调用
    @classmethod
    def count(cls):
        print(cls)
        return cls.__count

    @classmethod
    def make_instance(cls):
        print(cls)
        return cls('老王', 40)

    # 静态方法
    @staticmethod
    def make_uid():

        return uuid.uuid1()


p = Person('老王', 40)


# print(p.count())
# print(Person.count)

# print(Person)

# 类调用类方法
# print(Person.count())
# print(Person.make_instance())
# 实例对象来调用类方法
# print(p.make_instance())

# print(p.make_uid())
# print(p.id)



############################################# 对象类型

class F(Person):

    pass

f = F('老王', 40)

print(Person)
print(type(p))

print(isinstance(1, int))
print(isinstance(f, Person))

"""
对象(object)：
    万物皆对象、对象皆可分类

类(class)=> 实例对象(instance)

# type() 查看一个对象是由谁创建的
# 或者说查看一个对象的类型
"""
