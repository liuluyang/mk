


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
def func_01():

    result = [1, 'abc', [1, 2, 3], (1, 2, 3), {1:2, 3:4}, {1, 2}]

    return result


"""
第二题：
s = 'k1:v1|| k2:v2|||k3:v3| |k4:v4'
s_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
把字符串s处理成一个新的字符串s_new并返回
"""
def func_02():

    s = 'k1:v1|| k2:v2|||k3:v3| |k4:v4'
    result = s.replace('|', ' ').split()
    result = ','.join(result)

    return result

# func_02()


"""
第三题：
lst = [1, 2, 3, 'a', 4, 'b', 5]
计算列表lst里面所有数字的和
并返回计算结果
"""
def func_03():

    lst = [1, 2, 3, 'a', 4, 'b', 5]

    count = 0
    for n in lst:
        if isinstance(n, int):
            count += n

    return count

# func_03()


"""
第四题：
lst = [['老王', '开车'], ['去', '上班!']]
text = '老王开车去上班!'
把列表lst转换成字符串text并返回
"""

def func_04():

    lst = [['老王', '开车'], ['去', '上班!']]

    text = ''
    for per in lst:
        text += ''.join(per)

    return text

# func_04()


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
def func_05(num):

    nums_01 = list(range(1, num, 2))
    nums_02 = nums_01[::-1][1:]

    for i in nums_01+nums_02:
        print(('*'*i).center(num))

# func_05(10)


"""
第六题：
找出工资最高的人，并返回他的名字
data = {'佩奇':5000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000}
"""
def func_06():

    data = {'佩奇': 5000, '老男孩': 6000, '海峰': 7000, '马JJ': 8000, '老村长': 9000,
            '黑姑娘': 10000}
    max_salary = 0
    result = None
    for name, salary in data.items():
        if salary > max_salary:
            result = name

    return result

# func_06()


#
"""
第七题：
读取user_info.txt的信息
当输入某个人的姓名时，打印出这个人的电话号码
注：当输入的人名不存时程序不能出错，可以返回提示信息
"""
def func_07():

    with open('file/user_info.txt', 'r', encoding='utf8') as f:

        info_dict = {}
        for line in f:
            line_lst = line.split()
            info_dict[line_lst[0]] = line_lst[-1]

        while True:
            name = input('请输入要查询的名字：')
            if name == 'q':
                break

            print(info_dict.get(name, '未找到！'))

# func_07()


#
"""
第八题：
工资单.txt 里面姓名是三个字的,他们工资的总和是多少，返回工资总和
"""
def func_08():

    with open('file/工资单.txt', 'r', encoding='utf8') as f:
        f.readline()
        salary_all = 0
        for line in f:
            line_lst =line.split()
            if len(line_lst[0]) == 3:
                salary_all += int(line_lst[-1])
    return salary_all

# func_08()


#
"""
第九题：
我的作品_打乱.txt 里面是被打乱的作品
需要最后整理成 我的作品_整理.txt 的样子
"""
def func_09():

    with open('file/我的作品_打乱.txt', 'r', encoding='utf8') as f:
        data = {}
        for line in f:
            line_lst = line.split('.')
            data[line_lst[0]] = line
        with open('file/我的作品_new.txt', 'w', encoding='utf8') as f_new:
            for k in sorted(data.keys()):
                f_new.write(data[k])

# func_09()


#
"""
第十题：
从车牌号.txt 文件里面找出所有符合要求的车牌号，
判断一下符合规范的车牌里面，号码是否全部都不一样
如果全部不一样返回True
否则返回False
"""
def func_10():

    with open('file/车牌号.txt', 'r', encoding='utf8') as f:

        cards = []
        for card in f.read().split():
            if not card.isdigit() and not card.isalpha():
                cards.append(card)

        return len(cards) == len(set(cards))

# print(func_10())


"""
第十一题：
写个函数
每次调用该函数返回一个符合要求的车牌号
车牌号要求：
五位数、必须同时包含数字和大写字母
"""
def func_11():

    import random
    import string
    params = string.ascii_uppercase + string.digits

    while True:
        card = ''
        for i in range(5):
            card += random.choice(params)
        if not card.isdigit() and not card.isalpha():
            return card

# print(func_11())


"""
第十二题：
把一百个不同的符合要求的车牌号写入文件
要求：每行十个，每个车牌号之间用空格隔开
"""
def func12():

    with open('file/cards.txt', 'w', encoding='utf8') as f:
        cards_set = set()
        while True:
            cards_set.add(func_11())
            if len(cards_set) == 100:
                break

        for i in range(10):
            cards = [cards_set.pop() for i in range(10)]
            f.write(' '.join(cards) + '\n')