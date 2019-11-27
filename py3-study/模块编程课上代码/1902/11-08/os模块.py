

import os


"""
提供文件或者目录的一些操作
"""

# 获取当前脚本执行路径  **
# print(repr(os.getcwd()))

# 获取指定目录下所有文件、文件夹 **
# print(os.listdir('D:/n'))

# 创建单个（一级）文件夹 #当文件已存在时，无法创建该文件
# os.mkdir('dir/d/d')

# 创建多个（多级）文件夹 #当文件已存在时，无法创建该文件
# os.makedirs('dir_new/d/d/d/d/t.py')

# 删除文件
# os.remove(r'E:\project\education\other\t')

# 只能删除空文件夹
# os.removedirs('d')

# 重命名文件或目录
# os.renames(r'E:\project\education\other\t', r'E:\project\education\other\y')
# os.renames('dir', 'dir_rename')

#################################################### path **

# 返回当前文件路径 E:\project\education\11-08\os模块.py
# print(repr(__file__))
# print(__file__)
# 获取完整路径
# print(os.path.abspath(__file__))

# 获取给定目录所在路径
# print(os.path.dirname(os.path.abspath(__file__)))

# 判断给定的路径是否存在
# print(os.path.exists('D:/Dict'))

# 判断给定的路径是否是文件的路径，不是或者不存都返回False
# print(os.path.isfile('D:/Dict'))

# 判断给定的路径是否是文件夹的路径，不是或者不存都返回False
# print(os.path.isdir('D:/Dict/r'))

# print(os.listdir('.'))
# 路径拼接
# print(os.path.join('D:/', 't'))

# path_now = os.getcwd()
# for i in os.listdir('.'):
#     path_full = os.path.join(path_now, i)
#     if os.path.isdir(path_full):
#         for ii in os.listdir(path_full):
#             print(ii)

# 获取文件的大小
# print(os.path.getsize(__file__))
# print(os.path.getsize('dir_new')) # 0 不能获取文件夹大小

# file_info= os.stat(__file__)

import time

# # 修改时间
# print(time.localtime(file_info.st_atime))
# print(time.localtime(file_info.st_mtime))
# # 创建时间
# print(time.localtime(file_info.st_ctime))








