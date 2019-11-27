

"""
周考
"""
"""
所有考题必须在函数内作答
"""

"""
第一题：
给一段字符串，里面是一些连续重复的字符，统计他们每个字符出现的次数，
把统计结果以字符串的形式返回，返回的字符顺序必须跟源字符串里面的字符一致。
res = 'xxzzaaabbcdddeuuuuuut'
res_count = 'x2z2a3b2c1d3e1u6t1'
"""
def func_01():

    res = 'xxzzaaabbcdddeuuuuuut'
    res_count = ''
    dic = {}
    for s in res:
        if s in dic:
            dic[s] += 1
        else:
            if dic:
                tup = dic.popitem()
                res_count += tup[0] +str(tup[-1])
            dic[s] = 1
    tup = dic.popitem()
    res_count += tup[0] + str(tup[-1])

    return res_count
# print(func_01())


"""
第二题：
说一下 可迭代对象、迭代器对象、生成器函数、生成器对象分别是什么以及他们之间的区别：
"""

"""
第三题：
1.如何判断一个对象是否是迭代器对象
2.哪几个内置函数返回的结果是迭代器对象，至少写两个，并解释他们的作用
"""

"""
第四题：
列举学过的几个模块，至少写五个，并解释他们的用处
"""

"""
第五题：
写一个函数，该函数接收一个参数nums，根据nums来控制打印的列表的数量
找规律打印相应的列表
n01 = [1]
n02 = [1, 1]
n03 = [1, 2, 1]
n04 = [1, 3, 3, 1]
n05 = [1, 4, 6, 4, 1]
n06 = [1, 5, 10, 10, 5, 1]
"""
def make_lst(lst):

    lst_new = []
    for index in range(len(lst)-1):
        lst_new.append(lst[index] + lst[index+1])

    return [1] + lst_new + [1]
# print(make_lst([1,2,1]))

def func_05(nums=6):

    lst = [1]
    print(lst)

    for i in range(nums-1):
        lst_next = make_lst(lst)
        print(lst_next)
        lst = lst_next
# func_05(6)


"""
第六题：
找出列表里面只出现了一次的那个数
nums = [1, 2, 2, 3, 4, 4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 1, 2, 2, 3,
        4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 5, 2, 2, 2, 3, 4, 4, 3, 2,
        ]
注：不能用count()方法
"""
def func_06():

    nums = [1, 2, 2, 3, 4, 4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 1, 2, 2, 3,
            4, 3, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 4, 3, 5, 2, 2, 2, 3, 4, 4, 3, 2,
            ]
    set_01 = set()
    set_02 = set()
    for num in nums:
        if num in set_01:
            set_02.add(num)
        else:
            set_01.add(num)

    return set_01 - set_02
# print(func_06())


"""
第七题：
找出英文句子里面出现频率最高的单词
res = "Bob hit a ball, the hit BALL flew far after it was hit."
注：忽略大小写
"""
def func_07():

    import re
    res = "Bob hit a ball, the hit BALL flew far after it was hit."
    words_list = re.findall('[a-zA-Z]+', res)

    dic = {}
    word = None
    max_num = 0
    for w in words_list:
        w = w.lower()
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1
        num = dic[w]
        if num > max_num:
            max_num = num
            word = w

    return word
# print(func_07())


"""
第八题：
写个程序计算五天之后的日期时间，格式是字符串
"""
def func_08():

    import time
    after_five_day = time.time() + 86400*5

    time_str = time.strftime('%Y-%m-%d %X', time.localtime(after_five_day))

    return time_str
# print(func_08())


"""
第九题：
写个程序统计当前文件所在目录下，每个python文件的代码行数
数据返回格式：{'test01':20, 'test02':100}
注：空行不算
"""
def count_code(filepath):

    with open(filepath, 'rb') as f:
        count = 0
        for line in f:
            line = line.strip()
            if line:
                count += 1

        return count
# print(count_code('test.py'))

def func_09():

    import os
    file_data = {}
    file_list = os.listdir('.')

    for file_name in file_list:
        if file_name.endswith('.py'):
            file_data[file_name] = count_code(file_name)

    return file_data
# print(func_09())


"""
第十题：
下面的字符串是由一个两位长度的字符串md5加密的结果，
找出这个字符串并返回
提示：该字符串只包含小写字母
res = '25ed1bcb423b0b7200f485fc5ff71c8e'
"""
def func_10():

    import hashlib
    from string import ascii_lowercase

    res = '25ed1bcb423b0b7200f485fc5ff71c8e'
    for x in ascii_lowercase:
        for y in ascii_lowercase:
            s = x + y
            if hashlib.md5(s.encode()).hexdigest() == res:
                return s
# print(func_10())


"""
第十一题：
用循环打印下面的图形：大小不必完全一样
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


def func_11(num=20):
    nums01 = list(range(1, num, 2))
    nums02 = nums01[:-1][::-1]

    for index, n in enumerate(nums01 + nums02):
        if index % 2 == 0:
            s = '*' * n
        else:
            s = '*' + ' ' * (n - 2) + '*'
        print(s.center(num + 1))
# func_11()


"""
第十二题：
写个函数把一个整数字符串转成整数
列如：'123' => 123, '230' => 230
注：不能用int(),eval()
"""
def func_12(res):

    change_dict = {str(num):num for num in range(10)}
    res = res[::-1]
    num = 0
    for index, s in enumerate(res):
        num += change_dict[s]*10**index

    return num
# print(func_12('1230'))





