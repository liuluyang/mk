



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


"""
2. 说出下面代码的执行结果：
def num_add(num):

    if num >= 10:
        return 11
    num += 1
    print(num)

    num_add(num)

    print(num)
    
num_add(1)
"""


"""
3. 说出下面代码的执行结果：
def num_add(num):

    if num >= 10:
        return 11
    num += 1
    print(num)

    print(num_add(num))

    print(num)

num_add(1)
"""


"""
4. 说一下 可迭代对象、迭代器对象、生成器函数、生成器对象分别是什么以及他们的区别：
"""
