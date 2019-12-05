# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/3 11:44



print((11 or 2))

print(3 and 7 or 9 and 0)


import functools, itertools, math


open_new = functools.partial(open, encoding='utf8')

f = open_new('test.txt', 'r')
print(f.read())


def note(func):
    "note function"
    # @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    """
    test doc
    """

    print('this is a test func')

test()

print(test.__doc__, test.__name__, test.__class__)


import copy


lst = [1, 2, 3, ['a', 'b']]

a = copy.deepcopy(lst)

lst.append(1)
lst[3].append(1)
print(lst)
print(a)


func_lst = [lambda x:x*i for i in range(4)]

r = [f(2) for f in func_lst]
print(r)


print(math.log2(10))
print(math.floor(10.2))