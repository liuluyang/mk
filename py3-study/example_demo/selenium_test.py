from selenium import webdriver
import time


"""
/s?wd=%E5%A4%A7&pn=10&oq=%E5%A4%A7&ie=utf-8&usm=1&rsv_idx=1&rsv_pq=ae38f8320000bd8a&rsv_t=a04bQmVvnOhjCvOAMHUNdfZZQhHS7K%2FdKqCOkM%2FXleaZD7yZwg0NxOHAcbI
/s?wd=%E5%A4%A7&pn=20&oq=%E5%A4%A7&ie=utf-8&usm=1&rsv_idx=1&rsv_pq=ae38f8320000bd8a&rsv_t=a04bQmVvnOhjCvOAMHUNdfZZQhHS7K%2FdKqCOkM%2FXleaZD7yZwg0NxOHAcbI
/s?wd=%E5%A4%A7&pn=30&oq=%E5%A4%A7&ie=utf-8&usm=1&rsv_idx=1&rsv_pq=ae38f8320000bd8a&rsv_t=a04bQmVvnOhjCvOAMHUNdfZZQhHS7K%2FdKqCOkM%2FXleaZD7yZwg0NxOHAcbI
"""

browser = webdriver.Chrome('E:\刘禄扬\安装包\chromedriver\chromedriver.exe')


url_index = 'http://www.baidu.com'
url_search = 'http://www.baidu.com/s?bdorz_come=1&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=大'

browser.get(url_search)

print(browser.get_cookies())
a_list = browser.find_elements_by_tag_name('a')
print(a_list)
for a in a_list:
    print(a.click())
    time.sleep(1)



