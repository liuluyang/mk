# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/12 8:35


"""
第一题：
lst = ['李贺', '小白', '班长', '蔡子涵', '小黑']
index = 2
length = 10

lst_new = []
"""
lst = ['李贺', '小白', '班长', '蔡子涵', '小黑']
index = 2
length = 10

def func_01(lst, index, length):
    """

    :param lst:
    :param index:
    :param length:
    :return:
    """
    lst_new = []
    lst_len = len(lst)
    for i in range(length):
        # 修改索引01
        if index >= lst_len:
            index = 0

        # 修改索引02
        # index %= lst_len
        lst_new.append(lst[index])
        index += 1

    print(lst_new)

# func_01(lst, index, length)


"""
第二题：
食堂账本.txt 数据处理
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

            # 统计份数
            if name in data:
                data[name] += 1
            else:
                data[name] = 1

            # 统计份数、总和
            # if name in data:
            #     v = data[name]
            #     v[0] += 1
            #     v[-1] += price
            #     print(name, v)
            # else:
            #     data[name] = [1, price]

            # 计算总和
            all += price

            return all, data

# func_02()
