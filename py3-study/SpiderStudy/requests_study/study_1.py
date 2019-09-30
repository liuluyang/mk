import requests
import json


"""
http://2.python-requests.org/zh_CN/latest/user/quickstart.html
"""

def save_html(r, name):
    """
    保存页面
    :param r:
    :param name:
    :return:
    """
    with open('{}.html'.format(name), 'w', encoding='utf8') as f:
        f.write(r.content.decode('utf8'))

"""
简单的get请求
以及response
"""

r = requests.get('http://www.baidu.com')
# # save_html(r, 'images/baidu')
# print(r)   # response对象
# print(r.status_code)  # 状态码(数字)
# print(r.content.decode())  # 解码后的页面内容
# print(r.text)              # 自动解码后的页面（一般不用）

"""
带参数请求
"""

params = {'wd':'python'}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36'
}

# url = 'http://www.baidu.com/s?wd=python'
# r2 = requests.get('http://www.baidu.com/s', params=params, headers=headers)
# save_html(r2, 'images/search')
# print(r2)
# print(r2.content.decode())

"""
获取json数据
"""
# r3 = requests.get('https://api.github.com/events')
# print(r3)
# print(json.loads(r3.content.decode()))
# print(r3.json())

"""
post请求
"""
form_data = {
    'k1':'v1',
    'k2':'v2'
}
files = {'file': open('images/baidu.html', 'r', encoding='utf8')}

# r4 = requests.post("http://httpbin.org/post", data=form_data, headers=headers)
# r4 = requests.post("http://httpbin.org/post", files=files, headers=headers)
# print(r4)
# for k, v in r4.json().items():
#     print(k, v)

"""
其他属性
"""
# r5 = requests.get('http://www.baidu.com')
# print(r5.headers)
# print(dict(r5.cookies))
# print(r5.url)

"""
重定向
allow_redirects=False 默认可以重定向
timeout = 10   可设置超时时间
"""

# r6 = requests.get('http://github.com', timeout=0.1)
# r6 = requests.get('http://github.com', allow_redirects=False)
# print(r6)
# print(r6.url)
# print(r6.history)