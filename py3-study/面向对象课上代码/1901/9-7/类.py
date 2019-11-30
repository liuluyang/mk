# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/7 13:44

"""--"""

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__, self.name)
    # self.__class__ 可以得到当前 实例对象 由那个类实例化得到的。


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")


class CharField(Field):
    def __init__(self, name):
        super(CharField, self).__init__(name, "varchar(32)")


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        '''
        :param cls:   当前准备创建类的对象
        :param name:  当前类的名字
        :param bases:  当前类集成的父类的集合 (mro) 新式类广度优先
        :param attrs:  类方法的集合(以键值对的方式保存, 之后使用  " .__dict__" 可以获取到所有的方法)
                attrs中有的方法都最终成为 实例对象的一个方法 或者 属性
        :return:
        '''
        if name == "Model":  # 不对Model这个类做任何的改动, 直接返回
            return type.__new__(cls, name, bases, attrs)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)
        # self.name = "miller"

    def __setattr__(self, key, value):
        self[key] = value
        # self.__dict__[key] = value  # 这种方式添加的时候, 实例对象的 __dict__ 中才有 初始化函数中定义的值

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'model' has no attribute %s" % item)

    def save(self):
        # print(self.__class__.__dict__)
        # print(self.__class__)
        # print(self)
        # print(self.__table__)
        table = self.__table__
        columns = []
        params = []
        print(self.__mappings__)
        for k, v in self.__mappings__.items():

            res = self.get(k, None)
            # self 由于继承了字典, 元类中通过 __setattr__ 将 key和value 保存了起来, 所以通过 .get() 的方式取值
            columns.append(v.name)
            params.append(str(res) if not isinstance(res, str) else res)

        sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, ",".join(columns), ",".join(params))
        print(sql)


class User(Model):
    # 类中定义的所有的属性, 都会通过 Metaclass 中的 __new__ 方法，进行处理。
    # 并且所有的方法, 都会在 attrs 中有体现。 包括以下的类
    id = IntegerField("nid")
    name = CharField("username")
    # 字段类中的 名字是真实的数据的字段名字。


# User类中指定的key 需要和 User类中, 字段类的对象名相同。
p = User(id=1, name="miller")

p.save()





