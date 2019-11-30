



lst = ['德', '玛', '西', '亚']
index = 2
nums = 10

def func(lst, index, nums):

    lst_new = []
    for i in range(nums):
        # 修改索引值1
        if index >= len(lst):
            index = 0

        # 修改索引值2
        # index %= len(lst)

        lst_new.append(lst[index])
        index += 1

    return lst_new

# print(func(lst, index, nums))


def num_add(num):
    if num >= 10:
        return 11
    num += 1
    print(num)

    print(num_add(num))

    print(num)


# num_add(1)
