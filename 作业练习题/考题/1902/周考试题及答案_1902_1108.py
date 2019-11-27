

"""
周考
"""
"""
注：
每个题单独定义一个函数
如果标明需要返回值的，必须要有返回值
"""


"""
第一题：
lst = [1, 2, 'abc', [], (), {}, 'cba', 3]
计算列表lst里面有多少种数据类型（列表最多含六种数据类型）
"""
def func_01():

    lst = [1, 2, 'abc', [], (), {}, 'cba', 3]

    return len({type(obj) for obj in lst})
# print(func_01())


"""
第二题：
s = '   李银河  你好哇  '
s_new = '李银河  你好哇'
把字符串s处理成一个新的字符串s_new并返回
注：不能用strip()方法
"""
def func_02(res):

    index_ =  0
    for i in range(len(res)):
        if res[i] == ' ':
            index_ += 1
        else:
            break
    res_02 = res[index_:]

    index_ = -1
    for i in range(len(res_02)):
        if res_02[index_] == ' ':
            index_ -= 1
        else:
            break
    if index_ != -1:
        res_02 = res_02[:index_+1]

    return res_02
# print(func_02('   李银河  你好哇  '))


"""
第三题：
lst = [['老王', 1], ['去', '上班!'], 2, [3, 4], 'abc']
求列表里面所有数字的和
"""
def func_03():

    lst = [['老王', 1], ['去', '上班!'], 2, [3, 4], 'abc']
    count = 0
    for obj in lst:
        if isinstance(obj, int):
            count += obj
        elif isinstance(obj, list):
            for i in obj:
                if isinstance(i, int):
                    count += i

    return count
# print(func_03())


"""
第四题：
用循环打印出下面的空心菱形：大小不必完全一样
                   *
                  * *
                 *   *
                *     *
               *       *
              *         *
             *           *
            *             *
           *               *
          *                 *
           *               *
            *             *
             *           *
              *         *
               *       *
                *     *
                 *   *
                  * *
                   *
"""
def func_04(num=10):

    nums = list(range(1, num, 2))
    nums = nums + nums[:-1][::-1]
    for i in nums:
        if i == 1:
            s = '*'
        else:
            s = '*'+ ' '*(i - 2)+ '*'
        print(s.center(40))
# func_04()


"""
第五题：
工资信息
data = {'佩奇':15000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000}
把data数据处理成lst并返回
lst = [['佩奇', 15000], ['黑姑娘', 10000], ['老村长', 9000], ['马JJ', 8000], ['海峰', 7000], ['老男孩', 6000]]
"""
def func_05():

    data = {'佩奇': 15000, '老男孩': 6000, '海峰': 7000, '马JJ': 8000, '老村长': 9000,
            '黑姑娘': 10000}
    r = sorted(list(data.items()), key=lambda x:x[-1], reverse=True)

    return [list(i) for i in r]
# print(func_05())


"""
第六题：
['佩奇', '老男孩', '海峰', '马JJ', '老村长', '黑姑娘', '白姑娘']
找出名字最长的，如果有多个全部找出来
"""
def func_06():

    names = ['佩奇', '老男孩', '海峰', '马JJ', '老村长', '黑姑娘', '白姑娘']

    num = max([len(i) for i in names])

    return [name for name in names if len(name) == num]
# print(func_06())


def func_06_02():

    names = ['佩奇', '老男孩', '于海峰', '马JJ', '老村长', '黑姑娘', '白姑娘']

    names_filter = []
    max_num = 0
    for name in names:
        name_len = len(name)
        if name_len > max_num:
            max_num = name_len
            names_filter = [name]
        elif name_len == max_num:
            names_filter.append(name)

    return names_filter
# print(func_06_02())


#
"""
第七题：
读取user_info.txt的信息
当输入某个人的姓名时，打印出这个人的电话号码
或者输入某个人的手机号码，打印出这个人的姓名
注：当查找的信息不存时程序不能出错，可以返回提示信息
"""
def func_07():

    with open('user_info.txt', 'r', encoding='utf8') as f:
        f.readline()
        info_dict = {}
        for line in f:
            line_lst = line.split()
            info_dict[line_lst[0]] = line_lst[-1]
            info_dict[line_lst[-1]] = line_lst[0]
        # print(info_dict)

        while True:
            name = input('请输入要查询的内容：')
            if name == 'q':
                break
            print(info_dict.get(name, '未找到！'))
# func_07()


#
"""
第八题：
把我的作品.txt 按行数编号，打乱之后写入一个新的文件
"""
def func_08():

    import random
    with open('我的作品.txt', 'r', encoding='utf8') as f:
        lines = ['%s.%s'%(index, line) for index, line in enumerate(f)]
        random.shuffle(lines)
    with open('我的作品_new.txt', 'w', encoding='utf8') as f:
        f.writelines(lines)
# func_08()


#
"""
第九题：
这里有一个 食堂账本.txt
统计一下各个菜品的售卖情况
注：有的菜品有大小份，但是算作一种菜品，也就是忽略大小份
"""
def func_09():

    with open('食堂账本.txt', 'r', encoding='utf8') as f:
        f.readline()
        data = {}
        count = 0
        for line in f:
            lst = line.replace('（大）', '').replace('（小）', '').split()
            name, price = lst[0], int(lst[-1])
            # print(name, price)

            if name in data:
                data[name] += price
            else:
                data[name] = price

            count += price

        return data, count
# print(func_09())


"""
第十题：
写个递归函数 求1-10的阶乘
1*2*3...10
"""
def func_10(num):

    if num >= 10:
        return 10

    return num * func_10(num + 1)
# print(func_10(1))


"""
第十一题：
写个装饰器函数
"""
def func_11(func):

    def inner(*args, **kwargs):

        f = func(*args, **kwargs)
        return f

    return inner


"""
第十二题：
写一个生成器模仿enumerate函数的功能
"""
def func_12(item, n=0):

    for i in item:
        yield (n, i)
        n += 1