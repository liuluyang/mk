# !/uer/bin/env python
# _*_ utf-8 _*_
# __author__ = Miller
#  2019/9/23 12:00

import time

# with open('test.txt', 'w', encoding='utf8') as f:
#     f.write('hello')

f = open('test.txt', 'w', encoding='utf8')
f.write('hello')
# f.flush()
f.close()
del f


while True:
    time.sleep(1)
    pass

