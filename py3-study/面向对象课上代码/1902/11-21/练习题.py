


def check_id_card(idcard):
    """
    身份证号验证
    :param idcard:
    :return:
    """

    # 数据处理
    nums = idcard[:-1]
    valid_code = idcard[-1]         # 获取最后一位校验码
    if not nums.isdigit() or len(idcard) != 18:
        return False, '号码位数不对或数据类型错误'

    coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 系数
    last_nums = '10X98765432'                                            # 最后一位数

    index = sum(map(lambda x:int(x[0])*x[1] ,zip(nums, coefficient))) % 11  # 取模

    if valid_code == last_nums[index]:
        return True

    return False


def check(idcard):

    return idcard[-1] == '10X98765432'[sum(map(lambda x: int(x[0]) * x[1],zip(idcard[:-1],[7, 9, 10, 5, 8, 4, 2, 1, 6,3, 7, 9, 10, 5, 8, 4,2]))) % 11]



if __name__ == '__main__':
    r = check_id_card('151651561551544415')
    print(r)
    print(check('151651561551544415'))