

# print('hello')


def hello():

    print('hello111111111')


def func():
    import string
    res = '0123456789'+string.ascii_uppercase
    count = 0
    for x in res:
        for y in res:
            for z in res:
                for f in res:
                    for i in res:
                        count += 1
                        yield x, y, z, f, i, count

if __name__ == '__main__':

    f = func()
    for i in f:
        print(i)
    pass