




def add_test(num):

    print(num)

    add(num + 1)


# add_test(1)


import sys

sys.setrecursionlimit(2000)

def add(num):

    if num >= 1198:
        return num

    return num + add(num + 1)

# print(add(1))

"""
add(1) => 
return 1 + add(2) =>
return 1 + 2 + add(3) =>
return 1 + 2 + 3 + add(4) =>
return 1 + 2 + 3 + 4 + add(5) =>
add(5) = return 5


"""

import time

def func_04(num):

    print(num)
    return num

def func_03(num):

    print(num)
    func_04(num + 1)

def func_02(num):

    print(num)
    func_03(num + 1)

def func_01(num):

    print(num)
    func_02(num + 1)
    print(1111)


# func_01(1)











