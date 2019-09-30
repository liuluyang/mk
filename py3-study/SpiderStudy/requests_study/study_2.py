import requests
from requests.auth import HTTPBasicAuth

"""
会话
"""

session = requests.Session()
# session = requests
cookies = {
    'name':'liu'
}
# session.headers.update({'pass':'111'})
# session.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = session.get('http://httpbin.org/cookies', cookies=cookies)
# print(r.headers)
# print(r.text)


"""
代理IP
"""
proxies = {
  "http": "10.10.1.10:3128",
  "https": "10.10.1.10:1080",
}

# requests.get("http://example.org", proxies=proxies)


"""
身份认证
"""
s = requests.Session()
# s = requests
r2 = s.get('https://www.luffycity.com/python-book/',
                  auth=('user', 'name'))
# r2 = s.get('https://www.luffycity.com/python-book')
print(r2)
print(r2.content.decode())
print(r2.headers)