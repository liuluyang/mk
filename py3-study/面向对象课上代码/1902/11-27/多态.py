


class Open:

    def read(self):

        print('你猜我在干嘛。。。。')


#####################################  不同对象调用相同的方法
# f = open('练习题.py', 'r', encoding='utf8')
# print(f.read())
#
# # 类文件对象
# op = Open()
# op.read()
#
# import sys
#
# t = sys.stdin.read()
# print(t)


#######################################  统一接口调用

class Test1:

    def read(self):
        return '我正在写代码。。。'

class Test2:

    def read(self):
        return '我不知道在干吗。。。'

f = open('练习题.py', 'r', encoding='utf8')
t1 = Test1()
t2 = Test2()


def run(obj):
    print(obj.read())


# run(f)
# run(t1)
# run(t2)

