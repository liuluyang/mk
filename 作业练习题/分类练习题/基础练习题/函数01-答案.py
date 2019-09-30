
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
# 分别执行 查看结果


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
#   执行查看结果


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
#   执行查看结果


"""
4. 说一下 可迭代对象、迭代器对象、生成器函数、生成器对象分别是什么以及他们的区别：
"""
"""
学面向对象之前：
1. 一般我们认为 可作用于for循环的都是 可迭代对象，例如字符串。列表等
2. 一个可迭代对象被iter()函数转换之后，就变成了一个迭代器对象，next()函数可取出迭代器对象里面的值。
3. 生成器函数也是函数，只不过函数里面有yield关键字，也就是说函数里面有yield关键字的函数，我们就说他是生成器函数。
4. 生成器函数执行之后，就变成了一个生成器对象，生成器对象也是一个可迭代对象

from typing import Iterable, Iterator, Generator
上面导入的对象，可判断某一个对象的类型 例如：isinstance('hello', Iterale)
"""


