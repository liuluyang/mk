


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

        self.__islogin = False

    def __login(self):
        """
        登陆
        :return:
        """
        account = input('请输入账户名：')
        passwd = input('请输入密码：')
        account_data = self.__balance()

        if account == account_data['account'] and passwd == account_data['passwd']:
            self.__islogin = True

    def __take_money(self):
        """
        取钱
        :return:
        """
        num = int(input('请输入金额：'))
        account_data = self.__balance()

        if num <= account_data['amount']:
            account_data['amount'] -= num
            self.__update_account(account_data)
            return True, '取款成功！'
        else:
            return False, '余额不足！'

    def __update_account(self, data):
        """
        更新账户信息
        :return:
        """
        with open('account', 'w') as f:
            json.dump(data, f)

    def __balance(self):
        """
        查询余额
        查看账户信息
        :return:
        """
        with open('account', 'r') as f:
            data = json.load(f)

        return data

    def __exit(self):
        """
        退出
        :return:
        """
        self.__islogin = False

    def make_account(self):
        """
        创建一个账户文件
        :return:
        """
        with open('account', 'w') as f:
            data = {'account':'123', 'passwd':'123456', 'amount':2000}
            json.dump(data, f)

    @property
    def islogin(self):
        """
        是否登陆
        :return:
        """
        return self.__islogin

    def main(self):
        """
        主函数
        :return:
        """

        check_dict = {'1':self.__take_money, '2':self.__balance, '3':self.__exit}
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
                self.__login()

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

        pass


if __name__ == '__main__':
    atm = ATM()
    # atm.test()
    atm.main()
