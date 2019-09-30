#coding:utf8
import os
import time

"""
os模块学习
注：
删除操作慎用
"""

# 指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
work_station = os.name
# print('当前平台：', work_station)

# 返回指定目录下的所有文件和目录名
listdir = os.listdir('D://Python')
# print(len(listdir), listdir)

# 得到当前工作目录
getcmd = os.getcwd()
# print(getcmd)

# 创建目录 注：目录已存在时会出错
dir_name = 'mkdir_demo'
full_path = os.path.join(getcmd, dir_name)
# print(full_path)
# if not os.path.exists(full_path):
#     os.mkdir('mkdir_demo')
#     print('创建dir成功')
# else:
#     print('{}已存在'.format(dir_name))

# 删除目录 注：目录不存在时会出错
# time.sleep(1)
# os.rmdir(dir_name)  # 只能删除空目录

# 删除文件 注：文件不存在时会出错
# os.remove('he.py')

# 改变工作目录到dirname: os.chdir(dirname)
# os.chdir(dir_name)
# print(os.getcwd())

# 运行shell命令 执行成功返回0 失败是1
# s = os.system('dir')
# print(s)

# 判断是否是文件、目录(文件、目录不存在返回False)
# print(os.path.isdir(dir_name))
# print(os.path.isfile('hello.py'))

# 判断文件、目录是否存在
# print(os.path.exists(dir_name))
# print(os.path.exists('h'))

# 获取文件大小 目录返回0 文件不存在会报错
# file_size = os.path.getsize('hello_modul.py')
# print('{}字节'.format(file_size))

# 返回目录和文件名
path_split = os.path.split(full_path)
# print(path_split)
# 返回路径文件名和文件路径
# print(os.path.basename(full_path))
# print(os.path.dirname(full_path))
# print(full_path.split('\\'))

# 获得绝对路径 对比os.getcwd()
# print(os.path.abspath('../'))
# print(os.getcwd())

# 链接目录和文件名
# print(os.path.join('D://', 'file.text'))

# for name in ['a.txt', 'b.txt']:
    # os.mkdir(os.path.join(full_path, name.split('.')[0])) # 创建单级目录
    # os.makedirs(os.path.join(full_path, name.split('.')[0], name)) # 创建多级目录
    # with open(os.path.join(full_path, name), 'w') as f:
    #     pass
    # pass

"""
os 模块提供了很多允许你的程序与操作系统直接交互的功能

得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
返回指定目录下的所有文件和目录名:os.listdir()
函数用来删除一个文件:os.remove()
删除多个目录：os.removedirs（r“c：\python”）
检验给出的路径是否是一个文件：os.path.isfile()
检验给出的路径是否是一个目录：os.path.isdir()
判断是否是绝对路径：os.path.isabs()
检验给出的路径是否真地存:os.path.exists()
返回一个路径的目录名和文件名:os.path.split()     e.g os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt') 
分离扩展名：os.path.splitext()       e.g  os.path.splitext('/usr/local/test.py')    结果：('/usr/local/test', '.py')
获取路径名：os.path.dirname()
获得绝对路径: os.path.abspath()  
获取文件名：os.path.basename()
运行shell命令: os.system()
读取操作系统环境变量HOME的值:os.getenv("HOME") 
返回操作系统所有的环境变量： os.environ 
设置系统环境变量，仅程序运行时有效：os.environ.setdefault('HOME','/home/alex')
给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux and MAC使用'\n'
指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
重命名：os.rename（old， new）
创建多级目录：os.makedirs（r“c：\python\test”）
创建单个目录：os.mkdir（“test”）
获取文件属性：os.stat（file）
修改文件权限与时间戳：os.chmod（file）
获取文件大小：os.path.getsize（filename）
结合目录名与文件名：os.path.join(dir,filename)
改变工作目录到dirname: os.chdir(dirname)
获取当前终端的大小: os.get_terminal_size()
杀死进程: os.kill(10884,signal.SIGKILL)
"""