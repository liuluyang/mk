
import time


############################################### 装饰器传参

def check_time(func):

    def inner(*args, **kwargs):

        f = func(*args, **kwargs)

        return f

    return inner


# c = check_time(lambda x, y, z, h=111:x+y+z+h)
# r = c(1, 2, 3, h=222)
# print(r)
##################################################

@check_time
def add(num1, num2):

    print('this is add')
    r = num1 + num2
    time.sleep(1)

    return r


# add = check_time(add)  # 装饰器自己做的操作
#
# add(1, 2)


######################################## 函数调用传参的另一种方式


def add02(n, m, x=1, xx=1):

    print(n, m, x, xx)


# add02(1, 2)
# d = [11, 22]
# d02 = {'xx':33}
#
# add02(*d, **d02)













