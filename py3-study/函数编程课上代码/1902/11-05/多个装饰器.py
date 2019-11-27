




def outer01(func):
    print('outer01')
    def inner01():

        print(1111)
        func()
        # print(1111)


    return inner01


def outer02(func):
    print('outer02')
    def inner02():

        print(2222)
        func()
        # print(2222)

    return inner02


@outer01
@outer02
def func():

    print('this is func')

# func = outer01(outer02(func))  # 多个装饰器的函数嵌套关系

# func
# print(func.__name__)
# func()                         # 函数执行顺序 inner01 => inner02


############################################## 函数签名

def test():
    pass

# t = test
# print(t.__name__)