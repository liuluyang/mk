# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/11 14:27


"""
ATM:
    属性：
        是否登录

    方法：
        登录 login

        取钱
        查询余额
        退出

d = {"username": "xiaobai", "password": "xiaohei", "amount": 2000}
"""
import json

class ATM:

    def __init__(self):
        self.__is_login = False

    def __login(self):
        """
        登录
        :return:
        """
        username = input('username:')
        password = input('password:')
        data = self.__amount()
        if username == data['username'] and password == data['password']:
            self.__is_login = True

    def __take_money(self):
        """
        取钱
        :return:
        """
        money = int(input('请输入取款金额:'))

        if self.__amount()['amount'] >= money:
            self.__update_account(money)
            # print('取款成功!')
            return True, '取款成功!'

        # print('余额不足！')
        return False, '余额不足！'

    def __update_account(self, money, is_out=True):
        """
        更新账户余额
        :param money:
        :return:
        """
        data = self.__amount()
        with open('账户', 'w') as f:
            money = money if is_out else -money
            data['amount'] -= money
            # if is_out:
            #     data['amount'] -= money
            # else:
            #     data['amount'] += money
            json.dump(data, f)

    def __amount(self):
        """
        查询账户信息
        :return:
        """
        with open('账户', 'r') as f:
            data = json.load(f)
            # print(data, type(data))

        return data

    def __exit(self):
        """
        退出
        :return:
        """
        self.__is_login = False

    def main(self):
        """
        主函数
        :return:
        """
        data = {'1':self.__amount, '2':self.__take_money, '3':self.__exit}
        text = """
        查询余额：1
        取款：    2
        退出：    3    
        """

        while True:
            # 如果登录进入内层循环
            if not self.__is_login:
                self.__login()
                continue

            while True:
                # 如果退出登录
                if not self.__is_login:
                    break
                print(text)
                order = input('请输入指令：')
                func = data.get(order)
                if func:
                    result = func()
                    if result:
                        print(result)

    def test(self):

        # print(self.__amount())
        while True:
            if self.__is_login:

                while True:
                    if not self.__is_login:
                        break
                    print('ok')
                    pass

            self.__login()



if __name__ == '__main__':
    atm = ATM()
    # atm.test()
    # atm.main()