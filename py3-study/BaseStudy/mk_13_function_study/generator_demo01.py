

from typing import Iterable, Iterator, Generator

class FF:

    def __iter__(self):
        # return (i for i in range(10))
        return iter([1, 3])
ff = FF()
ff = iter(ff)
print(ff, isinstance(ff, Iterable), isinstance(ff, Iterator), isinstance(ff, Generator))
nums = range(10)
nums_new = iter(nums)
def func():
    yield 1
f = func()
print(nums_new, isinstance(nums_new, Iterable), isinstance(nums_new, Iterator), isinstance(nums_new, Generator))
print(f, isinstance(f, Iterable), isinstance(f, Iterator), isinstance(f, Generator))

# for n in nums_new:
#     print(n)

# print([i for i in nums_new])