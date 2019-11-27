
import random

# file_name 参数 形参
# 参数都是有顺序的
def find_replace(file_name, num):
    """
    查找替换
    :return:
    """
    print(file_name, num)
    # file_name = input('请输入你要查找的文件：')


    with open(file_name, 'r', encoding='utf8') as f:  # 打开文件

        data = f.read()  # 读取内容

        # while True:
        check_text = input('请输入你要查找的内容：')  # 接收输入
        check_nums = data.count(check_text)  # 统计匹配到的内容个数
        print(data.replace(check_text, '\033[1;%sm%s\033[0m' % (
        random.randint(31, 36), check_text)))
        print('找到%s个' % check_nums)

    # 修改

    with open(file_name, 'w', encoding='utf8') as f:  # 打开文件

        check_new = input('请输入你要修改的内容：')  # 接收输入

        data_new = data.replace(check_text, check_new)  # 替换

        f.write(data_new)  # 写入

        print('修改完成')

# filename = '函数语法.py'
# num01 = 123
# find_replace('函数语法.py', 123)
# find_replace(filename, num01)


########################################## 求和函数
"""
函数的作用：
    1. 减少重复代码
    2. 使程序变的可扩展
    3. 使程序变得易维护
"""

# 自己创建的函数，函数名不能和内建的函数名冲突

def sum_new(num01, num02):
    print(num01, num02)

    result = (num01) + (num02)

    print(result)

    # 返回函数执行的结果
    # 如果没有返回值默认是None
    # 返回值可以是任何数据类型
    return result


r = sum_new(12, 2)
# print(r)
# n01 = input('请输入01：')
# n02 = input('请输入02：')
# print(n01 + n02)
# r = (100*10+1-1**4) + (1*10+1-1**3)
# print(r)












