# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/4 11:47

import os
import random

def set_color(s):

    return '\033[1;%sm%s\033[0m'%(random.randrange(34, 35), s)

def check_file(path, num=0):

    file_list = os.listdir(path)

    for file_path in file_list:
        full_path = os.path.join(path, file_path)

        # if '循环' in file_path:
        #     print(os.path.join(path, file_path.replace('循环', set_color('循环'))))

        if os.path.isfile(full_path):
            print('      '*num, full_path, '文件')
            pass
        else:
            print('      '*num, full_path, '目录')
            pass
            check_file(full_path, num + 1)



check_file(r'F:\刘禄扬\project\project\education')










