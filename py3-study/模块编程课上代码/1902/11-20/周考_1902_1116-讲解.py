

"""
周考
"""
"""
所有考题必须在函数内作答
"""
import time
import re
import os
import hashlib

def decorate(func):

    def inner(*args, **kwargs):

        t = time.time()
        f = func(*args, **kwargs)
        print('%s函数运行时间：%s'%(func.__name__, time.time() - t))

        return f

    return inner

"""
第一题：
给一段字符串，里面是一些连续重复的字符，统计他们每个字符出现的次数，
把统计结果以字符串的形式返回，返回的字符顺序必须跟源字符串里面的字符一致。
res = 'xxzzaaabbcdddeuuuuuut'
res_count = 'x2z2a3b2c1d3e1u6t1'
"""
# res = 'xxzzaaabbcdddeuuuuuut'
res = ''
for i in 'abcdefghijklmn':
    res += i*10000

@decorate
def func_01(res):

    dic = {}
    # 统计字符个数
    # for i in res:           # n**2
    #     dic[i] = res.count(i)

    # for i in res:            # n * 2
    #     if i in dic:
    #         dic[i] += 1
    #     else:
    #         dic[i] = 1

    for i in res:              # n * 2
        dic[i] = dic.get(i, 0) + 1

    r = ''
    for k, v in dic.items():   # m
        r += k + str(v)

    return r
# print(func_01(res))

@decorate
def func_01_02(res):

    r = ''
    dic = {}
    string_before = ''
    for i in res:            # n * 2
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            # 当出现一个新字符的时候 把上一次字符的信息累加
            r += string_before + str(dic.get(string_before, ''))
            # 替换新的字符
            string_before = i
    r += string_before + str(dic.get(string_before, ''))

    return r
# print(func_01_02(res))

@decorate
def func_01_03(res):

    r = ''
    string_befor = ''
    string_num = 0
    for i in res:
        if i == string_befor:
            string_num += 1
        else:
            if string_befor != '':
                # 当出现一个新字符的时候 把上一次字符的信息累加
                r += string_befor + str(string_num)
            # 替换新的字符
            string_befor = i
            string_num = 1
    r += string_befor + str(string_num)

    return r
# print(func_01_03(res))


"""
第二题：
说一下 可迭代对象、迭代器对象、生成器函数、生成器对象分别是什么以及他们之间的区别：
"""


"""
第三题：
1.如何判断一个对象是否是迭代器对象
2.哪几个内置函数返回的结果是迭代器对象，至少写两个，并解释他们的作用
"""
# from typing import Iterable, Iterator
# isinstance('a', Iterator)


"""
第四题：
列举学过的几个模块，至少写五个，并解释他们的用处
"""


"""
第五题：
杨辉三角

写一个函数，该函数接收一个参数nums，根据nums来控制打印的列表的数量
找规律打印相应的列表
n01 = [1]
n02 = [1, 1]
n03 = [1, 2, 1]
n04 = [1, 3, 3, 1]
n05 = [1, 4, 6, 4, 1]
n06 = [1, 5, 10, 10, 5, 1]
"""
def make_list(lst):

    lst_new = []

    for index in range(len(lst) - 1):
        lst_new.append(lst[index]+lst[index+1])

    lst_new = [1] + lst_new + [1]

    return lst_new
# print(make_list([1, 2, 1]))

def func_05(nums):

    # r = []
    start_list = [1]
    if nums >= 1:
        # print(start_list)
        # r.append(start_list)
        yield start_list

    for i in range(nums - 1):
        lst_new = make_list(start_list)
        # print(lst_new)
        # r.append(lst_new)
        yield lst_new
        start_list = lst_new

# r = func_05(300)
# print(r)


"""
第六题：
找出列表里面只出现了一次的那个数
nums = [1, 2, 2, 3, 4, 4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 1, 2, 2, 3,
        4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 5, 2, 2, 2, 3, 4, 4, 3, 2,
        ]
注：不能用count()方法
"""
nums = [1, 2, 2, 3, 4, 4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 1, 2, 2, 3,
            4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 2, 2, 2, 3, 4, 4, 3, 2,
            ] * 10000 + [5]

@decorate
def func_06(nums):

    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    for k, v in dic.items():
        if v == 1:
            return k
# print(func_06(nums))

@decorate
def func_06_02(nums):

    set_01 = set()  # 所有数字
    set_02 = set()  # 出现次数大于一次的数字

    for num in nums:
        if num in set_01: # 出现次数大于一次的数字
            set_02.add(num)
        else:
            set_01.add(num)

    return set_01 - set_02
# print(func_06_02(nums))


"""
第七题：
找出英文句子里面出现频率最高的单词
res = "Bob hit a ball, the hit BALL flew far after it was hit."
注：忽略大小写
"""
res = "Bob hit a ball, the hit BALL flew far after it was hit"*1000

@decorate
def testing7(res):
    res ="  ".join(re.split("[,.!]",res)).split()
    print(res)
    li = [i.lower() for i in res]
    dic = {i : li.count(i) for i in li}
    num = max([dic[i] for i in dic])
    for i in dic:
        if dic[i] == num:
            return i

# print(testing7(res))

@decorate
def find_word_01(res):

    word_list_re = re.findall('[a-zA-Z]+', res)
    return word_list_re
# print(find_word_01(res))

@decorate
def find_word_02(res):

    word_list = []
    string_now = ''
    for s in res:
        if s.isalpha():
            string_now += s
        else:
            if string_now:
                word_list.append(string_now)
            string_now = ''

    return word_list
# print(find_word_02(res))

@decorate
def func_07(res):

    # 找出所有单词
    word_list_re = re.findall('[a-zA-Z]+', res)

    dic = {}
    max_str = None
    max_num = 0
    for string_now in word_list_re:
        string_now = string_now.lower()

        # 统计单词频率
        if string_now in dic:
            dic[string_now] += 1
        else:
            dic[string_now] = 1
        # 找高频单词
        num = dic[string_now]
        if num > max_num:
            max_num = num
            max_str = string_now

    return max_str
# print(func_07(res))

@decorate
def func_07_02(res):

    res += ' '

    string_now = ''
    dic = {}
    max_str = None
    max_num = 0
    for s in res:
        if s.isalpha():
            string_now += s
        else:
            string_now = string_now.lower()
            if string_now:

                # 统计单词频率
                if string_now in dic:
                    dic[string_now] += 1
                else:
                    dic[string_now] = 1
                # 找高频单词
                num = dic[string_now]
                if num > max_num:
                    max_num = num
                    max_str = string_now

            string_now = ''

    return max_str
# print(func_07_02(res))


"""
第八题：
写个程序计算五天之后的日期时间，格式是字符串
"""
def func_08():

    timestamp_five = time.time() + 86400*5
    return time.strftime('%Y-%m-%d %X', time.localtime(timestamp_five))

# func_08()


"""
第九题：
写个程序统计当前文件所在目录下，每个python文件的代码行数
数据返回格式：{'test01':20, 'test02':100}
注：空行不算
"""
def count_code(filepath):

    with open(filepath, 'rb') as f:
        num = 0
        for line in f:
            line = line.strip()
            if line:
                num += 1
        return num
# print(count_code(r'E:\project\education\11-20\t.py'))

def func_09():

    file_names = os.listdir('.')
    dic = {}
    for filename in file_names:
        if filename.endswith('.py'):
            dic[filename] = count_code(filename)

    return dic
# print(func_09())


"""
第十题：
下面的字符串是由一个两位长度的字符串加密的结果，
找出这个字符串并返回
提示：该字符串只包含小写字母
res = '25ed1bcb423b0b7200f485fc5ff71c8e'
"""
def func_10():

    from string import ascii_lowercase
    dic = {}
    for x in ascii_lowercase:
        for y in ascii_lowercase:
            s = x + y
            md5_ = hashlib.md5(s.encode()).hexdigest()
            if  md5_ == '25ed1bcb423b0b7200f485fc5ff71c8e':
                return s
            dic[md5_] = s
# print(func_10())


"""
第十一题：
用循环打印下面的图形：大小不必完全一样
              *         0              
             * *        1         
            *****       2          
           *     *      3       
          *********     4       
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
def func_sx(num):

    nums = list(range(1, num, 2))
    nums_02 = nums[::-1][1:]
    for i in nums + nums_02:
        s = '*'*i
        print(s.center(num))

# func_sx(10)

def func_kx(num):

    nums = list(range(1, num, 2))
    nums_02 = nums[::-1][1:]
    for i in nums + nums_02:
        s = '*' * i
        if i > 1:
            s = '*' + ' ' * (i - 2) + '*'
        print(s.center(num))

# func_kx(10)

def func_11(num):

    nums = list(range(1, num, 2))
    nums_02 = nums[::-1][1:]
    for index, i in enumerate(nums + nums_02):
        if index % 2 == 0:
            s = '*' * i
        else:
            s = '*' + ' ' * (i - 2) + '*'
        print(s.center(num))

# func_11(10)


"""
第十二题：
写个函数把一个整数字符串转成整数
列如：'123' => 123, '230' => 230
注：不能用int(),eval()
"""
"""
'123' =>

1 * 10**2 + 2 * 10**1 + 3 * 10**0

"""

def func_12(strnum, base=10):

    dic = {str(i):i for i in range(10)}
    dic_other = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    # print(dict(zip('abcdef', range(10, 16))))
    dic.update(dic_other)
    print(dic)

    r = 0
    for index, num in enumerate(strnum[::-1]):
        r += dic[num] * base**index

    return r


# r = func_12('11111111f', base=16)
# print(type(r), r)
# print(int('11111111f', base=16))
# print(1 * 10**2 + 2 * 10**1 + 3 * 10**0)
