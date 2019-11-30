



"""
继承练习：
    重用父类方法
"""

class ListNew(list):

    def __init__(self, seq=()):

        for per in seq:
            if isinstance(per, int) or (isinstance(per, str) and per.isdigit()):
                raise TypeError('类型错误')

        super().__init__(seq)

    def append(self, obj):

        print(obj, 'append_new')

        # self.append(obj) # 递归调用

        # 重新调用父类的方法
        # list.append(self, obj)

        if not isinstance(obj, int):
            super().append(obj)
        else:
            raise TypeError('类型错误')


lst = ListNew(['a', 'b', [1, 1]])
print(lst)
lst.append('a')
print(lst)
