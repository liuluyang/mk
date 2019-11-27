



def func_01():

    print('hello')
    print('world')


def func_02():
    """

    :return:
    """
    print('我是func_02')
    func_01()


# func_02()


def register(name, age, gender, position, country='中国'):

    print(name, age, gender, position, country)


def main():

    data = ['老王', 40, '男', '程序员', '德国', '1']

    data = dict(zip(['name', 'age', 'gender', 'position', 'country'], data))
    print(data)

    register(**data)


main()