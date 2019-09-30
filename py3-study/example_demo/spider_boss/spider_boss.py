import json, requests
from urllib import parse
from lxml import etree
import redis
import time
import random


pool = redis.ConnectionPool(host='', port=6379, db=9, password='')
redis_9 = redis.Redis(connection_pool=pool)
base_url = 'https://www.zhipin.com'
city = (('天津','c101030100'), ('合肥','c101220100'), ('青岛','c101120200'),
        ('郑州','c101180100'), ('南京','c101190100'), ('西安','c101110100'))
query = ['python', 'php']


def recruitment_list_get(c, q):
    """
    列表数据请求
    :param c:
    :param q:
    :return:
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36',
    }
    url = 'https://www.zhipin.com/{}/?query={}&page={}'
    print(c, q)
    page = 1
    while True:
        r = requests.get(url.format(c[1], q, page), headers=headers)
        print(r)
        html = r.content.decode()
        # with open('index.html', 'w', encoding='utf8') as f:
        #     f.write(html)
        is_next = content_parse(html, c, q)
        if is_next < 30:
            break
        page += 1
        time.sleep(random.random())


def content_parse(content, c=None, q=None):
    """
    列表内容解析
    :param content:
    :return:
    """
    html = etree.HTML(content)
    info_list = html.xpath('//div[@class="job-list"]/ul/li')
    for li in info_list:
        title = li.xpath('.//div[@class="job-title"]/text()')
        red = li.xpath('.//span[@class="red"]/text()')
        p = li.xpath('.//p/text()')
        name = li.xpath('.//h3[@class="name"]/a/text()')[-1]
        detail_url = li.xpath('.//a/@href')[:2]
        # print(title, red, p, name, detail_url)
        data = (
            ('title', title[0]), ('red', red[0]), ('other', p), ('name', name),
            ('title_url', detail_url[0]), ('name_url', detail_url[-1]),
            ('city', c[0]), ('query', q)
        )
        data = dict(data)
        print(data)

        redis_9.hset('position', data['title_url'], json.dumps(data))

    print(len(info_list))

    return len(info_list)


def detail_content(title_url):
    """
    详情页信息抓取
    :param title_url:
    :return:
    """
    if redis_9.sismember('detail_set', title_url):
        print('%s详情页信息已经存在'%(title_url))
        return False

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'cookie':'_uab_collina=156352061232239760898125; __guid=95203226.2691480139271496000.1563528506254.9312; monitor_count=5; __c=1563530041; __g=-; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F6a3d21fc63e56a2003Z52d27GVo~.html&r=; __a=59991252.1563520673.1563520673.1563530041.2.2.1.2; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1563520614,1563530041; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1563530041'
    }
    url = parse.urljoin(base_url, title_url)
    r = requests.get(url, headers=headers)
    if r.status_code in [404]:
        return None
    print(r, url)
    content = r.content.decode()
    # print(content)
    # with open('detail.html', 'w', encoding='utf8') as f:
    #     f.write(content)
    html = etree.HTML(content)
    text = html.xpath('//div[@class="job-sec"]/div/text()')
    text_new = ''
    for t in text:
        t =t.strip()
        if t:
            text_new += t + '\n'
    print(text_new)

    redis_9.hset('detail_dict', title_url, text_new)
    redis_9.sadd('detail_set', title_url)

    return text_new


def spider_main():
    """
    主程序
    :return:
    """
    for c in city[:]:
        for q in query[:]:
            recruitment_list_get(c, q)
            time.sleep(random.random())

def detail_main():
    """
    主程序
    :return:
    """
    # text_dict = redis_9.hgetall('detail_dict')
    # text_dict = {k.decode():v.decode() for k,v in text_dict.items()}
    # print(text_dict)
    # data = redis_9.hgetall('position')
    # json.dump({k.decode():v.decode() for k,v in data.items()}, open('data.txt', 'w'))
    data = json.load(open('data.txt', 'r'))
    for title_url in list(data.keys())[1950:]:
        # print(title_url)
        result = detail_content(title_url)
        if result == '':
            break
        time.sleep(random.random())


if __name__ == '__main__':
    # spider_main()
    # with open('index.html', 'r', encoding='utf8') as f:
    #     content = f.read()
    # content_parse(content)
    #
    # detail_content('/job_detail/d2732df0257b26231XJ929q_GVo~.html')
    # detail_main()
    pass