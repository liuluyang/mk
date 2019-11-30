

import time

def check_time(func):

    def inner(*args, **kwargs):

        t = time.time()
        f = func(*args, **kwargs)
        print('%s函数运行时间：%s'%(func.__name__, time.time() - t))

        return f

    return inner

res01 = 'abcd'*100000000
res02 = 'abcd'*1000000
# print(len(res01))
# print(id(res01), id(res02))
# print(res01)
# for i in res01:
#     print(id(i))
# for i in res02:
#     print(id(i))

@check_time
def func(res):

    for index in range(len(res)):

        s = res[index:index+100] == res02


# func(res01)

@check_time
def check_same():

    return res01 == res02


@check_time
def check_same_02():

    for x, y in zip(res01, res02):
        if x != y:
            return False

    return True

@check_time
def check_same_03():

    return hash(res01) == hash(res02)

# print(check_same())
# print(check_same_02())
# print(check_same_03())