
from typing import Iterable, Iterator, Generator
from itertools import count


def check_type(obj):
    print(obj, isinstance(obj, Iterable), isinstance(obj, Iterator), isinstance(obj, Generator))

nums_all = count(0)
d = [1, 2]

"""
map()
"""
# 接收一个一个可迭代对象 返回一个迭代器对象
d_new = map(float, nums_all)

check_type(d_new)
check_type(nums_all)

"""
zip()
"""
zip_nums = zip([1, 2], [11, 22])
check_type(zip_nums)

"""
filter()
"""
filter_nums = filter(lambda x:x>1, d)
check_type(filter_nums)
print(list(filter_nums))