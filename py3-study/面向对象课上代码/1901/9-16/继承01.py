# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/16 14:27


# 父类
class Person:

    def __init__(self, name, age):
        pass

    def walk(self):
        pass

    def hobby_01(self):
        print('爱好')

    def func_01(self):
        print('func_01')

    def func_02(self):
        print('func_02')

    def main(self):
        """
        主函数
        :return:
        """
        self.func_01()
        self.func_02()
        # self.func_03()
        print('main')


# 子类
class LaoWang(Person):
    # 只是单纯的继承
    # 所有属性、方法共用父类的
    pass

    # 覆盖、重写
    def hobby_01(self):

        print('串门')

    def hobby_02(self):
        print('开车LaoWang')

    def func_03(self):
        print('func_03')

    # 即重写了父类的方法，又调用了父类的方法
    def main(self):
        # self.func_01()
        # self.func_02()
        # print(1)

        self.func_03()
        Person.main(self)


class XiaoMing(LaoWang):

    def hobby_01(self):
        print('看书')



lw = LaoWang('老王', 44)
xm = XiaoMing('小明', 18)
p = Person('xiaohei', 22)

# Person.main(lw) # p.main()

# xm.hobby_01() # XiaoMing.hobby_01(xm)


#############################################  类属性


class Foo(object):

    country = '中国'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        # self.country = country


f = Foo('kk', 22, '女')

Foo.country = '美国'
print(f.country)
print(f.__dict__)
