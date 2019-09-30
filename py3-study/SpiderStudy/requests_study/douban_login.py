import requests



"""
requests模拟登录
"""

headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

login_url = 'https://accounts.douban.com/j/mobile/login/basic'
account_url = 'https://www.douban.com/people/153743685/'

data = {
'ck': '',
'name': '150',
'password': '',
'remember': 'false',
'ticket':''
}

cookies = {
    'dbcl2':'153743685:nk2kEd4141Y'
}


def login():
    # 保持会话
    # requests = requests.Session()
    # dbcl2="153743685:nk2kEd4141Y"
    r = requests.post(login_url, data=data, headers=headers)

    print(r)
    print(r.json())
    print(r.headers['set-cookie'])

    r2 = requests.get(account_url, headers=headers, allow_redirects=False,
                        cookies=cookies
                      )
    print(r2)
    #　print(r2.content.decode())

if __name__ == '__main__':
    pass
