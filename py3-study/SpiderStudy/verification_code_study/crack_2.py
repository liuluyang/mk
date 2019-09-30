import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


url = 'http://dun.163.com/trial/sense'
browser = webdriver.Chrome('E:\刘禄扬\安装包\chromedriver\chromedriver.exe')
browser.maximize_window()
wait = WebDriverWait(browser, 10)
browser.get(url)


"""模拟点击"""
# time.sleep(1) # 如果不等待会出问题
# browser.find_element_by_xpath('//span[@class="yidun_intelli-text"]').click()

# 等待元素可以点击
# button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="yidun_intelli-text"]')))
# button.click()
# 鼠标悬停
# ActionChains(browser).move_to_element(button).perform()

"""模拟滑动"""
# browser.find_element_by_xpath('//li[@captcha-type="jigsaw"]').click()
# time.sleep(1)
# browser.find_element_by_xpath('//span[@class="yidun_intelli-text"]').click()
# time.sleep(1)
#
# slider = browser.find_element_by_xpath('//div[@class="yidun_slider"]')
#
# for _ in range(5):
#     ActionChains(browser).click_and_hold(slider).perform()
#     ActionChains(browser).move_by_offset(170, 0).perform()
#     time.sleep(0.5)
#     ActionChains(browser).release().perform()
#     time.sleep(2)

"""模拟点选"""
# browser.find_element_by_xpath('//li[@captcha-type="point"]').click()
# time.sleep(1)
# browser.find_element_by_xpath('//span[@class="yidun_intelli-text"]').click()
# time.sleep(1)
#
# img = browser.find_element_by_xpath('//img[@class="yidun_bg-img"]')
# for _ in range(3):
#     webdriver.ActionChains(browser).move_to_element_with_offset(img,
#                     random.random()*100, random.random()*100).click().perform()
#     time.sleep(1)

time.sleep(10)
browser.quit()
