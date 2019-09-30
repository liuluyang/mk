from bs4 import BeautifulSoup


text = open('test.html', 'r', encoding='utf8').read()
soup = BeautifulSoup(text, 'lxml')

# print(soup)

"""
方法属性
.name
.attrs
.string
.get_text()

注：
弥补xpath做不到的一点
获取某标签下所有内容包括标签
"""

"""
重点：
css选择器
"""
# parse = soup.select('div.content p')
# print(parse, len(parse))


"""
find_all
"""
# parse = soup.find_all(attrs={'class':'top'})
# print(parse, len(parse))

"""
name和attrs
"""
# print(soup.p)
# print(soup.p['class'])
# print(soup.p.string)
# print(soup.div.contents)
# print(soup.div.children)