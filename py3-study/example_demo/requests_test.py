from urllib.parse import urlencode, urljoin

import requests
from lxml import etree

base_url = 'http://www.baidu.com/s?bdorz_come=1&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=大'

def html_get(url, html_name):
    r = requests.get(url)
    content = r.content.decode('utf8')
    # with open('{}.html'.format(html_name), 'w', encoding='utf8') as f:
    #     f.write(r.content.decode('utf8'))

    a_list = etree.HTML(content)
    a_list = a_list.xpath('//a/@href')
    print(a_list)
    # href_set = {urljoin(base_url, a) for a in a_list}
    # for href in href_set:
    #     print(href)
    #     if 'http' in href:
    #         try:
    #             r = requests.get(href, allow_redirects=False)
    #             if r.status_code == 200:
    #                 pass
    #                 #print(r.content.decode('utf8'))
    #         except:
    #             print('error')

params = {

    'wd':'大'
}
print(urlencode(params))

def link_html(url):
    r = requests.get(url)
    with open('link.html', 'w', encoding='utf8') as f:
        f.write(r.content.decode('utf8'))


if __name__ == '__main__':
    """
    """
    html_get(base_url, 'baidu_search_result')

    # link_html('http://yun.itheima.com/course/c27.html')