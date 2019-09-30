# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/20 14:16

import random

class Foo:
    """大傻蛋
    """

    def __init__(self):
        """

        """
        pass

    def __call__(self, *args, **kwargs):
        print(args, kwargs)

    def __contains__(self, item):

        print(item, '__contains__')

        if item == 'a':
            return True

        return False


# f = Foo()
# print(f.__doc__)            # 返回描述信息
# print(Foo.__doc__)
###########################
# print(random.__doc__)

# print(f.__module__)

# print(random.Random.__module__)

# print(f.__class__)
# print(Foo.__class__)
#
# print(type(f))
# print(type(Foo))
# print(type(type))


class DictNew(dict):


    def __hash__(self):


        return 111111111111111

    pass

if __name__ == '__main__':
    pass

    # f('xx', '22', gender='man')
    # print('aa' in f)
    # print(hash(f))

    # print(hash({}))

    # data = {}
    # d = DictNew([[1, 2], [3, 4]])
    # d2 = DictNew([[1, 2]])
    # # d2[3] = 4
    #
    # print(d, id(d))
    # print(d2, id(d2))
    #
    # data[d] = 'abc'
    # data[d2] = 'abc'
    #
    # d2[3] = 4
    #
    # print(data)
    # for k,v in data.items():
    #     print(id(k))