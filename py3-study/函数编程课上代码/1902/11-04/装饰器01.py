



####################################### 闭包

address = ('192.168.1.1', 8000)

# 高阶函数
def outer(func):

    name = 'alex'
    print('this is outer', name)

    def inner():
        print("在inner里打印外层函数的变量", name)
        print(address)

    return inner  # 注意这里只是返回inner的内存地址，并未执行

# t = outer(lambda x:x)    # 发生闭包现象
# # print(t)
# t()


########################################## 装饰器 decorate


account = {
    'name': 'xx',
    'passwd':'xxy',
    'isVip':True
}

def check_vip(func):

    name = input('name:')
    passwd = input('passwd:')

    if name == account['name'] and passwd == account['passwd']:
        print('登陆成功')
        if account['isVip']:
            print('isVIp')
            # func()
            # return True
            return func
        else:
            print('is not Vip')
            return False
    else:
        print('登陆失败')
        return False

# check_vip()

def home():
    print("---首页----")

def other():
    print('-----免费专区----')

def america():
    # if not check_vip():
    #     return
    print("----欧美专区----")

def japan():
    # if not check_vip():
    #     return
    print("----日韩专区----")

def henan():
    # if not check_vip():
    #     return
    print("----河南专区----")



# other()
# america()

# check_vip(henan)
# henan()


def check_vip(func):

    # print('this is check vip')
    def inner():

        name = input('name:')
        passwd = input('passwd:')

        if name == account['name'] and passwd == account['passwd']:
            print('登陆成功')
            if account['isVip']:
                print('isVIp')
                func()
            else:
                print('is not Vip')
                return False
        else:
            print('登陆失败')
            return False

    return inner  # 注意这里只是返回inner的内存地址，并未执行


@check_vip
def ouzhou():

    print("----欧洲专区----")

# henan = check_vip(henan)
# #
# henan()
# ouzhou()


######################################## 时间装饰器



def check_time(func):

    def inner():

        start_time  = time.time()
        f = func()
        print(time.time() - start_time, '函数执行时间')

        return f

    return inner

import time


@check_time
def add():

    print('this is add')
    r = 1 + 1
    time.sleep(1)

    return r


# r = add()
# print(r)

# print(time.time())
#
# time.sleep(1)
# print(time.time())









