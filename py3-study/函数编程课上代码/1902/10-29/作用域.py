

# 全局变量
text = '职业法师刘海柱'
address = ('192.168.1.1', 8000)


def func_01(text):

    text = 'xxxxxxxx'
    print(text)


# func_01('刘海柱')

###################################

# 函数里面定义的变量是局部变量
# 变量的查找顺序 先找局部变量 再找全局变量
# 函数外面无法引用局部变量

def func_02():

    # text = 'xxxxxxxx'
    print(text)


# func_02()

# print(text)

######################################## 修改全局变量

def func_03():

    # global text   # 声明一下 我要改全局变量
    text = 'xxxxx'

    def inner():

        # global text
        nonlocal text  # 声明一下 我要改外层局部变量
        text = 'yyyyy'

        print(text, 'inner')

    inner()
    print(text, 'outer')
    # inner()


# func_03()
# print(text)

#########################################

# 调用函数时，尽量不要传可变的数据类型
d = {"name": "miller", "age": 26, "hobbie": "大保健"}
l = ["Rebeeca", "Katrina", "Rachel"]


def change_data():

    d["hobbie"] = "学习"
    l.append("XiaoYun")

# change_data()

def change_data_02(info, girls):

    info["hobbie"] = "学习"
    girls.append("XiaoYun")

# change_data_02(d, l)

# print(d, l)


# d = '大保健'
#
# def change_data(info):
#     info = 'xxxx'
#
# change_data(d)
#
# print(d)








