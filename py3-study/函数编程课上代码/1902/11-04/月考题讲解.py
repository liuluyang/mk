


"""
月考
"""
"""
注：
每个题单独定义一个函数
如果标明需要返回值的，必须要有返回值
"""


"""
第一题：
返回一个列表
列表包含数字、字符串、列表、元祖、字典、集合六种数据
"""
def func01():

    lst = [1, 'abc', [1, 2, 3], (1,), {1:2, 3:4}, {1, 'a', (1, 2)}]

    return lst

# print(func01())


"""
第二题：
s = 'k1:v1|| k2:v2|||k3:v3| |k4:v4'
s_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
把字符串s处理成一个新的字符串s_new并返回
"""
def func02():

    s = 'k1:v1|| k2:v2|||k3:v3| |k4:v4'

    result = s.replace('|', ' ').split()
    result = ','.join(result)
    # print(dict([d.split(':') for d in result])) # 扩展
    print(result)

    return result

# func02()

"""
第三题：
lst = [1, 2, 3, 'a', 4, 'b', 5]
计算列表lst里面所有数字的和
并返回计算结果
"""
def func03():

    lst = [1, 2, 3, 'a', 4, 'b', 5]
    count = 0
    for per in lst:
        if isinstance(per, int):
            count += per
            count = count+per

    # print(count)
    return count

# func03()


"""
第四题：
lst = [['老王', '开车'], ['去', '上班!']]
text = '老王开车去上班!'
把列表lst转换成字符串text并返回
"""
def func04():

    lst = [['老王', '开车'], ['去', '上班!']]
    result = ''
    for per in lst:
        s = ''.join(per)
        result += s

    return result

# func04()
"""
扩展
"""
lst = [
    [   'a',
        ['老王', ['111', ['222', ['333', ['444']]]]], ['开车']
    ],
    [
        ['去'], ['上班!']
    ]

    ]

# r = ''
# for f in lst:
#     print(f)
#     for ff in f:
#         if isinstance(ff, str):
#             r += ff
#         elif isinstance(ff, list):
#             for i in ff:
#                 r += i
#
# print(r)

r = []
def func_res(lst):

    for per in lst:
        if isinstance(per, str):
            r.append(per)
        else:
            func_res(per)
# func_res(lst)
# print(r)


"""
第五题：
用循环打印出下面的菱形：大小不必完全一样
                   *                    
                  ***                   
                 *****                  
                *******                 
               *********                
              ***********               
             *************              
            ***************             
           *****************            
          *******************             
           *****************            
            ***************             
             *************              
              ***********               
               *********                
                *******                 
                 *****                  
                  ***                   
                   *   
"""
def func05(num):


    nums_01 = list(range(1, num, 2))
    nums_02 = nums_01[::-1][1:]
    # print(nums_01, nums_02)

    for i in nums_01 + nums_02:
        print(('*'*i).center(num))

# func05(10)

"""
第六题：
找出工资最高的人，并返回他的名字
data = {'佩奇':5000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000}
"""
def func06():

    data = {'佩奇': 5000, '老男孩': 6000, '海峰': 7000, '马JJ': 8000, '老村长': 9000,
            '黑姑娘': 10000}

    name = None
    max_salary = 0
    for k, v in data.items():
        if v > max_salary:
            max_salary = v
            name = k

    return name, max_salary

# print(func06())

#
"""
第七题：
读取user_info.txt的信息
当输入某个人的姓名时，打印出这个人的电话号码
注：当输入的人名不存时程序不能出错，可以返回提示信息
"""
def func07():

    with open('file/user_info.txt', 'r', encoding='utf8') as f:
        f.readline()
        data = {}
        for line in f:
            line_lst = line.split()
            data[line_lst[0]] = line_lst[-1]
        # print(data)

        while True:
            name = input('请输入要查找的名字：')
            if name == 'q':
                break

            print(data.get(name, '未找到！'))


# func07()

#
"""
第八题：
工资单.txt 里面姓名是三个字的,他们工资的总和是多少，返回工资总和
"""
def func08():

    with open('file/工资单.txt', 'r', encoding='utf8') as f:
        f.readline()
        count = 0
        for line in f:
            line_lst = line.split()
            if len(line_lst[0]) == 3:
                count += int(line_lst[-1])

        return count

# print(func08())
# res = 'a       bccc'
# print(res.split())

#
"""
第九题：
我的作品_打乱.txt 里面是被打乱的作品
需要最后整理成 我的作品_整理.txt 的样子
"""
def func09():

    with open('file/我的作品_打乱.txt', 'r', encoding='utf8') as f:
        # 方法一
        data = {}
        for line in f:
            line_lst = line.split('.')
            data[line_lst[0]] = line

        print(data)
        with open('file/我的作品_new.txt', 'w', encoding='utf8') as f_new:
            for i in range(len(data)):
                f_new.write(data[str(i)])

        # 方法二
        # lst = f.readlines()
        # lst.sort()
        # with open('file/我的作品_new.txt', 'w', encoding='utf8') as f_new:
        #     for line in lst:
        #         f_new.write(line)
        #     # f_new.writelines(lst)
    pass

# func09()

#
"""
第十题：
从车牌号.txt 文件里面找出所有符合要求的车牌号，
判断一下符合规范的车牌里面，号码是否全部都不一样
如果全部不一样返回True
否则返回False
"""
def func10(filename='车牌号.txt'):

    with open('file/%s'%filename, 'r', encoding='utf8') as f:

        cards = f.read().split()
        cards_new = []
        for card in cards:
            if not card.isdigit() and not card.isalpha():
                cards_new.append(card)

        return len(set(cards_new)) == len(cards_new)

# func10()

"""
第十一题：
写个函数
每次调用该函数返回一个符合要求的车牌号
车牌号要求：
五位数、必须同时包含数字和大写字母
"""

def func11():

    import random
    import string
    import time

    # params = string.ascii_uppercase + string.digits
    params = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


    while True:
        card = ''
        for i in range(5):
            card += random.choice(params)

        # if not card.isdigit() and not card.isalpha():
        #     return card

        if card.isdigit():
            pass
        elif card.isalpha():
            pass
        else:
            return card

        # time.sleep(2)

# print(func11())



"""
第十二题：
把一百个不同的符合要求的车牌号写入文件
要求：每行十个，每个车牌号之间用空格隔开
"""

def func12():

    with open('file/cards.txt', 'w', encoding='utf8') as f:

        cards_set = set()
        while True:
            cards_set.add(func11())
            if len(cards_set) == 100:
                break

        for i in range(10):
            cards = [cards_set.pop() for i in range(10)]
            f.write(' '.join(cards) + '\n')

# func12()
# print(func10('cards.txt'))



























