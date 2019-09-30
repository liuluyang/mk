from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Options
import time
import json
import requests
import getpass


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                     '(KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }


def login():
    """
    模拟豆瓣登录selenium版
    :return:
    """
    drive = webdriver.Chrome('E:\刘禄扬\安装包\chromedriver\chromedriver.exe')

    url = 'https://accounts.douban.com/passport/login_popup?login_source=anony'
    # 请求
    drive.get(url)
    time.sleep(2)
    # 保存html
    with open('images/douban_login.html', 'w', encoding='utf8') as f:
        f.write(drive.page_source)
    # 截图
    drive.save_screenshot('images/douban_login.png')

    # 填写登录信息并提交
    drive.find_element_by_xpath('//li[@class="account-tab-account"]').click()
    drive.find_element_by_id('username').send_keys('150')
    drive.find_element_by_id('password').send_keys('')
    time.sleep(1)
    drive.find_element_by_xpath('//a[@class="btn btn-account btn-active"]').click()

    # 获取登录cookies保存到本地
    time.sleep(1)
    cookies = {}
    for c in drive.get_cookies():
        print(c['name'], c['value'])
        cookies[c['name']] = c['value']
    json.dump(cookies, open('images/douban_cookies.txt', 'w'))

    # 关闭浏览器
    drive.quit()


def check_login():
    """
    检查cookies文件是否有效
    :return:
    """
    # 加载cookies
    cookies = json.load(open('images/douban_cookies.txt', 'r'))
    print(cookies)
    # 请求用户页面
    r = requests.get('https://www.douban.com/people/153743685/',
                     allow_redirects=False, cookies=cookies,
                     headers=headers
                     )
    if r.status_code == 200:
        print('cookies有效，登录成功')
    else:
        print('cookies失效，登录失败')
    html = r.content.decode()
    # 保存用户页面
    with open('images/account.html', 'w', encoding='utf8') as f:
        f.write(html)


def check_login_02(session):
    """
    检查登录session版
    :param session:
    :return:
    """
    r = session.get('https://www.douban.com/people/153743685/',
                     allow_redirects=False, headers=headers
                     )
    if r.status_code == 200:
        print('cookies有效，登录成功')
    else:
        print('cookies失效，登录失败')

    return session

def check_login_main():
    session = requests.Session()
    cookies = json.load(open('images/douban_cookies.txt', 'r'))
    session.cookies = requests.utils.cookiejar_from_dict(cookies,
                                                         cookiejar=None,
                                                         overwrite=True)
    print(session)
    session = check_login_02(session)
    check_login_02(session)


if __name__ == '__main__':
    # login()
    # check_login()
    # check_login_main()
    pass