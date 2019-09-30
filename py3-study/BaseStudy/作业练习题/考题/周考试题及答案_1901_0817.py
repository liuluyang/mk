


"""
周考
"""
"""
注：
所有考题必须在函数内作答
"""

"""
第一题：
给出一个数 num  注意：给出的num大于1
生成一个列表 num_list = [1, 2, ... num, num-1, ...2, 1]
例1：
num = 9
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
例2：
num = 2
num_list = [1, 2, 1]
"""
def create_nums(num):
    """
    第一题
    :param num:
    :return:
    """
    list_01 = list(range(1, num+1))
    list_02 = list(range(1, num))[::-1]
    list_03 = list_01 + list_02

    return list_03

# create_nums(9)

"""
第二题：
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
def create_dimond_01():
    """
    第二题
    :return:
    """
    num = 20
    list_01 = list(range(1, num + 1))
    list_02 = list(range(1, num-1))[::-1]
    nums = list_01 + list_02

    for n in nums:
        if n % 2 == 1:
            s = '*'*n
            print(s.center(30))

# create_dimond_01()

"""
第三题：
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
def create_dimond_02():
    """
    第三题
    :return:
    """
    num = 20
    list_01 = list(range(1, num + 1))
    list_02 = list(range(1, num - 1))[::-1]
    nums = list_01 + list_02

    for n in nums:
        if n % 2 == 1:
            if n != 1:
                s = '*'+' '*(n-2) +'*'
            else:
                s = '*'
            print(s.center(30))

# create_dimond_02()

"""
第四题：
读取user_info.txt的信息
当输入某个人的姓名时，打印出这个人的电话号码
"""
def phone_num_get():
    """
    第四题
    :return:
    """
    name = input('请输入姓名：')
    with open('user_info.txt', 'r', encoding='utf8') as f:
        user_info = []
        for line in f:
            user_info.append(line.split())
        user_info = dict(user_info[1:])
        print(user_info.get(name))

# phone_num_get()

"""
第五题：
我的作品_打乱.txt 里面是被打乱的作品
需要最后整理成 我的作品_整理.txt 的样子
"""
def make_file():
    """
    第五题
    :return:
    """
    with open('我的作品_打乱.txt', 'r',  encoding='utf8') as f:
        text_dict = {}
        for line in f:
            text_dict[line.split('.')[0]] = line

        with open('我的作品_整理.txt', 'w',  encoding='utf8') as f_new:
            for num in sorted(list(text_dict.keys())):
                f_new.write(text_dict[num])

# make_file()

"""
第六题：
找出工资最高的人
data = {'佩奇':5000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000}
"""
def find_person():
    """
    第六题
    :return:
    """
    data = {'佩奇':5000, '老男孩':6000, '海峰':7000, '马JJ':8000, '老村长':9000, '黑姑娘':10000, '白姑娘':10000}
    person_list = []
    high_pay = 0
    for k, v in data.items():
        if v > high_pay:
            high_pay = v
            person_list = [k]
        elif v == high_pay:
            person_list.append(k)

    return high_pay, person_list

# find_person()

"""
第七题：
统计一下 车牌号.txt 文件里面有多少符合规范的车牌
规范：车牌里面必须包含数字和字母 
"""
def card_nums():
    """
    第七题
    :return:
    """
    with open('车牌号.txt', 'r', encoding='utf8') as f:
        cards = f.read().split()
        cards_match = []
        for card in cards:
            if not card.isdigit() and not card.isalpha():
                cards_match.append(card)

        return len(cards_match), cards_match
    pass

# card_nums()

"""
第八题：
判断一下符合规范的车牌里面，号码是否全部都不一样
如果全部不一样返回True
否则返回False
"""
def is_all_different():
    """
    第八题
    :return:
    """
    nums, cards = card_nums()
    # print(nums, cards)

    return len(set(cards)) == nums

# is_all_different()

"""
第九题：
找出出现频率最高的车牌号，以及他们出现的频率
注：如果出现频率最高的有多个车牌，请全部找出来
"""
def find_max_cards():
    """
    第九题
    :return:
    """
    nums, cards = card_nums()
    cards_dict = {}
    same_cards = []
    max_times = 0
    for card in cards:
        if card in cards_dict:
            cards_dict[card] += 1
        else:
            cards_dict[card] = 1

        t = cards_dict[card]
        if t > max_times:
            max_times = t
            same_cards = [card]
        elif t == max_times:
            same_cards.append(card)

    return max_times, same_cards

find_max_cards()


