from selenium import webdriver
import time
# 无头模式
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

headless = 0
if headless:
    browser = webdriver.Chrome('E:\刘禄扬\安装包\chromedriver\chromedriver.exe',
                           options=options)
else:
    browser = webdriver.Chrome('E:\刘禄扬\安装包\chromedriver\chromedriver.exe')

index_url = 'https://www.qiushibaike.com/'
local_url  = 'http://127.0.0.1:8000/drag_to_drop.html'


def qiubai(browser, url):
    """
    模拟点击下一页
    :param browser:
    :param url:
    :return:
    """
    # 请求页面
    browser.get(url)
    for _ in range(1, 5):
        time.sleep(1)
        # 执行js代码 滚动条下拉到底
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        browser.execute_script('alert("到底了")')
        time.sleep(2)
        # 点击下一页
        browser.find_element_by_xpath('//span[@class="next"]').click()

    # 关闭浏览器
    browser.quit()


def drag_to_drop(browser, url):
    """
    控制可移动元素
    :param browser:
    :param url:
    :return:
    """
    browser.get(url)
    time.sleep(1)
    drag = browser.find_element_by_id('draggable')
    drop = browser.find_element_by_id('droppable')
    # print(drop.location)
    # print(drop.size)

    # webdriver.ActionChains(browser).drag_and_drop_by_offset(drag, 400, 10).perform()
    webdriver.ActionChains(browser).drag_and_drop(drag, drop).perform()


if __name__ == '__main__':
    # qiubai(browser, index_url)
    # drag_to_drop(browser, local_url)
    pass