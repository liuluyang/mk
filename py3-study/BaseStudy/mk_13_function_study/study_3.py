


"""

递归函数（如果一个函数在内部调用自已本身，这个函数就叫做递归函数）
 1.必须有一个明确的结束条件

 2.每次进入更深一层递归时，问题规模相比上次递归都应有所减少

 3.递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）
 这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，
 栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）
"""

num = 100
# while True:
#     print(num)
#     if num < 1:
#         break
#     num //= 2
depth = 0
def func_1(num):
    print(num)
    if num < 1:
        # print('return', num)
        return
    # global depth
    # depth += 1
    # print('depth', depth)
    func_1(num//2)
    # print(num)

# func_1(100)

# 阶乘
num = 5
result = 1
for i in range(1, num+1):
    result *= i
# print(result)

def func_2(num):
    if num < 1:
        return 1
    return num * func_2(num-1)

r = func_2(num)
print(r)

"""
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
"""

"""
内置函数
https://www.runoob.com/python3/python3-built-in-functions.html
"""
import builtins
builtins_list = dir(builtins)
print(len(builtins_list), builtins_list)


"""
命名空间:
python里面有很多名字空间，每个地方都有自己的名字空间，互不干扰，
不同空间中的两个相同名字的变量之间没有任何联系。
作用域查找顺序:
locals -> enclosing function -> globals ->builtins
"""
print(globals())
print(locals())

def test_(n):
    m = n + 1
    for i in range(2):
        print(i)
    print(locals())
    print(globals())
    for i in locals().items():
        print(i)

test_(2)

if __name__ == '__main__':
    data  = globals()
    # for k, v in list(data.items()):
    #     print(k, '#'*10,v)