import pickle, json

"""
pickle/json模块学习
序列化和反序列化
"""

"""
pickle模块提供了四个功能：dumps、dump、loads、load
"""
def t():
    a = 1
    return a

def pickle_func():
    data = {'name':'xx', 'from':'xx', 'age':22}
    # data = t
    print('data:', data, type(data))
    # 转换
    data_dumps = pickle.dumps(data)
    print('data_dumps:',data_dumps, type(data_dumps))
    print('data_loads:', pickle.loads(data_dumps))
    # 写入
    with open('pickle_data', 'wb') as f:
        pickle.dump(data, f)
    # 取出
    with open('pickle_data', 'rb') as f:
        d= pickle.load(f)
        #　print(type(d), d)

"""
Json模块也提供了四个功能：dumps、dump、loads、load，用法跟pickle一致
json常用的方法：loads dumps
"""
def json_func():
    data = {'name':'xx', 'from':'xx', 'age':22}
    # data = [1, 2]
    # 转换
    data_dumps = json.dumps(data)
    print('data_dumps:',data_dumps, type(data_dumps))
    print('data_loads:', json.loads(data_dumps))
    # 写入
    with open('json_data', 'w') as f:
        json.dump(data, f)
    # 取出
    with open('json_data', 'r') as f:
        d= json.load(f)
        print(type(d), d)


if __name__ == '__main__':
    # pickle_func()
    # json_func()
    pass

    """
    JSON:

    优点：跨语言(不同语言间的数据传递可用json交接)、体积小

    缺点：只能支持int\str\list\tuple\dict

    Pickle:

    优点：专为python设计，支持python所有的数据类型

    缺点：只能在python中使用，存储数据占空间大
    """

