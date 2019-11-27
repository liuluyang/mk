


"""
1. 说出下面代码的执行结果
def inner():
    print('我是小函数')

    return 1

def outter():
    print('我是大函数')

    return inner


inner()
print(inner())
outter()
print(outter())

def outter():
    print('我是大函数')

    return inner()

outter()
print(outter())
"""

def inner():
    print('我是小函数')

    return 1

def outter():
    print('我是大函数')

    return inner()

# inner()
# print(inner())

# outter()
# print(outter())