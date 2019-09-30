#coding:utf8

import os

"""
递归遍历指定路径下所有文件
"""
# dir_list = os.listdir('.')
# print(dir_list)


def find_file(path='.', num=0):
    num += 5
    dir_list = os.listdir(path)
    for d in dir_list:
        path_new = os.path.join(path, d)
        if os.path.isdir(path_new):
            print(' '*num, d, '<dir>')
            find_file(path_new, num)
        else:
            print(' '*num, d, '<file>')


if __name__ == '__main__':
    find_file(r'D:\Python3')
