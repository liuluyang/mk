



"""
第一题：
1. 把字符串res01, res02, res03 都转换成字符串res_new
2. 把字符串res_new 转换成字典res_dict

res01 = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
res02 = 'k1:v1 |k2:v2| k3:v3 | k4:v4'
res03 = 'k1:v1 |k2:v2||k3:v3 | k4:v4'

res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'

res_dict = {'k1':'v1', 'k2':'v2', 'k3':'v3', 'k4':'v4'}
"""
res01 = 'k1:v1 | k2:v2 | k3:v3 | k4:v4'
res02 = 'k1:v1 |k2:v2| k3:v3 | k4:v4'
res03 = 'k1:v1 |k2:v2||k3:v3 | k4:v4'

res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'

res01_new = res01.replace(' | ', ',')
res02_new = res02.replace('|', ',').replace(' ', '')
# res03_new = res03.replace('|', ' ').replace('  ', ',').replace(' ', '')
res03_new = ','.join(res03.replace('|', ' ').split())
# print(res_new, '目标')
#
# print(res03_new)
# print(res03_new == res_new)

#################################################### 2
res_new = 'k1:v1,k2:v2,k3:v3,k4:v4'
res_dict = {'k1':'v1', 'k2':'v2', 'k3':'v3', 'k4':'v4'}

# 第一种方法
# dic = {}
# res_new = res_new.split(',')
# for res in res_new:
#     lst = res.split(':')
#     dic[lst[0]] = lst[-1]
#
# print(dic)

# 第二种方法
print(dict([r.split(':') for r in res_new.split(',')]))







