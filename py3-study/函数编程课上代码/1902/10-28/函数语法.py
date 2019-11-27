
import random

"""
函数:
    1. 函数的创建
    2. 函数名的命名规则
    3. 函数的调用

"""

num_01 = 1
num_02 = 2

# 定义一个函数
# func是函数名 跟变量的命名一样

def func_01():

    print('我是函数01')


# 函数的调用
# func_01()

def func_02():

    print('我是函数02')


def my_name():

    with open('我的名字.txt', 'w', encoding='utf8') as f:
        f.write('晓明\n' * 100)


def find_replace():
    """
    查找替换
    :return:
    """

    with open('我的名字.txt', 'r', encoding='utf8') as f:  # 打开文件

        data = f.read()  # 读取内容

        # while True:
        check_text = input('请输入你要查找的内容：')  # 接收输入
        check_nums = data.count(check_text)  # 统计匹配到的内容个数
        print(data.replace(check_text, '\033[1;%sm%s\033[0m' % (
        random.randint(31, 36), check_text)))
        print('找到%s个' % check_nums)

    # 修改

    with open('我的名字.txt', 'w', encoding='utf8') as f:  # 打开文件

        check_new = input('请输入你要修改的内容：')  # 接收输入

        data_new = data.replace(check_text, check_new)  # 替换

        f.write(data_new)  # 写入

        print('修改完成')


# 函数的执行顺序
# my_name()
# find_replace()
# my_name()
# print('函数执行完毕')







