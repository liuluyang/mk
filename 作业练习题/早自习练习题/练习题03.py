


"""
第一题：
给出一个列表lst以及开始索引index和所需元素个数
从给定位置开始取元素，取到末尾之后，继续从头部开始取，直到取够指定个数，把取的元素放到新的列表lst_new
lst = ['李贺', '小白', '班长', '蔡子涵', '小黑']
index = 2
length = 10

lst_new = ['班长', '蔡子涵', '小黑', '李贺', '小白', '班长', '蔡子涵', '小黑', '李贺', '小白']
"""
lst = ['李贺', '小白', '班长', '蔡子涵', '小黑']
index = 2
length = 10

def func_01(lst, index, length):
    """
    第一题
    :param lst:
    :param index:
    :param length:
    :return:
    """
    lst_new = []
    lst_len = len(lst)
    for i in range(length):
        # 修改索引 方法一
        if index >= lst_len:
            index = 0
        # 修改索引 方法二
        # index %= lst_len

        lst_new.append(lst[index])
        index += 1

    return lst_new


"""
第二题：
食堂账本.txt 数据处理
1. 统计总收入
2. 统计每个菜品售卖的份数（忽略大小份）
3. 统计每个菜品售卖的份数和收入
"""

def func_02():

    with open('食堂账本.txt', 'r', encoding='utf8') as f:
        f.readline()

        data = {}
        all = 0
        for line in f:
            # 数据清洗
            line_new = line.split()
            name = line_new[0]
            price = int(line_new[-1])
            if '（' in name:
                name = name[:-3]

            # 2.统计份数
            if name in data:
                data[name] += 1
            else:
                data[name] = 1

            # 3.不同菜品分别统计份数、收入
            # if name in data:
            #     v = data[name]
            #     v[0] += 1
            #     v[-1] += price
            #     print(name, v)
            # else:
            #     data[name] = [1, price]

            # 1.计算收入总和
            all += price

            return all, data
