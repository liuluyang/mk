

"""

文件操作
"""

"""
r 只读模式
w 创建模式，若文件已存在，则覆盖旧文件
a 追加模式，新数据会写到文件末尾
b 二进制模式
+ 更新（可读可写）

读取方式
read()  一次读取全部
readlines()  按行读取到列表
readline()   一行一行读

seek()  光标移到
"""

"""
只读模式
注：
文件不存在会报错
"""
# f = open(file='python之禅.txt', mode='r', encoding='utf8')  # 加载文件 文件不存在报错

# data = f.read()
# print(data)
# print(data, len(data))
# f.seek(0)   # 把操作文件的光标移到指定位置

# data_lines = f.readlines()
# print(data_lines)
# print(data_lines, len(data_lines))

# nums = 0
# for line in data_lines:
#     nums += len(line)
# print(nums)

# data_line = f.readline()
# print('第一行：', data_line)
# print('第二行：', f.readline())

# for line in f:
#     print(line)

# f.close()  # 关闭文件

##############################################################
"""
写入模式
注：
1.文件不存在会自行创建
2.如果存在写入新内容会覆盖原文件内容
3.文件关闭时写入的内容才会一次性写入文件（写入的内容先放在内存中）
4.可把文件从内存buffer里强制刷新到硬盘，方法flush()
5.如果以写模式打开文件未写入内容，相当于清空文件
"""
import time

text = """致橡树

我如果爱你
绝不学攀援的凌霄花
借你的高枝炫耀自己

我如果爱你
绝不学痴情的鸟儿
为绿荫重复单调的歌曲
"""

# f = open(file='我的作品.txt', mode='w', encoding='utf8')
# f.write(text)
# f.write('读者：作品不错！\n')  # 如果不加换行符\n会写入在一行
# f.write('是的')

# for line in text.split():
#     f.write(line+'\n')
#     f.flush()           # 强制刷新
#     print('写入：', line)
#     time.sleep(3)
# f.close()

"""
追加写模式
"""
# f = open(file='我的作品.txt', mode='a', encoding='utf8')
# f.write(text)
# f.close()


"""
上下文管理器
语法简写模式
"""

with open(file='我的作品.txt', mode='r', encoding='utf8') as f:
    # print(f.read())
    pass

"""
读写二进制
"""
# from PIL import Image
# im = Image.open('air.jpg')
# im_new = im.convert('1')
# im_new.save('air_new_2.jpg')

# with open('air.jpg', 'rb+') as im:
#     im_data: bytes = im.read()
#     print(im_data)
#     # im.write(im_data)
#     f = open('air_copy.jpg', 'wb')
#     f.write(im_data)
#     f.close()


"""
练习
对指定文字进行替换
"""








