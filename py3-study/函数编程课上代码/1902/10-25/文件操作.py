


"""
文件操作：
    读
    写
    追加写
    二进制读
    二进制写
"""
"""
读取文件
"""

# f = open('我的作品.txt', 'r', encoding='utf8')  # 打开文件
# data = f.read()  # 一次性读取文件的全部内容
# print(f)         # 查看文件对象
# print(data)
# f.seek(12)       # 移动光标


# print(f.readlines())  # 读取所有行 并把内容放入列表
# print(f.readline())   # 读取一行内容
# print(f.readline())

# 循环文件对象
# for line in f:
#     print(line)

# f.close()               # 关闭文件 回收资源


"""
写入数据
"""
# f = open('我的作品02.txt', 'w', encoding='utf8') # 覆盖写
#
# f.write('你好哇\n')
# f.write('李银河\n')
# f.write('你哈\n')
#
#
# f.close()


"""
追加写
"""
# f = open('我的作品03.txt', 'a', encoding='utf8')
#
# f.write('你好哇\n')
# f.write('李银河\n')
# f.write('你哈\n')
#
# f.close()


"""
二进制读
"""
# f = open('favicon.png', 'rb')  # 打开文件
# for index, line in enumerate(f):
#     print(index, len(line), line)
# data = f.read()  # 一次性读取文件的全部内容
# lines = f.readlines()
# print(lines)
# print(len(data))
#
# f.close()

"""
二进制写
"""
# f02 = open('f_new.png', 'wb')
# f02.write(lines[0])
# f02.write(lines[1])
# f02.write(lines[3])
# f02.write(lines[2])
# f02.writelines(lines[4:])
# f02.close()
