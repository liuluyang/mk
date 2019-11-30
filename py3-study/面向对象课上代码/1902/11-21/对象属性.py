


class Person:

    def __init__(self, name, age):  # 初始化方法
        """
        # 初始化方法（构造方法）、实例化对象时会自动的执行该方法
        # 给对象绑定属性、供自身（self）调用
        :param name:
        :param age:
        """
        # print('初始化的时候执行我')
        # print(name, age)

        print('内部self:', self)
        self.name = name
        self.age = 22

        # self.walk()
        # print(self.name)

    def walk(self):

        print('我是%s，我在走路！！！！！！！！！！！！'%(self.name))
        print(self.age)

    def eat(self):
        # self 自己

        # self.walk()
        print('%s正在吃饭'%(self.name))
        pass


p = Person('小黑', 22)
# print('外部p:', p)
# # p.walk()
# p.eat()
# p.name = 'xx'
# print(p.name)

# 当调用对象方法时 p会被当做方法的第一个参数self传入
# p.walk()
# Person.walk(p)


###########################################

import random

class Beer:

    def __init__(self):

        self.uid = int(random.random()*100000)


# beer_list = []
# for i in range(100):
#     b1 = Beer()
#     beer_list.append(b1)
#
# print(len(set(beer_list)))
#
# print(beer_list[0].uid)
















