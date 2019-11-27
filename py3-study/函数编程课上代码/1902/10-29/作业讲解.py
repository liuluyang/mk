

import random

def set_color(res, num=None):
    """
    给字符串添加颜色
    :param res:
    :return:
    """
    if num is None:
        color_num = random.randint(30, 37)
    else:
        color_num = num
    res_new = '\033[1;%sm%s\033[0m' % (color_num, res)

    return res_new


"""
1. 第一题：
写一个函数register
需要传入姓名、年龄、性别、职业、国籍等参数
然后把数据写入文件
"""

def register(name, age, gender, position, country='中国'):

    with open('人员信息.txt', 'a', encoding='utf8') as f:
        f.write(' '.join([name, str(age), gender, position, country]) + '\n')
    print(set_color('数据存入成功'))

# register('老王', 40, '男', '程序员', '德国')

"""
2. 第二题：
    写个函数 无限接收用户的输入，
    然后调用register函数，把接收的输入存入文件
    当接收的输入等于q时，结束循环
"""


def main():

    while True:
        data = input('请输入人员信息：')

        # 结束程序
        if data == 'q':
            break

        # 处理数据
        data = data.split()

        # 判断参数的完整性
        if len(data) < 4 or len(data) > 5:
            print(set_color('输入的人员信息错误', 31))
            continue

        # 存入数据
        register(*data)

# main()

"""
3. 第三题：
    查找
    当输入姓名时，打印出这个人的信息
    当查找的这个人不存时，打印’找不到‘
"""


def check(filename='人员信息.txt'):

    with open(filename, 'r', encoding='utf8') as f:

        # 方法一
        data_dict = {}
        for line in f:
            line = line.strip()
            if line:
                lst = line.split()
                data_dict[lst[0]] = lst

        while True:
            name = input('请输入你要查找的人员：')
            info = data_dict.get(name)
            if info:
                print(set_color('-'.join(info)))
            else:
                print(set_color('找不到', 31))


        # 方法二
        # data = f.readlines()
        # print(data)

        # while True:
        #     name = input('请输入你要查找的人员：')
        #
        #     for d in data:
        #         if d.startswith(name):
        #             print(set_color(d))
        #             break
        #     else:
        #         print(set_color('找不到', 31))


# check()




