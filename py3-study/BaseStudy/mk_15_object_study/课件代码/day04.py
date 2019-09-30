


######################################## 继承和多态 ###########################

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.IQ = 200

    def walk(self):
        print('%s正在走路。。。'%(self.__name))

    def eat(self):
        print('%s正在吃饭。。。'%(self.__name))

    @property
    def name(self):
        return self.__name


class LaoWang(Person):

    def hobby(self):
        print('%s正在邻居家。。。'%(self.name))

    def eat(self):
        print('%s正在邻居家吃饭。。。' % (self.name))

# lw = LaoWang('老王', 40)
# print(lw.name)
# lw.hobby()
# lw.walk()
# lw.eat()
"""
子类调用不到父类私有属性和方法，需要通过公开方法调用
"""

########################################### 在子类中重用父类方法01 ##################

class Vehicle:  # 定义交通工具类
    Country = 'China'

    def __init__(self, name, speed, power):
        self.name = name
        self.speed = speed
        self.power = power

    def run(self):
        print('开动啦...')


class Subway(Vehicle):  # 地铁
    def __init__(self, name, speed, power, line):
        Vehicle.__init__(self, name, speed, power)        # 重用父类方法
        self.line = line

    def run(self):
        print('地铁%s号线欢迎您'%self.line)
        Vehicle.run(self)


# line01 = Subway('中国地铁', '180m/s', '电', 1)
# line01.run()
# print(line01.Country)

########################################### 在子类中重用父类方法02 ##################

class Vehicle02:  # 定义交通工具类
    Country = 'China'

    def __init__(self, name, speed, power):
        self.name = name
        self.speed = speed
        self.power = power

    def run(self):
        print('开动啦...')


class Subway02(Vehicle02):  # 地铁
    def __init__(self, name, speed, power, line):
        # Vehicle02.__init__(self, name, speed, power)
        super().__init__(name, speed, power)
        self.line = line

    def run(self):
        print('地铁%s号线欢迎您'%self.line)
        # Vehicle02.run(self)
        super().run()


# line02 = Subway02('中国地铁', '180m/s', '电', 1)
# line02.run()
# print(line02.Country)

########################################### 多态 #######################################

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

