


"""

1、父类的私有属性和方法不可继承

2、重写父类的初始化方法

3、重用父类的方法
    父类名.父类方法(self)
    super().父类方法()
"""


class Person:

    def __init__(self, name):
        self.name = name

    # def walk(self):
    #
    #     print('一步一步走。。。')

    def eat(self):
        print(self)

        print('一口一口的吃。。。', self.name)

#############################

class F:

    def walk(self):
        print('三步。。。')

class LaoWang(Person, F):

    # 重写初始化函数
    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.__sex = 'man'

    def __hobby_03(self):

        print('嘿嘿嘿。。。')

    # 可以重写父类的方法
    def walk(self):

        # 调用父类的方法 **
        # Person.walk(self)

        # 自动按顺序查找父类方法
        # super().walk()

        print('两步两步走。。。')

lw = LaoWang('laowang', 40)
# print(lw.name)
# lw.eat()
# lw.walk()

##############################

class XiaoWang(LaoWang):

    def walk(self):

        print('半步半步走。。。')

    def find(self):

        # 无法调用父类的私有方法
        # self.__hobby_03()
        # print(self.__sex)
        pass

# xw = XiaoWang('xiaohei', 20)
#
# print(xw.find())


###########################################


class ListNew(list):

    def append(self, obj):

        print(obj, 'append_new')

        # self.append(obj) # 递归调用

        # 重新调用父类的方法
        # list.append(self, obj)

        if not isinstance(obj, int):
            super().append(obj)
        else:
            raise TypeError('类型错误')


lst = ListNew(['a', 'b', [1, 1]])
lst.append(1)
print(lst)


######################################

class Vehicle02:  # 定义交通工具类

    def __init__(self, name, speed, power):
        self.name = name
        self.speed = speed
        self.power = power

    def run(self):
        print('开动啦...')


class Subway02(Vehicle02):  # 地铁

    def __init__(self, name, speed, power, line):
        Vehicle02.__init__(self, name, speed, power)
        # super().__init__(name, speed, power)
        # self.name = name
        # self.speed = speed
        # self.power = power
        self.line = line

    def run(self):
        print('地铁%s号线欢迎您'%self.line)
        # print('开动啦...')
        # Vehicle02.run(self)
        super().run()

# sub = Subway02('中国地铁', '180m/s', '电', 1)
# sub.run()