



"""
1. 第一题：
写一个函数register
需要传入姓名、年龄、性别、职业、国籍等参数
然后把数据写入文件
"""

def func01():
    print('我是func01')
    print('数据已存入')
    pass


"""
2. 第二题：
    写个函数 无限接收用户的输入，
    然后调用register函数，把接收的输入存入文件
    当接收的输入等于q时，结束循环
"""

def func02():

    while True:
        data = input('>>>')
        if data == 'q':
            break

        func01()

func02()


"""
3. 第三题：
    查找
    当输入姓名时，打印出这个人的信息
    当查找的这个人不存时，打印’找不到‘
"""


