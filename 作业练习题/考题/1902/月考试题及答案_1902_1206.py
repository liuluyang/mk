

"""
月考
"""


"""15
from itertools import count

测试count的用法
1、解释count的用法（参数，返回值、返回值类型等方面）
2、写个类模仿count的功能
"""
from itertools import count
from typing import Iterator

r = count(1, 2)
# print(r, isinstance(r, Iterator))
# print(next(r))
# print(next(r))
# for i in r:
#     print(i)

class CountNew:

    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step

    def __iter__(self):

        return self

    def __next__(self):

        self.start += self.step

        return self.start - self.step

    def __repr__(self):

        return 'CountNew(%s, %s)'%(self.start, self.step)

# r2 = CountNew(1, 2)
# print(r2, isinstance(r2, Iterator))
# print(next(r2))
# print(next(r2))
# for i in r2:
#     print(i)


"""15
列表nums里面每个数都不相同，从里面找出两个数相加结果跟target相等，
返回这两个数的索引值
nums = [1, 2, 3, 5, 8, 7, 9]
target = 16

result = (4, 5)
"""
def func_02(nums, target):

    n = 0
    for index01, x in enumerate(nums):
        for index02, y in enumerate(nums):
            n += 1
            print(n)
            if x + y == target and index01!=index02:
                return index01, index02

def func_02_02(nums, target):

    n = 0
    for index01 in range(len(nums)):
        for index02 in range(index01 + 1, len(nums)):
            n += 1
            print(n)
            x, y = nums[index01], nums[index02]
            if x + y == target:
                return index01, index02

def func_02_03(nums, target):

    data = {}
    n = 0
    for index, num in enumerate(nums):
        n += 1
        print(n)
        anther_num = target - num
        if anther_num in data:
            return index, data[anther_num]
        else:
            data[num] = index
        print(data)


nums = [1, 2, 3, 5, 8, 7, 9]
target = 16
# print(func_02(nums, target))
# print(func_02_02(nums, target))
# print(func_02_03(nums, target))


"""15
读取score.csv文件（注意编码）
求每个学生四科成绩总分并从大到小进行排序
写入新的文件score_sorted.csv
"""
def func_03():

    data = []
    with open('score.csv', 'r', encoding='gbk') as f:
        f.readline()
        for line in f:
            line = line.strip()
            line_list = line.split(',')
            count = int(line_list[2]) + int(line_list[3])+ int(line_list[4])+ int(line_list[5])
            line_list.append(count)

            data.append(line_list)

        with open('score_sorted.csv', 'w', encoding='utf8') as f_new:
            data.sort(key=lambda x:x[-1], reverse=True)
            f_new.write('学号,姓名,一,二,三,四,总分\n')
            for d in data:
                d[-1] = str(d[-1])
                f_new.write(','.join(d) + '\n')
# func_03()


"""15
写一个函数
def open_file(file):
    pass

1、该函数只能够正常读取gbk或者utf8编码的文本文件, 然后返回文件内容
2、如果读取失败（解码失败），主动触发异常，异常内容为：该文件不是gbk或utf8编码
3、其他异常正常抛出
"""
def open_file(file):

    try:
        with open(file, "r", encoding="utf8") as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(file, "r", encoding="gbk") as f:
                return f.read()
        except UnicodeDecodeError:
            raise ValueError("该文件不是gbk或utf8编码")

def open_file_new(file):

    for encode_type in ['utf8', 'gbk']:
        try:
            with open(file, "r", encoding=encode_type) as f:
                return f.read()
        except UnicodeDecodeError:
            pass
    else:
        raise ValueError("该文件不是gbk或utf8编码")

# print(open_file('test1.py'))
# print(open_file_new('score.csv'))


"""15
写五个特殊方法，解释并演示他们的用法
"""
class F:

    def __int__(self):
        """
        支持int()操作
        :return:
        """

        return 1


f = F()
#
# print(int(f))


"""15
查看日志.txt文件
1、统计出访问频率最高的ip地址
2、并把他的访问记录写入一个新的文件 高频访问ip.txt
"""
def func_04():

    with open('日志.txt', 'r', encoding='utf8') as f:
        dic = {}
        max_num = 0
        word = []
        for line in f:
            ip = line.split("'")[1]
            if ip in dic:
                dic[ip] += 1
            else:
                dic[ip] = 1
            num = dic[ip]
            if num > max_num:
                max_num = num
                word = [ip]
            elif num == max_num:
                word.append(ip)
        # print(dic)
        # print(word, max_num)

    f_new = open('高频访问ip.txt', 'w', encoding='utf8')
    with open('日志.txt', 'r', encoding='utf8') as f:
        for line in f:
            for ip in word:
                if ip in line:
                    f_new.write(line)
                    break
# func_04()



"""30
写一个练习打字的程序
要求：
1、读取文件内容、对内容进行处理
2、开始一行一行打字，每打一行，把打错的字标出来，并计算正确率
3、‘close()’为结束程序的标志
4、结束打字时，把打字开始时间、用时、总字数、正确率等信息写入文件。

初始化函数  __init__
读取文件    content
统计每行正确率  count
打字结束统计信息  close
开始打字主函数       start
"""


def func_05():

    with open('我的作品.txt', 'r', encoding='utf8') as f:
        for line in f:
            line = line.strip()
            print('>>>', line)
            line_new = input('>>>')

            n = 0
            for x, y in zip(line, line_new):
                if x == y:
                    n += 1
            percent = int(n / len(line) *100)
            print('正确率：%s%%'%(percent))

# func_05()

import time

class Writing:
    """
    练习打字程序
    """
    log_file = 'writing.log'

    def __init__(self, filename):

        self.filename = filename
        self.start_timestamp = time.time()
        self.start_time_str = time.strftime('%Y-%m-%d %X', time.localtime())
        # 总字数
        self.words_count = 0
        # 正确率
        self.accuracy = []
        self.close_tag = 'close()'

    @staticmethod
    def set_color(s):
        """
        设置字符串颜色
        :param s:
        :return:
        """

        return '\033[1;%sm%s\033[0m' % (33, s)

    def content(self):
        """
        练习内容读取、处理
        :return:
        """
        with open(self.filename, 'r', encoding='utf8') as f:
            for index, line in enumerate(f):
                line = line.strip()
                if line:
                    line = line[:30]
                    yield line

        # return ['hello', 'world']

    def count(self, line, line_new):
        """
        实时统计练习结果
        :param line:
        :param line_new:
        :return:
        """
        line_len = len(line)
        num = 0
        check_line = ''
        for x, y in zip(line, line_new):
            if x == y:
                num += 1
            else:
                y = self.set_color(y)
            check_line += y
        percent = num / line_len
        self.words_count += line_len
        self.accuracy.append(percent)

        print('#' * 40)
        print(line)
        print(check_line)
        print('正确率%s%%' % int(percent * 100))
        print('#' * 40)

    def close(self):
        """
        结束练习
        进行数据统计、记录
        :return:
        """
        with open(self.log_file, 'a', encoding='utf8') as f:
            use_time = round((time.time() - self.start_timestamp) / 60)
            accuracy = int(sum(self.accuracy) / len(self.accuracy) * 100)
            self.format_str = '开始时间：%s\t用时：%s分钟\t总字数：%s\t正确率：%s%%\n' % (
                self.start_time_str, use_time, self.words_count, accuracy
            )
            f.write(self.format_str)

    def start(self):
        """
        开始练习
        :return:
        """

        for line in self.content():
            print('>>>', line)
            print()
            line_new = input('>>>')
            if line_new == self.close_tag:
                break
            self.count(line, line_new)

        self.close()
        print(self.format_str)
        print('练习结束')

        return True














