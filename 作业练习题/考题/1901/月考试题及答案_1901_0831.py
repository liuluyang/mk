

"""
月考
"""
"""
注：
所有考题必须在函数内作答
"""

"""
第一题：
返回一个列表
列表的元素有数字、字符串、列表、元祖、字典、集合六种数据
每种数据必须命名
"""
def func_01():
    """
    第一题
    :return:
    """
    n01 = 1
    n02 = 'hello'
    n03 = ['hello', 'world']
    n04 = ('hello', 'world')
    n05 = {'hello':'world'}
    n06 = {'hello', 'world'}
    n_list = [n01, n02, n03, n04, n05, n06]
    # for n in n_list:
    #     print(type(n))

    return n_list

# r = func_01()
# print(r)


"""
第二题：
s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
s_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
把字符串s处理成一个新的字符串s_new并返回
"""
def func_02():
    """
    第二题
    :return:
    """
    s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'

    s_new = s.replace(' | ', ',')

    return s_new

# r = func_02()
# print(r)


"""
第三题：
s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
data = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
把字符串s处理成一个字典data并返回
"""
def func_03():
    """
    第三题
    :return:
    """
    s = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'

    data = dict([d.split(':') for d in s.split(' | ')])

    return data

# r = func_03()
# print(r)


"""
第四题：
nums = [random.randrange(1, 101) for _ in range(10)]
计算出列表nums所有数的和、奇数的和、偶数的
把结果放进字典result并返回
注：不能用内置函数sum()
"""
def func_04():
    """
    第四题
    :return:
    """
    import random
    nums = [random.randrange(1, 101) for _ in range(10)]
    result = {'所有数和':0, '奇数和':0, '偶数和':0}

    for num in nums:
        if num % 2 == 0:
            result['偶数和'] += num
        else:
            result['奇数和'] += num
        result['所有数和'] += num

    return result

# r = func_04()
# print(r)


"""
第五题：
nums = [random.randrange(1, 101) for _ in range(10)]
找出列表nums最大数、最小数
把结果放进字典result并返回
注：不能用内置函数max()min()
"""
def func_05():
    """
    第五题
    :return:
    """
    import random
    nums = [random.randrange(1, 101) for _ in range(10)]
    result = {'最大数':0, '最小数':0}

    result['最小数'] = nums[0]
    for num in nums:
        if num > result['最大数']:
            result['最大数'] = num
        elif num < result['最小数']:
            result['最小数'] = num

    return result

# r = func_05()
# print(r)


"""
第六题：
nums_01 = [random.randrange(1, 101) for _ in range(10)]
nums_02 = [random.randrange(1, 101) for _ in range(10)]
找出两个列表里面都有的数字、和所有出现过的数字
把结果放进字典result并返回
"""
def func_06():
    """
    第六题
    :return:
    """
    import random
    nums_01 = [random.randrange(1, 101) for _ in range(10)]
    nums_02 = [random.randrange(1, 101) for _ in range(10)]
    result = {'都有的数字':None, '所有出现过的数字':None}

    nums_01_set, nums_02_set = set(nums_01), set(nums_02)
    result['都有的数字'] = nums_01_set & nums_02_set
    result['所有出现过的数字'] = nums_01_set | nums_02_set

    return result

# r = func_06()
# print(r)

"""
第七题：
工资信息
data = {'佩奇':15000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000, '白姑娘':10000}
按他们的工资大小进行排序，之后把他们的姓名放进列表并返回
"""
def func_07():
    """
    第七题
    :return:
    """
    data = {'佩奇': 15000, '老男孩': 6000, '海峰': 7000, '马JJ': 8000, '老村长': 9000, '黑姑娘': 10000, '白姑娘': 10000}
    data_list = list(data.items())
    name_list = [name[0] for name in sorted(data_list, key=lambda x:x[-1])]
    # print(data_list)
    # print(name_list)

    return name_list

# func_07()

"""
第八题：
把文件 我的作品.txt 的内容按顺序进行编号
之后打乱作品写入一个新的文件，类似于 我的作品_打乱.txt 的内容 
"""
def func_08():
    """
    第八题
    :return:
    """
    import random
    with open('我的作品.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()
        lines_new = [str(index)+'.'+line for index,line in enumerate(lines)]
        print(lines_new)
        random.shuffle(lines_new)
        with open('我的作品_new.txt', 'w', encoding='utf8') as f_new:
            f_new.writelines(lines_new)

# func_08()


"""
第九题：
写个函数
每次调用该函数返回一个符合要求的车牌号
车牌号要求：
五位数、必须同时包含数字和字母
"""
def func_09():
    """
    第九题
    :return:
    """
    import string, random
    params = string.ascii_uppercase + string.digits
    while True:
        card = ''
        for _ in range(5):
            card += random.choice(params)
        if not card.isdigit() and not card.isalpha():
            return card

# card = func_09()
# print(card)

"""
第十题：
用循环打印下面的图形：大小不必一样
              *               
             * *              
            *****             
           *     *            
          *********           
         *         *          
        *************         
       *             *        
      *****************       
     *                 *      
      *****************       
       *             *        
        *************         
         *         *          
          *********           
           *     *            
            *****             
             * *              
              *
"""
def func_10():
    """
    第十题
    :return:
    """
    num = 20
    nums = list(range(1, num, 2)) + list(range(1, num-2, 2))[::-1]
    for index, n in enumerate(nums):
        s = '*'*n
        if index % 2 == 1:
            s = '*' + ' '*(n-2) + '*'
        print(s.center(num*2))

# func_10()

"""
第十一题：
这里有一个 食堂账本.txt
统计一下总收入、最受欢迎的菜品
注：
1.最受欢迎菜品可能不止一种
2.有的菜品有大小份，但是算作一种菜品，也就是忽略大小份
"""
def func_11():
    """
    第十一题
    :return:
    """
    result = {'总收入':0, '最受欢迎的菜品':[]}
    data_dict = {}
    favorite = []
    max_num = 0
    with open('食堂账本.txt', 'r', encoding='utf8') as f:
        for index, line in enumerate(f):
            if index == 0:
                continue

            # 数据处理
            d = line.split()
            name = d[0] if '（' not in d[0] else d[0][:-3]
            price = int(d[-1])
            result['总收入'] += price

            # 统计各菜品售卖数量
            if name in data_dict:
                data_dict[name] += 1
            else:
                data_dict[name] = 1

            # 统计售卖最多的菜品
            sell_nums = data_dict[name]
            if sell_nums > max_num:
                max_num = sell_nums
                favorite = [name]
            elif sell_nums == max_num:
                favorite.append(name)

        result['最受欢迎的菜品'] = favorite
        print(data_dict, sum(data_dict.values()))
    return result

# f = func_11()
# print(f)

"""
第十二题：
写一个递归函数打印出1->10-10->1的数
"""
def func_12(num=0):
    """
    第十二题
    :return:
    """
    if num >= 10:
        return
    num += 1
    print(num)
    func_12(num)
    print(num)

# func_12()


"""
第十三题：
写一个计算函数运行时间的装饰器
"""
def func_13(func):
    """
    第十三题
    :return:
    """
    import time
    def inner(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        end = time.time() - start
        print('%s 运行用时%s'%(func.__name__, end))

        return f

    return inner

"""
第十四题：
写一个可以产生一百万个数字的生成器
"""
@func_13
def func_14(num=1000000):
    """
    第十四题
    :return:
    """
    n = 0
    while True:
        yield n
        n += 1
        if n >= num:
            break

from typing import Generator
# f = func_14()
# print(isinstance(f, Generator))

"""
第十五题：
统计一下自己项目里面有多少python文件,以及总共有多少行代码
"""
import os
def func_15(path):
    """
    第十五题
    :return:
    """
    py_dict = {'file_nums':0, 'line_nums':0}
    def find_file(path):
        dir_list = os.listdir(path)
        for d in dir_list:
            path_new = os.path.join(path, d)
            if os.path.isdir(path_new):
                find_file(path_new)
            else:
                file_name = os.path.split(path_new)[-1]
                if file_name.split('.')[-1] == 'py' and path_new.replace('\\', '/') != __file__:
                    try:
                        with open(path_new, 'r', encoding='utf8') as f:
                            lines_num = len(f.readlines())
                            py_dict[path_new] = lines_num
                            py_dict['file_nums'] += 1
                            py_dict['line_nums'] += lines_num
                    except:
                        print('编码不是utf8', path_new)

    find_file(path)
    print(py_dict)
    print(__file__)

# func_15(r'E:\liuluyang\课件代码\py3-study')

if __name__ == '__main__':
    # func_03()
    pass