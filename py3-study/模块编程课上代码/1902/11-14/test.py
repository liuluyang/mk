

import re



# with open('车牌号.txt', 'r', encoding='utf8') as f:
#     data = f.read()
#     r = re.findall('\w{6}', data)
#
#     r2 = re.findall('(?![0-9]+$)(?![a-zA-Z]+$)([0-9a-zA-Z]{5})', data)
#
#     print(r)
#
#     print(r2)



# 从头开始匹配  匹配单个
# obj = re.match('\d+', 'r123uuasf123')
# if obj:
#     print(obj.group())

# 搜索 匹配单个 可分组
# obj = re.search('(\d+)(uu\w*)', 'r123uuasf123')
# if obj:
#     print(obj.groups())

# 替换
# obj = re.sub('\d{2}', ' | ', '123hello123   word2TTTT')
# if obj:
#     print(obj)

# 切分
# obj = re.split('\d{3}', '123hello321   word2TTTT')
# if obj:
#     print(obj)

##############################################


# qq = '12321312@qq.com  1321321xx@163.com'
# print(re.findall('\w+@qq.com', qq))


# 匹配中文 [\u4e00-\u9fa5]

info = """
姓名        地区    身高    体重    电话
况咏蜜     北京    171    48    13651054608
王心颜     上海    169    46    13813234424
马纤羽     深圳    173    50    13744234523
乔亦菲     广州    172    52    15823423525
罗梦竹     北京    175    49    18623423421
刘诺涵     北京    170    48    18623423765
岳妮妮     深圳    177    54    18835324553
贺婉萱     深圳    174    52    18933434452
叶梓萱    上海     171    49    18042432324
杜姗姗   北京      167    49    13324523342
"""
# print(re.findall('[\u4e00-\u9fa5]+', info))
# print('中'.isalpha())

# 取出两边空格
s = '   he llo  '
r = re.sub('^\s+', '', s)
r2 = re.sub('\s+$', '', r)
print(r, len(r), r2, len(r2))