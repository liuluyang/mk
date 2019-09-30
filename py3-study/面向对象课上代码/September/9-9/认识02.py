# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/9 16:26



def hobby_01(name,age,gender):
   data = "%s,性别%s,今年%s岁,喜欢开车" %(name,gender,age)
   print(data)

def hobby_02(name,age,gender):
   data = "%s,性别%s,今年%s岁,喜欢串门" %(name,gender,age)
   print(data)

def hobby_03(name,age,gender):
   data = "%s,性别%s,今年%s岁,喜欢大宝剑" %(name,gender,age)
   print(data)

# hobby_01('老王', 40, '男')
# hobby_02('老王', 40, '男')
# hobby_03('老王', 40, '男')

class Person01:


    def __init__(self, name, age, gender, IQ=200):
        # 初始化函数（构造函数）
        # 当实例化对象的时候就会执行我
        print('当实例化对象的时候就会执行我')
        # self.name = 'laowang'
        # self.gender = 'nan'
        # self.age = 40

        self.name = name
        self.gender = gender
        self.age = age
        self.IQ = IQ

    def hobby_01(self):
        data = "%s,性别%s,今年%s岁,喜欢开车" % (self.name, self.gender, self.age)
        print(data, self.IQ)

    def hobby_02(self, name, age, gender):
       data = "%s,性别%s,今年%s岁,喜欢串门" % (name, gender, age)
       print(data)

    def hobby_03(self, name, age, gender):
       data = "%s,性别%s,今年%s岁,喜欢大宝剑" % (name, gender, age)
       print(data)


# p = Person01('老王', 40, '男')
# p.hobby_01()
# print(p.name)