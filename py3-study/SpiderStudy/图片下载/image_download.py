# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/28 17:09


import requests


r = requests.get('https://wx1.sinaimg.cn/large/70eb479bly1g7f7kclkg6j20f408in44.jpg')
print(r)

# with open('new.jpg', 'wb') as f:
#     f.write(r.content)