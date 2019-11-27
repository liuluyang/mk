
import sys


######################################### 模仿input/print函数


# data = input('>>>')

def input_new(*args):
    """

    :param args:
    :return:
    """
    if len(args) > 1:
        raise
    elif len(args) == 1:
        sys.stdout.write(str(args[0]))

    data = sys.stdin.readline()

    return data

# data = input_new('>>>')
# print(data)

############################################### print

f = open('t', 'w', encoding='utf8')
# print('111', '222', [111], sep='-')
# print('111', '222', [111], sep='-')

def print_new(*args, sep=' ', end='\n', file=None):

    # sys.stdout.write(sep.join([str(i) for i in args]))

    for index, a in enumerate(args):
        sys.stdout.write(str(a))
        if index != len(args)-1:
            sys.stdout.write(sep)

    sys.stdout.write(end)

# print_new('111', '222', [111], sep='-')
# print_new('111', '222', [111], sep='-')
# print('-'.join('abc'))


################################################ 回文字符串


s = 'aba'

# print(s == s[::-1])

# print('aba' == 'abc')


print('abc'*1000 + 'n')
print('abc'*1000 + 'v')









