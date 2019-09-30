#coding:utf8



"""
九九乘法表
for循环、循环嵌套、字符串格式化
"""
for i in range(1,10):
    for y in range(1, i+1):
        text = '{} * {} = {}'.format(i, y, i*y)
        print(text, end='\t')
    print('\n')
