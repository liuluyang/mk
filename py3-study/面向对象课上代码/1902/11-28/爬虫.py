# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/11/28 16:50


"""
http://www.daomubiji.com/dao-mu-bi-ji-1
url href

"""

import requests
import re


def html_get():

    r = requests.get('http://www.daomubiji.com/dao-mu-bi-ji-1')

    print(r, r.status_code)

    print(r.content.decode())

    with open('七星鲁王宫.html', 'w', encoding='utf8') as f:
        f.write(r.content.decode())


def parse_title():

    with open('七星鲁王宫.html', 'r', encoding='utf8') as f:
        text = f.read()

        title_list = re.findall('<article class="excerpt excerpt-c3"><a href=".*?</a></article>', text, re.S)
        # print(title_list)
        with open('章节目录.txt', 'w', encoding='utf8') as f:
            for index, line in enumerate(title_list):
                # print(index, line)
                # print(line.split('href="')[1])
                data = line.split('href="')[1].split('">')
                url = data[0]
                name = data[-1].split('\n')[0]

                f.write(name + '\t' + url + '\n')



if __name__ == '__main__':
    # parse_title()
    pass



















