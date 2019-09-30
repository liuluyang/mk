



"""
第一题：
一个小球从100米的高度落下，之后弹起，弹起高度是下落高度的一半 比如第一次弹起高度为50米
从下落到弹起之后，为一次完整的下落

给一个下落次数：
1.求出此时小球离地面的距离
2.小球总共走的路径
当小球离地面高度小于0.01米时:
3. 小球下落了多少次
"""
def func_01(num):
    """
    第一题 1,2问
    :param num:
    :return:
    """

    path_length = 0
    hight = 100

    for i in range(num):
        path_length += hight
        hight /= 2
        path_length += hight

    return hight, path_length

def func_02():
    """
    第一题 3问
    :return:
    """

    hight = 100
    count = 0
    while True:
        hight /= 2
        count += 1
        if hight < 0.01:

            return count


"""
第二题：
判断一个单个字符是否在一个字符串里面
s_father = 'hello world'
s_child = 'd'
注：不能用in
"""
def func_03(s_father, s_child):
    """
    第二题
    :param s_father:
    :param s_child:
    :return:
    """
    for per in s_father:
        if per == s_child:
            return True

    return False


"""
第三题：
判断一个字符串是否在另一个字符串里面
s_father = 'hello world'
s_child = 'hello'
注：不能用in
"""
def func_04(s_father, s_child):
    """
    第三题
    :param s_father:
    :param s_child:
    :return:
    """
    s_len = len(s_child)
    for index_ in range(len(s_father)-s_len+1):
        per = s_father[index_:index_+s_len]
        if per == s_child:
            return True

    return False


"""
第四题：
给一个排好序的字符串
s = 'DDDAACCBB'
按顺序统计他们的字符出现次数：
s_new = 'D3A2C2B2'
"""
def func_05(res):
    """
    第四题 方法一
    :param res:
    :return:
    """
    lst = []
    s_new = ''
    for s in res:
        if s not in lst:
            lst.append(s)

    for index, v in enumerate(lst):
        nums = res.count(v)
        s_new += v + str(nums)

    return s_new


def func_06(res):
    """
    第四题 方法二
    :param s:
    :return:
    """

    if len(res) == 0:
        return ''

    s_new = ''
    lst = [[res[0], 1]]
    for s in res[1:]:
        if s == lst[-1][0]:
            lst[-1][-1] += 1
        else:
            lst.append([s, 1])

    for per in lst:
        s_new += per[0] + str(per[-1])

    return s_new


def func_07(res):
    """
    第四题 方法三
    :param res:
    :return:
    """
    if len(res) == 0:
        return ''

    s_new = res[0]
    num = 1

    for per in res[1:]:
        if per == s_new[-1]:
            num +=1
        else:
            s_new += str(num)
            s_new += per
            num = 1

    s_new += str(num)
    return s_new