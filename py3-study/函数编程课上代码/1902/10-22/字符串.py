

"""
replace split join count index strip startswith endswith isdigit isalnum zfill format
"""
func_lst = ''.__dir__()
func_new = []
for i in func_lst:
    if not i.startswith('__'):
        func_new.append(i)

# print(len(func_new), func_new)
# print('upper'.upper())

# 判断整数字符串
# print('123213'.isdigit())
# 判断字母字符串
# print('adA'.isalpha())
# 判断里面是数字或字母
# print('121'.isalnum())
# 填充
# print('123'.zfill(10))

# 格式化
names = ['小红', '小白', '小黑', '小绿']
# for name in names:
#     res05 = """
#
#     亲爱的：{}
#
#     .........
#     再见{}
#     """.format(name, name)
#     print(res05)

# for name in names:
#     res05 = """
#
#     亲爱的：%s
#
#     .........
#     再见%s
#     """%(name, name)
#     print(res05)



# 替换
# res01 = '屈晓明'
# res_new = res01.replace('屈', '张')
# print(res01, res_new)

# 切分
res02 = '1, 2, 3'
# res02 = open('信息', 'r', encoding='utf8').read()
# print(res02)
# print(res02.split())

# 统计
# dic = {}
# lst_num = [1, 2, 3, 1, 1]
# for n in lst_num:
#     dic[n] = lst_num.count(n)
#     print(n, dic)
#
# print(dic)

# 找元素索引位 找不到汇报错
res03 = '133213123'
# print(res03.index('2'))
# print(res03.find('22'))

# 取字符串两边空格
res04 = 'liuluyang '
# print(len(res04))
# print(len(res04.strip()))


res05 = '1123q'
print(not res05.isdigit() and not res05.isalpha() and res05.isalnum())





