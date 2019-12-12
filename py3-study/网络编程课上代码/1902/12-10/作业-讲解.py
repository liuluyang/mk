# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/10 9:33



from itertools import cycle, combinations, permutations, product, groupby

c = cycle('abc')

# print(c)
#
# for i in c:
#     print(i)


class CycleNew:


    def __init__(self, iterable):

        self.iterable = iterable
        self.iterator = iter(self.iterable)

    def __iter__(self):

        return self

    def __next__(self):

        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.iterable)
            return next(self.iterator)

c2 = CycleNew('abc')

# for i in c2:
#     print(i)
# print(next(c2))
# print(next(c2))
# print(next(c2))
# print(next(c2))


r = combinations('abc', 3)
for i in r:
    print(i)
print('#'*15)
p = permutations('abc', 3)
for i in p:
    print(i)
print('#' * 15)
p2 = product('abc', 'xyz', '123')
for i in p2:
    print(i)
print('#' * 15)
g = groupby('aadjkadjasdas')
for i, item in g:
    print(i, item, list(item))
