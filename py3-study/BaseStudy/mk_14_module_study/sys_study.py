import sys
"""
sys模块学习
"""
print(sys.path)
print(sys.getdefaultencoding())
print(sys.getrecursionlimit())
print(sys.getfilesystemencoding())
print(sys.maxsize)
print(sys.platform)
# for i in range(10):
#     if i > 5:
#         sys.exit(0)
#     else:
#         print(i)
# print(2)
"""
sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
# sys.stdout sys.stdin sys.stderr
sys.stdout.write('please:')  #标准输出 , 引出进度条的例子， 注，在py3上不行，可以用print代替
val = sys.stdin.readline()[:-1] #标准输入
sys.getrecursionlimit() #获取最大递归层数
sys.setrecursionlimit(1200) #设置最大递归层数
sys.getdefaultencoding()  #获取解释器默认编码
sys.getfilesystemencoding  #获取内存数据存到文件里的默认编码
"""

"""
print()=>sys.stdout.write()
错误输出 sys.stderr.write()
input()=>sys.stdin.readline() readlines() read()
"""

def input_new(b='请输入：'):
    """

    :param b:
    :return:
    """
    sys.stdout.write(b)
    line = sys.stdin.readline()
    sys.stdout.write(line)


def print_new(s, end='\n'):
    """

    :return:
    """
    sys.stdout.write(s)
    sys.stdout.write(end)


# input_new()
# print_new('hello', end=' ')
# print_new('hello')