



class Person:
    # 作用域

    # 类属性
    # 可以被类或者对象来调用
    country = '中国'
    count = 0
    # 解析的过程中 会执行类里面可执行的代码
    # print(111111111111)

    def __init__(self, name, age):

        self.name = name
        self.age = age
        # self.country = '111111'
        Person.count += 1

    def w(self):
        pass

    # print(2222222222)

# 实例化的过程
# 绑定(bound)属性和方法
p = Person('老王', 40)
p2 = Person('小王', 20)
p3 = Person('小王2', 20)

# 对象属性查找顺序: 对象属性 =》类属性
# print(p.country)
# 类调用类属性
# print(Person.country)

# p2对象添加自己的属性、对其他对象或者类的属性没有影响
# p2.country = '美国'

Person.country = '美国'

# print(p.count)
# print(p.country)
