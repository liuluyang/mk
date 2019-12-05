# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liuluyang"
# Datetime: 2019/12/3 10:38



class OpenNew:


    def __enter__(self):
        """
        进入
        :return:
        """
        # print('进入')

        self.f = open('test.txt', 'rb')

        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        结束

        如果with语句里面出现异常
        返回值的bool如果是False,异常正常传递
        返回值的bool如果是True,异常不会抛出

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        # print('结束')
        self.f.close()

        # 参数类型
        print('exc_type:', exc_type)
        print('exc_val:', exc_val, type(exc_val), str(exc_val))

        # if isinstance(exc_val, TypeError):
        #     print('!!!!!!!!!!!!!')
        #     return True

        return True


op = OpenNew()


with OpenNew() as f:
    # print(f)
    # print('其他的操作')
    # raise TypeError('类型错误')
    f.write('a')
    pass

# print(f.closed)
# print('结束之后')


# f = open('test.txt', 'rb')
# print(f.read())
# f.close()
# print(f.closed)

# with open('test.txt', 'rb') as f:
#     # print(f.read())
#     # print(f.closed)
#     pass
#     f.write('a')

# print(f.closed)