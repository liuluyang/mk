



"""
继承：
    好处
    语法
    添加新方法
    重写父类方法
    方法的查找顺序
"""

# 人类
# 在继承里面：父类、超类
class Person(object):

    # def __init__(self, name):
    #     self.name = name

    def walk(self):

        print('一步一步走。。。')

    def eat(self):

        print('一口一口的吃。。。')


# 非洲人
class African:

    def __init__(self, name):
        self.name = name
        self.skin_color = '黑色black'

    def walk(self):

        print('一步一步走。。。')

    def eat(self):

        print('一口一口的吃。。。')

    def run(self):

        print('flying...')


#########################################################

# 子类
class LaoWang(Person):

    def hobby_01(self):

        print('乐于助人。。。。')

    # 自己的方法
    def hobby_02(self):

        print('串门。。。')

    # 可以重写父类的方法
    def walk(self):

        print('两步两步走。。。')


lw = LaoWang()
lw02 = LaoWang()
# print(lw, lw02)
"""
继承中方法的查找顺序：
    自己 =》父类 =》
"""
# lw.walk()


class XiaoWang(LaoWang):

    pass

# xw = XiaoWang()
# xw.walk()


################################################


class StrNew(str):

    def w(self):

        print('...........')

    def count(self, x):

        return '123111111111111'


s = StrNew(1123)
# print(s, type(s))
# print(len(s))
# print(s.w())

print(s.count('1'))

# print(type('hello'))






