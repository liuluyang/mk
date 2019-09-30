


"""
1.模拟字符串拼接的join方法：
res = 'hello world'
print('-'.join(res))  #  h-e-l-l-o- -w-o-r-l-d
"""
# res = 'hello world'
# print('-'.join(res))
#
# tag = '-'
# res_new = ''
# for s in res:
#     res_new += s + tag
# res_new = res_new[:-len(tag)]
# print(res_new)


"""
2.模拟判断字符串是否以指定的字符串开始或结束：
res = 'hello world'
print(res.startswith('hell'))  # True
print(res.endswith('ld'))      # True
"""
# res = 'hello world'
# print(res.startswith('hell'))
# print(res.endswith('ld'))
#
# tag01 = 'hell'
# tag02 = 'ld'
# print(res[:len(tag01)] == tag01)
# print(res[-len(tag02):] == tag02)


"""
3.模拟字符串的split方法：
res = 'hello'
print(res.split('h'))      # ['', 'ello']
print(res.split('l'))      # ['he', '', 'o']
print(res.split('o'))      # ['hell', '']
"""
# res = 'hello'
# print(res.split('h'))
# print(res.split('l'))
# print(res.split('o'))
#
# res_new_list = []
# res_new = ''
# tag = 'h'
# res_len = len(res)
# index = 0
# for s in res:
#     if s == tag:
#         res_new_list.append(res_new)
#         res_new = ''
#     else:
#         res_new += s
#
#     if index == res_len-1:
#         res_new_list.append(res_new)
#     index += 1
# print(res_new_list)


"""
4.模拟消除字符串两边空格：
"""
# res = ' hello   '
# res_new = res.strip()
# print(res_new, len(res_new))
#
# index_ =  0
# for i in range(len(res)):
#     if res[i] == ' ':
#         index_ += 1
#     else:
#         break
# res_02 = res[index_:]
#
# index_ = -1
# for i in range(len(res_02)):
#     if res_02[index_] == ' ':
#         index_ -= 1
#     else:
#         break
# if index_ != -1:
#     res_02 = res_02[:index_+1]
# print(res_02, len(res_02))


"""
5.把字符串res处理成一个新的字符串res_new
res = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
"""
# res = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
# res_new = res.replace(' | ', ',')
# print(res_new)


"""
6.把字符串res处理成一个新的字符串res_new
res = 'k1:v1 |k2:v2| k3:v3 | k4:v4'
res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
"""
# res = 'k1:v1 |k2:v2| k3:v3 | k4:v4'
# res_new = ','.join(res.replace('|', '').split())
# print(res_new)


"""
7.把字符串res处理成一个新的字符串res_new
res = 'k1:v1 |k2:v2||k3:v3 | k4:v4'
res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
"""
# res = 'k1:v1 |k2:v2| k3:v3 | k4:v4'
# res_new = ','.join(res.replace('|', ' ').split())
# print(res_new)


"""
8.把字符串res处理成一个字典dic
res = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
"""
# res = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
# dic = dict([d.split(':') for d in res.split(' | ')])
# print(dic)