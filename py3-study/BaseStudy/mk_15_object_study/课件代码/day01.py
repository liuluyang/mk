
# import random
#
# num = random.randrange(1, 11)
# print('随机数已生成， 猜数游戏开始。。。')
# r = False
#
# for i in range(1, 4):
#     print('第%s次机会'%i)
#     n = int(input('请输入猜测的数字：'))
#     if n > num:
#         print('数猜大了')
#     elif n < num:
#         print('数猜小了')
#     else:
#         print('猜对了')
#         r = True
#         break
#     print('#'*20)
#
# if not r:
#     print('你要猜的数是%s'%num)
# print('游戏结束！')


##################################### 函数 ###########################################

def guess_num():

    import random
    num = random.randrange(1, 11)
    print('随机数已生成， 猜数游戏开始。。。')
    r = False

    for i in range(1, 4):
        print('第%s次机会' % i)
        n = int(input('请输入猜测的数字：'))
        if n > num:
            print('数猜大了')
        elif n < num:
            print('数猜小了')
        else:
            print('猜对了')
            r = True
            break
        print('#' * 20)

    if not r:
        print('你要猜的数是%s' % num)
    print('游戏结束！')

##################################### 面向对象 ##########################################

class BasePractice:

    def guess_num(self):
        """
        猜数游戏
        :return:
        """
        import random
        num = random.randrange(1, 11)
        print('随机数已生成， 猜数游戏开始。。。')
        r = False

        for i in range(1, 4):
            print('第%s次机会' % i)
            n = int(input('请输入猜测的数字：'))
            if n > num:
                print('数猜大了')
            elif n < num:
                print('数猜小了')
            else:
                print('猜对了')
                r = True
                break
            print('#' * 20)

        if not r:
            print('你要猜的数是%s' % num)
        print('游戏结束！')

bp = BasePractice()
bp.guess_num()
