# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/11/28 10:49

class Payment:
    """
    此类什么都不做，就是制定一个标准，谁继承我，必须定义我里面的方法。
    """
    def pay(self,money):

        raise Exception("你没有实现pay方法")


class QQpay:

    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:

    def pay(self,money):
        print('使用支付宝支付%s元' % money)

class Wechatpay(Payment):  # 野生程序员一般不会看别人怎么写，自己才是最好，结果......

    def zhifu(self, money):
        print('使用微信支付%s元' % money)

    def pay(self, money):

        # self.zhifu(money)
        pass


a = Alipay()
# a.pay(100)
b = QQpay()
# b.pay(200)
w = Wechatpay()
# w.zhifu(100)


def main_pay(obj, money):

    # 支付的前后可以做一些日志的记录

    obj.pay(money)


# main_pay(w, 200)