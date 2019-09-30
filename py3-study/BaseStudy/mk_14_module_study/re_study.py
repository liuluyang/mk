import re

"""
re模块学习

'.'     默认匹配除\n之外的任意一个字符
'^'     匹配字符开头
'$'     匹配字符结尾
'*'     匹配*号前的字符0次或多次     >=0
'+'     匹配前一个字符1次或多次      >=1
'?'     匹配前一个字符1次或0次        1 or 0
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次
'|'     匹配|左或|右的字符
'(...)' 分组匹配
'\d'    匹配数字0-9   =>[0-9]
'\D'    匹配非数字    =>[^0-9]
'\w'    匹配          =>[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9] =>[^A-Za-z0-9]
'\s'     匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]
'\S'     匹配任何非空白字符。等价于 [^ \f\n\r\t\v]
"""

"""
实例
"""
with open('人员信息.txt', 'r', encoding='utf8') as f:
    text = f.read()

    # r = re.findall('\d{11}', text)
    # print(r)

    # r = re.findall('.', text)
    # print(r)

s = '况咏蜜     北京    171    48    13651054608'
print(s)
# print(s.encode(encoding='utf8'))

# r = re.findall('171', s)
# print(r)
#
# r = re.findall('1|4+', s)
# print(r)


# 中文
# r = re.findall('[\u4e00-\u9fa5]+', s)
# print(r)

# 数字
# r = re.findall('\d+', s)
# print(r)

# 非数字
# r = re.findall('\D+', s)
# print(r)

# 数字字母
# r = re.findall('\w+', s)
# print(r)

# r = re.findall('\W+', s)
# print(r)

# 空白字符
# r = re.findall('\s+', s)
# print(r)
#
# r = re.findall('\S+', s)
# print(r)

"""
匹配方式

re.match 从头开始匹配(匹配不到返回None)
re.search 匹配包含(匹配不到返回None)

re.findall 把所有匹配到的字符放到以列表中的元素返回(匹配不到返回[])
re.split 以匹配到的字符当做列表分隔符
re.sub 匹配字符并替换
re.fullmatch 全部匹配
"""

# r = re.match('\w', s)
# if r:
#     print(r, r.group())
# else:
#     print(r)

"""
搜索search
"""
# r = re.search('\d+', s)
# if r:
#     print(r, r.group())
# else:
#     print(r)

"""
split
"""
# r = re.split('\d+', s)
# # print(s.split('8'))
# print(r)

"""
匹配替换
"""
# r = re.sub('\d+', '数字位置', s)
# print(r)

"""
分组:
group() 返回整个匹配
group(index) 返回指定第几组
groups() 以元组形式返回所有组
"""
# r = re.match('(\w)(\w)', s)
# if r:
#     print(r, r.groups())
# else:
#     print(r)


# email_s = '5331@qq.com'
# phone_num = '+8615133224458'
# print(re.match('^\+86\d{11}$', phone_num))
#
# patternas = re.compile('^\+86\d{11}$')
# print(patternas.match(phone_num))

# 密码只能由数字、字母组成而且长度不能小于8位
# passwd = '123456xx'
# print(re.match('^[a-zA-Z0-9]{8,}$', passwd))

# 密码必须包含数字、字母而且长度不能小于8位
# passwd = '123456xx'
# print(re.match('(?![0-9]+$)(?![a-zA-Z]+$)([0-9a-zA-Z]{8,30})$', passwd).groups())

# 贪婪模式和非贪婪模式 ?
# html = '<div>hello</div><div hidden></div>'
# print(re.search('<div>.*?</div>', html))



