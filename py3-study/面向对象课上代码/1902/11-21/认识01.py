




def func():

    print('xxxxxx')


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


# print(guess_num)
# guess_num()


def func_t():

    pass

################################################ 定义一个类以及调用

# 类的定义  class(类)
# 定义类名：首字母大写

class BasePractice:

    pass

# print(func_t)        # <function func_t at 0x00000000027B96A8>
# print(BasePractice)  # <class '__main__.BasePractice'>


class Guess:

    def guess_num(self):

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

    def name(self):

        print('老王')


# Guess.guess_num()
# Guess   <class '__main__.Guess'>

# 类里面方法的调用
# g = Guess()         # <__main__.Guess object at 0x00000000027580B8>
# g.guess_num()       # 调用类里面的函数
# print(g)


g = Guess()
g.name()


s = str(111111232324)
print(s.count('1'))





















