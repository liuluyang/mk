import requests
from retrying import retry
from lxml import etree
import time, random
import queue
import threading


class Qiubai_spider():
    def __init__(self):
        self.url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0"
        }
        self.base_url = 'https://www.qiushibaike.com'

    @retry(stop_max_attempt_number=5)  # 调用retry，当assert出错时候，重复请求5次
    def parse_url(self, url):
        """
        列表页数据请求
        :param url:
        :return:
        """
        response = requests.get(url, timeout=10, headers=self.headers)  # 请求url
        assert response.status_code == 200  # 当响应码不是200时候，做断言报错处理
        print(url)
        # print(response.text)
        with open('data/qiubai.html', 'w', encoding='utf8') as f:
            f.write(response.text)
        return etree.HTML(response.text)  # 返回etree之后的html

    def parse_content(self, html):
        """
        列表内容解析
        :param html:
        :return:
        """
        item_temp = html.xpath('//div[@class="recommend-article"]/ul/li[@class="item typs_word"]')
        # print(len(item_temp), item_temp)
        for item in item_temp:
            # print(item)
            href = item.xpath('.//a[@class="recmd-content"]/@href')[0]
            content = item.xpath('.//a[@class="recmd-content"]/text()')[0]
            u = item.xpath('.//span[@class="recmd-name"]/text()')[0]
            print(href, u)
            print(content)
            self.detail_content(href)

    def detail_content(self, href):
        """
        详细页内容
        :param href:
        :return:
        """
        response = requests.get(self.base_url+href, headers=self.headers)
        html = etree.HTML(response.text)
        content = html.xpath('string(//div[@class="content"])')
        self.q.put(content)

    def run(self, page=1):
        """
        主函数
        :param page:
        :return:
        """
        url = self.url.format(page)  # 获取到url
        html = self.parse_url(url)  # 请求url
        self.parse_content(html)  # 解析页面内容并把内容存入内容队列
        time.sleep(random.random())


if __name__ == "__main__":
    """
    多线程
    """
    q = queue.Queue()
    thread_list = []
    qiubai = Qiubai_spider()
    qiubai.q = q
    for i in range(1, 14):
        t = threading.Thread(target=qiubai.run, args=(i,))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    while True:
        if q.empty():
            break
        data = q.get()
        with open('data/qiubai_thread02.txt', 'a', encoding='utf8') as f:
            f.write(data+'\n')