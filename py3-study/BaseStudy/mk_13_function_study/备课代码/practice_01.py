

"""

"""

"""
考察函数的调用及返回
"""
def inner():
    print('我是小函数')

    return 1

def outter():
    print('我是大函数')

    return inner    # inner()

inner()


"""
考察对递归的理解
"""

def num_add(num):

    if num >= 10:
        return 11
    num += 1
    print(num)

    num_add(num)

    print(num)


num_add(1)

