

"""
函数的学习
"""

"""
函数的定义、调用及返回值

定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，
      要想执行这个函数，只需调用其函数名即可
      
特性:

1.减少重复代码

2.使程序变的可扩展

3.使程序变得易维护
"""
#最简单的函数
def func():
    pass   #占位符

func()



"""
形参：
只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。
因此，形参只在函数内部有效。函数调用结束返回主调用函数后则不能再使用该形参变量
"""

def power(x):
    return x * x

def power_2(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def power_3(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def func_2(n):
    # 在以下代码块编写任何你想做的事
    print(n)
"""
实参：
可以是常量、变量、表达式、函数等，无论实参是何种类型的量，
在进行函数调用时，它们都必须有确定的值，以便把这些值传送给形参。因此应预先给实参赋值
"""
# num = 2
# func_2(num)

"""
位置参数
返回值
如何调用返回值
注意：

函数在执行过程中只要遇到return语句，就会停止执行并返回结果，
so 也可以理解为 return 语句代表着函数的结束

如果未在函数中指定return,那这个函数的返回值为None
"""
def func_3(n, m):
    result = n + m
    print(n, m)

    return result

# num_1 = 2
# num_2 = 3
# func_3(num_1, num_2)

"""
关键字参数（默认参数）以及顺序,
以及重新赋值关键字参数
(使用默认参数有什么好处？最大的好处是能降低调用函数的难度)

正常情况下，给函数传参数要按顺序，不想按顺序就可以用关键参数，
只需指定参数名即可(指定了参数名的参数就叫关键参数)，
但记住一个要求就是，关键参数必须放在位置参数(以位置顺序确定对应关系的参数)之后
"""
def func_4(n, m=10):
    result = n + m

    return result

# func_4(4)
# func_4(5, 11)

"""
非固定参数
*args
**kwargs
"""
def func_5(n, m=10, *args, **kwargs):
    print(n, m)
    print(args, kwargs)

    result = sum(args)
    print()
# 关键字参数跟随在位置参数后面
# func_5(4,20,30,k=60)

def func_6(*args):
    print(args)

# nums = (1, 3, 4)
# func_6(1, 3, 4)  # 注:func_6(k=1)
# func_6(nums)
# func_6(*nums)


def func_7(**kwargs):
    print(kwargs)
    # if not kwargs.get('role').strip():
    #     print('role字段不能为空')

data_info = {'name':'王大锤', 'age':30, 'role':'演员'}

# func_7(k=1, m=2)
# func_7(k = data_info)  #注：func_7(data_info)
# func_7(**data_info)

