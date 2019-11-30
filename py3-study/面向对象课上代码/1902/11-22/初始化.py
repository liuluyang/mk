


class Person:

    def __init__(self, name, age, sex='girl'):

        # 实例化之后会执行 初始化函数
        # 给对象添加属性
        # print(name, '__init__')

        self.name_new = name
        self.age_new = age
        self.sex = sex

    def walk(self):

        print('%s 正在走路。。。'%(self.name_new))

    def eat(self):

        self.walk()
        self.walk()
        print('%s 正在吃饭。。。'%(self.name_new))

    def info(self):

        return self.name_new, self.age_new, self.sex


p = Person('小绿', 22)
# 外部修改属性
p.name_new = '小黑'

# 外部删除属性
# del p.name_new

# 外部 手动添加属性
# p.name = '小绿'

# print(p.name_new, p.age_new)

# p.walk()
# p.walk()

# p.eat()

# print(p.info())