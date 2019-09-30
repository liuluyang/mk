

"""
封装、继承和多态
"""

######################################## 私有属性 ###################################
class Person:

    def __init__(self, name, age, role):
        if not 0<=age<=200:
            raise ValueError('年龄输入错误')
        self.__name = name
        # self.age = age       # 第二种赋值
        self.__age = age
        self.__role = role
        self.IQ = 200

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        print('setter age')
        if not 0<=age<=200:
            raise ValueError('年龄输入错误')
        self.__age = age

    def info(self):
        """
        获取个人信息
        :return:
        """
        data = (self.__name, self.__age, self.__role)
        return data

    def birthday(self):
        """
        过生日
        :return:
        """
        self.__age += 1
        print('{}又长了一岁'.format(self.__name))

        return self.__age

    # 把该方法当做属性调用
    @property
    def isAdult(self):
        """
        判断是否成年
        :return:
        """
        if self.__age >= 18:
            print('年龄{}岁,已成年'.format(self.__age))
            return True
        else:
            print('年龄{}岁,未成年'.format(self.__age))
            return False

p = Person('小绿', 20, '学生')
# p.age = 30
# print(p.isAdult)

