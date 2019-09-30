from lxml import etree


"""
打开文件
获取ElementTree对象
"""
# html = etree.parse('search.html', etree.HTMLParser())
# print(html)
# print(html.xpath('//title/text()'))


"""
字符串
获取ElementTree对象
"""
# f = open('search.html', 'r', encoding='utf8').read()
# html = etree.HTML(f)
# print(html)

"""
通过路径和标签获取对象列表
"""
# print(html.xpath('//title'))  # 获取title标签
# print(html.xpath('/html/head/title'))
# for s in html.xpath('//script'):
#     print(s)

"""
通配符	描述
*	匹配任何元素节点。
@*	匹配任何属性节点。（获取路径下所有属性）
node()	匹配任何类型的节点。
"""
# print(html.xpath('/html/node()'))
# print(html.xpath('/html/*'))
# print(html.xpath('/@*')) # 获取路径下所有属性


"""
获取特定属性元素
"""
# a_list = html.xpath('//div[@class]')
# a_list = html.xpath('//div[@class="1"]')
# a_list = html.xpath('//div[@id="1"]')
# print(len(a_list), a_list)


"""
获取元素内容
1.属性内容
2.文本内容
"""

# div_list = html.xpath('//div[@class="result c-container "]')
# for d in div_list:
#     # print(d)
#     print(d.xpath('./h3/a[1]/*'))  # 节点元素
#     print(d.xpath('./h3/a[1]/node()')) # 所有元素（包括文本）
#     print(d.xpath('./h3/a[1]/text()')) # 文本
#     print(d.xpath('string(./h3/a[1])')) # 所有元素文本
#     print(d.xpath('./h3/a[1]/@href'))   # href属性值
#     print(d.xpath('./h3/a[1]/@*'))      # 所有属性值



"""
练习
"""
html = etree.parse('test.html', etree.HTMLParser())

# data_list = html.xpath('')
# print(len(data_list))
# print(data_list)
# for d in data_list:
#     print(d)