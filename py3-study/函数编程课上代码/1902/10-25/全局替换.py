

import random


with open('我的作品.txt', 'r', encoding='utf8') as f:
    text = f.read()
    while True:
        res = input('请输入你要查找的内容：')
        print(text.replace(res, '\033[1;%sm%s\033[0m'%(random.randrange(31, 37), res)))