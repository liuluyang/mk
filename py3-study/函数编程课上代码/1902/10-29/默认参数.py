

############################################ 默认参数
# 默认参数必须在顺序参数之后

def register(name, age, country='中国', nation='汉族'):

    print(name)
    print(age)
    print(country)
    print(nation)


# register('老王', 40, nation='汉族')

############################################## *args/**kwargs
# *args接收多个顺序参数
# args的类型是元组
def add(*args):

    print(args)
    print(sum(args))


# add(1, 2)


# **kwargs接收多个关键字参数
# kwargs的类型是字典
def register_new(**kwargs):

    print(kwargs)


# register_new(name='xiaobai', age=20, nation='han')


def func01(*args, **kwargs):

    print(args)
    print(kwargs)

# func01(1, 2, 3, 4,10,  nation='han', last_num=4, name='xiaobai', age=20)

############################################# 参数综合应用

# 除了num 其他顺序参数被args接收
def func02(num, *args, **kwargs):

    print(num)
    print(args)
    print(kwargs)


# func02(1, 2, 3, name='xiaobai')


def func03(num, *args):

    print(num)
    print(args)


# func03(1, 40)


def func04(num, **kwargs):

    print(num)
    print(kwargs)


# func04(1, name='')


def func05(num=1, **kwargs):

    print(num)
    print(kwargs)

# func05(name='laowang', num=10)


############################################# print函数的参数

# f = open('test', 'w', encoding='utf8')
# print('哈喽', '老王', sep='-', file=f)
# print('哈喽', '老王')
