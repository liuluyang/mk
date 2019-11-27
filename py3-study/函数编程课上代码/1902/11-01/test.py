



"""


"""


def test(num):

    if num == 2:
        return 2

    if num == 1:
        return 1
    elif num == 0:
        return 0

    return test(num - 1) + test(num - 2)


print(test(3))