




def func_01():

    a, b = 1, 1

    yield a
    yield b

    while True:
        n = a + b
        yield n

        a = b
        b = n

# f = func_01()
#
# for i in range(100):
#     print(next(f))


def func_02():

    # a, b = 1, 1
    a = b = 1

    while True:

        a, b = b, a+b
        yield b

# f02 = func_02()
#
# for i in range(10):
#     print(next(f02))


############################################# 变量赋值

a = 1
b = 1

m = (1, 2)

x, y = (1, 2)

h, g, k, p = 1, 2, 3, 4
