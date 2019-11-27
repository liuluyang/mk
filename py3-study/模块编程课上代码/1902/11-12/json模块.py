
import json
import pickle

"""
pickle/json模块学习
序列化和反序列化

常用方法 转换网络json数据**
Json模块也提供了四个功能：dumps、dump、loads、load
json常用的方法：loads dumps
"""

# s = '{"name":"xx"}'
# s = s.encode()
# print(s)

############################################# loads dumps
def f():
    pass

def test_01():

    # 把字典 => 字符串
    json_str = json.dumps({"name":'xx'})
    # print(json_str, type(json_str))
    json_b = json_str.encode()
    # print(json_b)

    # 字节码 => 字符串 => 字典
    # json_b = s
    new_str = json_b.decode()
    # print(new_str, type(new_str))
    data = json.loads(new_str)
    # print(data, type(data))
# test_01()

########################################### load dump

def test_02():

    # 把字典 =》写入文件
    with open('test', 'w') as f:
        json.dump({"name":'xx', 'age':11}, f)

    #
    # with open('test', 'rb') as f:
    #     data = f.read().decode()
    #     print(data, type(data))
    #     print(type(json.loads(data)))

    # 把文件数据 =》字典
    with open('test', 'r') as f:
        data = json.load(f)
        print(data, type(data))


############################################### pickle


############################################# loads dumps

def func():
    pass

def test_03():

    # 把python对象 => 字节
    pickle_b = pickle.dumps(test_01)
    print(pickle_b, type(pickle_b))

    # 字节码 => python对象
    obj = pickle.loads(pickle_b)
    print(obj, type(obj))

# test_03()


########################################### load dump

"""
以二进制方式 读取 写入文件
"""

def test_04():

    # 把python对象 =》写入文件
    with open('test_pickle', 'wb') as f:
        pickle.dump(test_03, f)
    # 把文件数据 =》python对象
    with open('test_pickle', 'rb') as f:
        data = pickle.load(f)
        print(data, type(data), data())

# test_04()


"""
    JSON:

    优点：跨语言(不同语言间的数据传递可用json交接)、体积小

    缺点：只能支持int\str\list\tuple\dict

    Pickle:

    优点：专为python设计，支持python所有的数据类型

    缺点：只能在python中使用，存储数据占空间大
    """