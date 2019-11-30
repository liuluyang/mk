



"""
类  是一个概念性的东西 是对一批具有相同特征的东西的描述
"""

# 生产人的工厂
class Person:

    def walk(self):

        print('我是xxx，我在走路！！！！！！！！！！！！')

    def eat(self):

        print('我在吃饭、、、、')

    def sleep(self):

        print('正在睡觉。。。。。。。。。')

    def study(self):

        print('coding......')


# 生产一个具体的人
# 类的实例化的过程
# p是实例化出来的具体的对象
# 对象是一些属性和方法的集合 **

p = Person()
# 给对象添加属性 不太常用
p.name = '小黑'
p.age = 22
# 调用对象的属性
print(p.name, p.age)

p2 = Person()
print(p2)
# p3 = Person()
# print(p3)

# p.walk()
# p.walk()
# p.eat()
# p.study()
# p.sleep()

##################################################
class Dog:

    def run(self):

        print('二哈偷了隔壁家的肉，跑的很快')

    def __str__(self):

        return '二哈'


# d = Dog()
# print(d)
# d.run()

# s = str('dadadsasd')
# print(s)





