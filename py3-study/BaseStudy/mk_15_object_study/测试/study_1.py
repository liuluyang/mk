

"""
class学习
"""

"""
class的语法
"""
def t(num):
    print(3*3*num)

class Person:
    pass

p =  Person()
print(p, Person, t)

"""
完整的类的定义
以及属性和方法
类的实例化对象(object)

__ini__(self) 当该类实例化的时候该方法会被调用
self是类实例化之后的对象本身，方便对象内部方法属性的调用
"""
class Person:

    def __init__(self, name):   # 初始化传参
        print('进行初始化。。。')
        self.name = name
        pass

    def walk(self):
        print('我是{}'.format(self.name))
        print('我可以走路')

        return

# p = Person('小绿')
# print(p.name)
# p.walk()
# p.age = 10   # 添加属性 一般不这么用
# p.t = t      # 添加方法 一般不这么用
# print(p.age)
# p.t(4)


"""
对象的多个方法和属性
"""
class Person:

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        pass

    def walk(self):
        """
        走路方法
        :return:
        """
        print('我是{}'.format(self.name))
        print('我可以走路')

    def fly(self):
        """
        飞翔方法
        :return:
        """
        print('我是{}'.format(self.name))
        print('我可以飞')

    def info(self):
        """
        获取个人信息
        :return:
        """
        data = (self.name, self.age, self.role)
        return data

    def birthday(self):
        """
        过生日
        :return:
        """
        self.age += 1
        print('{}又长了一岁'.format(self.name))

        return self.age

    def isAdult(self):
        """
        判断是否成年
        :return:
        """
        if self.age >= 18:
            print('年龄{}岁,已成年'.format(self.age))
            return True
        else:
            print('年龄{}岁,未成年'.format(self.age))
            return False

# p = Person('小绿', 20, '学生')
# print(p.name, p.age, p.role)
# p.birthday()
# print(p.age)
# print(p.info())
# print(p.isAdult())

"""
把上述例子练一遍
"""







