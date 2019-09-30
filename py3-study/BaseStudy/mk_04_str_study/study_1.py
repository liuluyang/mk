#coding:utf8

"""
字符串学习
"""
"""
注：
字符串为不可变对象，
每次对字符串的修改操作都会创建出新的字符串
"""

text_1 = 'this is string'
text_2 = "我是字符串"
text_3 = """
我是多行字符串
我是第二行
"""
text_4 = '''
我是多行字符串,
我是第二行
'''

# # 获取长度
print(len(text_1))
#
# # 取值
# print(text_2[0])
# print(text_2[1])
# print(text_2[0:8])
# print(text_2[:])
# print(text_2[:-1])
# print(text_2[::-1])

# # 拼接
# text_1_2 = text_1 + text_2
# print(text_1_2)

"""
转义符:\
把字符原本的意思转变成具有特殊含义的字符
"""
# text_5 = 'hello python,hello world'
# print(text_5)
# text_5_new = 'hello pytho\n,hello world'
# print(text_5_new)
# text_6 = 'hello\tpython'
# print(text_6)

# # 判断
# text_7 = '我是小a'
# print('a' in text_7)

# 格式化
# text_8 = '我是%s, 今年%d岁, 也可以是%05d, 也可以是%f, ' \
#          '也可以是%0.2f' % ('a', 12, 12, 12.5, 12.5)
# print(text_8)

"""
字符串的操作
"""
str_do_list = [func for func in dir(str) if not func.startswith('__')]
for index, f in enumerate(str_do_list, start=1):
    print(index, f)

# text_9 = 'abc'
# text_9_new = text_9.upper()
# print(text_9, text_9_new)
# text_9 = 'ABC'
# text_9_new = text_9.lower()
# print(text_9, text_9_new)
# text_9 = "  我前后都有空格  到我这结束  "
# text_9_new = text_9.strip()
# print(text_9, len(text_9))
# print(text_9_new, len(text_9_new))


"""
字符串方法
1 capitalize
2 casefold
3 center
4 count
5 encode
6 endswith
7 expandtabs
8 find
9 format
10 format_map
11 index

12 isalnum
13 isalpha
14 isascii
15 isdecimal
16 isdigit
17 isidentifier
18 islower
19 isnumeric
20 isprintable
21 isspace
22 istitle
23 isupper

24 join
25 ljust
26 lower
27 lstrip
28 maketrans
29 partition
30 replace
31 rfind
32 rindex
33 rjust
34 rpartition
35 rsplit
36 rstrip
37 split
38 splitlines
39 startswith
40 strip
41 swapcase
42 title
43 translate
44 upper
45 zfill
"""



