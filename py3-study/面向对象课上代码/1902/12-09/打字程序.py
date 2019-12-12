

"""
练习打字程序：
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
        # 正确字数
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


if __name__ == '__main__':
    w = Writing('我的作品.txt')
    r = w.start()
    pass
















