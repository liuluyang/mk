
import functools

"""

闭包及装饰器
"""

"""
闭包
"""

def outer():
    name = 'hello'
    def inner():
        print("在inner里打印外层函数的变量",name)
    return inner
f = outer()
# print(f)
# f()

"""
装饰器
"""
import time

def run_time(func):
    print('121', func.__name__)
    # @functools.wraps(func)
    def inner(*args, **kwargs):
        print('开始调用')
        t_start = time.time()
        r = func(*args, **kwargs)
        print('用时：', time.time() - t_start)

        return r
        # return func(*args, **kwargs)

    return inner

def run_time_2(func):
    print("123",func.__name__)
    def inner2(*args, **kwargs):
        print('开始调用2')
        t_start = time.time()
        r = func(*args, **kwargs)
        print('用时2：', time.time() - t_start)

        return r
        # return func(*args, **kwargs)

    return inner2


@run_time_2
@run_time
def count_(num):
    # t_start = time.time()
    time.sleep(2)
    r = 3*20*num
    print('计算结果=>', r)
    # print(time.time() - t_start)
    return r

# count_(2)

# 实际执行流程
# 注意函数__name__属性的变化, 变成了装饰器内层函数的__name__
# print(count_(123))
# f2 = run_time(count_)
# print(f2)
# f2(2)

#f2 = run_time_2(run_time(count_))  # inner2(inner)
# print(f2)
# f2(2)

"""
121 count_
123 inner
开始调用2
开始调用
count_ result 120
用时： 2.0001144409179688
用时2： 2.0001144409179688
"""