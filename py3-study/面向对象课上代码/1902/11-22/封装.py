


"""
封装
"""


class Person:

    def __init__(self, name, age):

        # __  可以把对象属性私有化
        # 外部无法对私有属性进行修改
        # 内部可以修改
        self.__name = name
        self.__age = age

    # @property 把一个方法进行装饰 让他可以向属性一样调用
    # 被装饰的方法不能有其他参数
    @property
    def name(self):
        """
        查看私有属性
        :return:
        """
        return self.__name

    def setname(self, name_new):
        """
        修改私有属性
        :param name_new:
        :return:
        """
        # print(name_new)

        if isinstance(name_new, str):
            self.__name = name_new


# p = Person('刘海柱', 40)
#
# # 查看私有属性
# # print(p.getname())
#
# # 修改私有属性
# # p.setname(['老王'])
#
# print(p.name, 1111111)

#################################################### 属性私有化

class Person:

    def __init__(self, name, age):

        # __  可以把对象属性私有化
        # 外部无法对私有属性进行修改
        # 内部可以修改
        self.__name = name
        self.__age = age

    @property
    def name(self):
        """
        查看私有属性
        :return:
        """
        return self.__name

    @name.setter
    def name(self, name_new):
        """
        修改私有属性
        :param name_new:
        :return:
        """
        # print(name_new)

        if isinstance(name_new, str):
            self.__name = name_new
        else:
            print('类型错误')


# p = Person('刘海柱', 40)
#
# # p.name = ['laowang']  # => @name.setter
# print(p.name)         # => @property


##################################################### 方法私有化


import os

class Test:

    def __count_code(self, filepath):

        with open(filepath, 'rb') as f:
            num = 0
            for line in f:
                line = line.strip()
                if line:
                    num += 1
            return num

    def func_09(self):

        file_names = os.listdir('.')
        dic = {}
        for filename in file_names:
            if filename.endswith('.py'):
                dic[filename] = self.__count_code(filename)

        return dic

# t = Test()
# print(t.func_09())




















