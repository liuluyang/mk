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

url_index = 'http://www.baidu.com'

# 请求页面
browser.get(url_index)

# 获取cookies
cookies = browser.get_cookies()
print(cookies)

# 生成当前页面快照并保存
browser.save_screenshot('images/baidu.png')

# 页面标题
print(browser.title)

# 搜索关键词python 并点击搜索
kw = browser.find_element_by_id('kw')
kw.send_keys('python')
# 获取内容、属性内容
print(kw.text)
print(kw.get_attribute('class'))
time.sleep(1)
browser.find_element_by_id('su').click()

# 查看cookies
for c in browser.get_cookies():
    print(c['name'], c['value'])
browser.save_screenshot('images/search_result.png')

# 查看页面源码
with open('images/search.html', 'w', encoding='utf8') as f:
    f.write(browser.page_source)


"""
页面操作
Selenium 的 WebDriver提供了各种方法来寻找元素，假设下面有一个表单输入框：
<input type="text" name="user-name" id="passwd-id" />
那么：

# 获取id标签值
element = driver.find_element_by_id("passwd-id")
# 获取name标签值
element = driver.find_element_by_name("user-name")
# 获取标签名值
element = driver.find_elements_by_tag_name("input")
# 也可以通过XPath来匹配
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
# 通过css选择器
element = driver.find_element_by_css_selector("input#passwd-id")
"""

# for _ in range(1, 5):
#     # 当前连接
#     print(_, browser.current_url)
#     time.sleep(1)
#     browser.implicitly_wait(1)
#     browser.find_element_by_xpath('//div[@id="page"]/a[@class="n"]').click()

# 关闭浏览器
browser.quit()