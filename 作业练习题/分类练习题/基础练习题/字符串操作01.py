


"""
1.模拟字符串拼接的join方法：
res = 'hello world'
print('-'.join(res))  #  h-e-l-l-o- -w-o-r-l-d
"""


"""
2.模拟判断字符串是否以指定的字符串开始或结束：
res = 'hello world'
print(res.startswith('hell'))  # True
print(res.endswith('ld'))      # True
"""


"""
3.模拟字符串的split方法：
res = 'hello'
print(res.split('h'))      # ['', 'ello']
print(res.split('l'))      # ['he', '', 'o']
print(res.split('o'))      # ['hell', '']
"""


"""
4.模拟消除字符串两边空格：
res = ' hello   '
res_new = res.strip()
print(res_new, len(res_new))   # hello  5
"""


"""
5.把字符串res处理成一个新的字符串res_new
res = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
"""


"""
6.把字符串res处理成一个新的字符串res_new
res = 'k1:v1 |k2:v2| k3:v3 | k4:v4'
res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
"""


"""
7.把字符串res处理成一个新的字符串res_new
res = 'k1:v1 |k2:v2||k3:v3 | k4:v4'
res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
"""


"""
8.把字符串res处理成一个字典dic
res = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
"""