



"""
第一题：
判断下面的字符串里面括号是否完整正确闭合

s = '(())'

举例不符合的：
s1 = ')'
s2 = '('
s3 =  '())(()'
"""

def func_01(res):
    """
    方法一
    :param res:
    :return:
    """
    while True:
        if res.startswith(')') or res.endswith('('):
            return False
        if len(res) == 0:
            return True
        res = res.replace('()', '')


def func_02(res):
    """
    方法二
    :param res:
    :return:
    """
    nums = 0
    for per in res:
        if per == '(':
            nums += 1
        elif per == ')' and nums != 0:
            nums -= 1
        elif per == ')' and nums == 0:  # 中途出现 ')'没有元素与之配对
            return False

    if nums != 0:   # 剩余没有配对完
        return False
    else:
        return True


if __name__ == '__main__':
    pass
    res = '(())'
    # print(func_01(res))
    # print(func_02(res))

























