




def map_new_01(func, item):

    for i in item:
        yield func(i)

# print(list(map(lambda x: x * 2, range(100))))
#
# print(list(map_new_01(lambda x: x * 2, range(100))))


def map_new_02(func, *item):

    item = [iter(i) for i in item]
    while True:
        try:
            args = []
            for i in item:
              args.append(next(i))
            yield func(*args)
        except:
            break


# m = map(lambda x, y: x * y, range(10), (i for i in range(5)))
# for i in m:
#     print(i)
# print('#'*20)
# m_new = map_new_02(lambda x, y: x * y, range(10), range(5))
# for i in m_new:
#     print(i)