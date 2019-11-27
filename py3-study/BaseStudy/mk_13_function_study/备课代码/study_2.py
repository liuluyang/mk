

"""

变量作用域
"""

"""
如果对全局变量的整个对象进行操作,需用global事先声明
函数内部声明的变量只在函数内部调用，函数之外无法获取
"""

a = '我是全局变量'
data = [1, 2, 3]

def func_1():
    # global a
    a = '我是局部变量'
    # global data
    # del data
    # print(data)
    print(a)

# print(a)
# func_1()
# # print(a)
# print(data)


"""
嵌套函数
"""

def func_2():
    name = 'func_2()的变量'
    print(name)
    def func_child():
        # name = 'func_child()的变量'
        # nonlocal name
        # name += 'sad'
        print(name)

    func_child()

# func_2()

"""
匿名函数lamdba
短小精悍 临时调用
"""

sum_ = lambda x, y, z:x+y+z
# print(sum_(1, 3, 1))

pop_ = lambda x:x[-1]
# print(pop_([1,2,3]))

double_ = lambda x:x*2
# print(double_('**'))

"""
高阶函数
只需满足以下任意一个条件，即是高阶函数
    1.接受一个或多个函数作为输入
    2.return 返回另外一个函数
"""
# print(abs(-1), abs)
# f = abs
# print(f(-1))

def abc_add(num, num_2, func):

    return func(num) + func(num_2)

r = abc_add(-3, -1, abs)
# print(r)

"""
常用的高阶函数
zip() map()
"""