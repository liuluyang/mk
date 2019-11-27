

import os


################################################## os

# 获取所给路径下所有文件和文件夹的名字
# print(os.listdir('D:\\'))

# 路径拼接
# print(os.path.join('D:\\', 'f'))

# 判断所给路径是否存在
# print(os.path.exists(os.path.join('D:\\', 'f')))

# 判断所给路径是否是目录
# print(os.path.isdir(os.path.join('D:\\', '306')))

# 判断所给路径是否是文件
# print(os.path.isfile(os.path.join('D:\\', '306')))

# 获取当前文件路径
# print(__file__)

# 获取绝对路径
# print(os.path.abspath('t'))

# 获取路径名
# print(os.path.dirname('E:/project/education/11-07'))

# 修改当前工作目录
# os.chdir(os.path.dirname(os.getcwd()))

# 获取当前文件工作路径
# print(os.getcwd())

# 删除文件
# print(os.remove(r'E:\project\education\test\t.py'))

# 只能删除空的目录
# print(os.removedirs(r'E:\project\education\test'))

# 查看文件或者目录信息
# print(os.stat(r'E:\project\education\test\t.py'))

# 获取文件大小
# print(os.path.getsize(r'E:\project\education\test\t.py'))

# 创建单个目录 #当文件已存在时，无法创建该文件
# os.mkdir('dir')

# 创建多级目录 #当文件已存在时，无法创建该文件
# os.makedirs('dir/dr/d/d/d/d')

# 重命名文件或目录
# os.renames('wd.py', 'hello.py')


