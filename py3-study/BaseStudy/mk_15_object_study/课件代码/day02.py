
"""

"""
"""
完成以下功能:
    老王/40岁/男/喜欢开车
    老王/40岁/男/喜欢串门
    老王/40岁/男/喜欢大宝剑
"""

# ##################### 函数版本 #########################

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

########################### 面向对象1 #################################
class Person01:

    def hobby_01(self, name, age, gender):
        data = "%s,性别%s,今年%s岁,喜欢开车" % (name, gender, age)
        print(data)

    def hobby_02(self, name, age, gender):
        data = "%s,性别%s,今年%s岁,喜欢串门" % (name, gender, age)
        print(data)

    def hobby_03(self, name, age, gender):
        data = "%s,性别%s,今年%s岁,喜欢大宝剑" % (name, gender, age)
        print(data)

# p = Person01()
# p.hobby_01('老王', 40, '男')

########################### 面向对象2 #################################
class Person02:

    def __init__(self, name, age, gender):       # 初始化方法（构造方法）、实例化对象时会执行该方法
        self.name = name                         # 给对象绑定属性、供自身（self）调用
        self.age = age
        self.gender = gender

    # def walk(self):
    #     print('%s正在走路'%(self.name))
    #
    # def eat(self):
    #     print('%s正在吃饭。。。'%(self.name))

    def hobby_01(self):
        data = "%s,性别%s,今年%s岁,喜欢开车" % (self.name, self.gender, self.age)
        print(data)

    def hobby_02(self):
        data = "%s,性别%s,今年%s岁,喜欢串门" % (self.name, self.gender, self.age)
        print(data)

    def hobby_03(self):
        data = "%s,性别%s,今年%s岁,喜欢大宝剑" % (self.name, self.gender, self.age)
        print(data)

    def main(self):
        self.hobby_01()
        self.hobby_02()
        self.hobby_03()


# p = Person02('老王', 40, '男')
# Person.hobby_01(p)

# p就是类里面的self
# 当调用对象方法时 p会被当做方法的第一个参数self传入
# p.hobby_01()           # 相当于Person.hobby_01(p)

####################################### 对象属性、类属性 #########################

class Person03:

    # 被其它对象共享
    country = 'china'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):
        print('%s正在走路'%(self.name))

    def eat(self):
        print('%s正在吃饭。。。'%(self.name))

    def birthday(self):

        self.age += 1          # 通过方法改变属性值
        print('%s过生日'%(self.name))

        return self.age

    def getInfo(self):

        return (self.name, self.age, self.gender, Person03.country)

p = Person03('老王', 40, '男')
p2 = Person03('小花', 20, '女')

# 属性增删改查
# 对象可以调用类的属性、类不可以调用对象的属性

print(p2.getInfo())
print(p.country)
print(p.name)
del p.name
p.name = '隔壁老李'
print(p.name)

