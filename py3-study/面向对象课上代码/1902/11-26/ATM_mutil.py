


"""
账户信息：
    {'account':'123', 'passwd':'123', 'amount':10000}

ATM:
    属性：
        __islogin
    方法：
        私有：
            __login        登陆
            __take_money   取钱
            __balance      查询余额
            __exit         退出

            save_money    存钱
            make_account   创建账户

        main         主函数

主函数：
    未登陆 请登录

    请选择功能：
        取钱    =》 取钱金额  =》 余额判断
        查看余额
        退出

"""
import json

class ATM:

    def __init__(self):

        self.islogin = False

    def login(self):
        """
        登陆
        :return:
        """
        account = input('请输入账户名：')
        passwd = input('请输入密码：')
        self.account = account

        account_data = self.balance()

        if account == account_data['account'] and passwd == account_data['passwd']:
            self.islogin = True

    def take_money(self):
        """
        取钱
        :return:
        """
        num = int(input('请输入金额：'))
        account_data = self.balance()

        if num <= account_data['amount']:
            account_data['amount'] -= num
            self.update_account(account_data)
            return True, '取款成功！'
        else:
            return False, '余额不足！'

    def update_account(self, data):
        """
        更新账户信息
        :return:
        """
        import os

        with open(os.path.join('info', self.account), 'w') as f:
            json.dump(data, f)

    def balance(self):
        """
        查询余额
        查看账户信息
        :return:
        """
        import os
        if self.account not in set(os.listdir('info')):

            return False, '账户不存在'

        with open(os.path.join('info', self.account), 'r') as f:
            data = json.load(f)

        return data

    def exit(self):
        """
        退出
        :return:
        """
        self.islogin = False

    def make_account(self):
        """
        创建一个账户文件
        :return:
        """
        with open('account', 'w') as f:
            data = {'account':'123', 'passwd':'123456', 'amount':2000}
            json.dump(data, f)

    def main(self):
        """
        主函数
        :return:
        """

        check_dict = {'1':self.take_money, '2':self.balance, '3':self.exit}
        info = """
        ####################
            可选择操作：
            1、取钱
            2、查询余额
            3、退出
        ####################
        """

        while True:

            if self.islogin:
                print(info)
                num = input('请输入指令：').strip()
                method = check_dict.get(num)
                if method:
                    r = method()
                    if r:
                        print(r)
            else:
                self.login()

    def test(self):
        """
        功能测试
        :return:
        """

        # self.make_account()
        # self.__balance()
        # self.__login()
        # print(self.__islogin)
        # print(self.__take_money())
        # self.save_money()
        print(self.make_account())
        pass


class AtmMutil(ATM):


    def save_money(self):
        """
        存钱
        :return:
        """
        num = int(input('请输入金额：'))

        account = self.balance()
        account['amount'] += num
        self.update_account(account)

        return True, '存款成功'

    def make_account(self):
        """
        创建一个账户
        :return:
        """
        import os
        account = input('请输入账户名：')
        passwd = input('请输入密码：')
        passwd_02 = input('请再次输入密码：')
        account_names = set(os.listdir('info'))
        if account in account_names:

            return False, '用户已存在'

        if account.strip() and passwd.strip() and passwd == passwd_02:

            with open(os.path.join('info', account), 'w') as f:
                data = {'account':account, 'passwd':passwd, 'amount':0}
                json.dump(data, f)

                return True, '账户创建成功'

    def main(self):
        """
        主函数
        :return:
        """

        check_dict = {'1':self.take_money, '2':self.save_money ,'3':self.balance, '4':self.exit}
        info = """
        ####################
            可选择操作：
            1、取钱
            2、存钱
            3、查询余额
            4、退出
        ####################
        """

        while True:

            if self.islogin:
                print(info)
                num = input('请输入指令：').strip()
                method = check_dict.get(num)
                if method:
                    r = method()
                    if r:
                        print(r)
            else:
                print('########\n'
                      '1、注册\n'
                      '2、登陆\n'
                      '#########\n')
                num = input('请输入指令：')
                if num == '1':
                    print(self.make_account())
                elif num == '2':
                    print(self.login())


if __name__ == '__main__':
    # atm = ATM()
    # atm.test()
    # atm.main()

    atm = AtmMutil()
    atm.main()
    # atm.test()

