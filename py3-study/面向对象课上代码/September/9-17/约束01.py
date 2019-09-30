# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/17 15:28

class PayBase:

    def pay(self, money):

        raise RuntimeError('请实现这个方法')


class QQpay:

    def pay(self,money):
        print('使用qq支付%s元' % money)

class Alipay:

    def pay(self,money):
        print('使用支付宝支付%s元' % money)

class Wachat(PayBase):

    def zhifu(self, money):
        print('使用微信支付%s元' % money)

    def pay(self, money):
        self.zhifu(money)

# a = Alipay()
# a.pay(100)
# b = QQpay()
# b.pay(200)

# w = Wachat()

def main(obj):
    obj.pay(100)

# main(w)