#coding:utf8

import base64
# from this import s
import uuid
from uuid import uuid1
import copy


"""
uuid.uuid1()　　基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性。

MAC地址：网卡唯一标识
"""
def get_uuid():
    uid = uuid1()

    return uid


def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]

    return ":".join([mac[e:e+2] for e in range(0,11,2)])


"""
python之禅
"""
def py_zen():
    from this import s
    # s = copy.deepcopy(s)
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    s = "".join([d.get(c, c) for c in s])

    translate_s = """
    Tim Peters的Python之禅
    
    美丽胜过丑陋。
    显式优于隐式。
    简单比复杂更好。
    复杂比杂乱更好。
    扁平优于嵌套。
    稀疏优于密集。
    可读性很重要。
    特殊情况不足以打破规则。
    虽然实用性胜过纯洁。
    错误不应该默默地传递。
    除非明确沉默。
    面对模棱两可，拒绝猜测的诱惑。
    应该有一个 - 最好只有一个 - 明显的方法来做到这一点。
    虽然这种方式起初可能并不明显，除非你是荷兰人。
    现在比永远好。
    虽然现在永远不会比*正确好。
    如果实施很难解释，这是一个坏主意。
    如果实现很容易解释，那可能是个好主意。
    命名空间是一个很棒的主意 - 让我们做更多的事情吧！
    
    """
    # print(translate_s.encode())
    # encode_s = base64.b64encode(translate_s.encode())
    # print(len(encode_s), encode_s)
    # print(base64.b64decode(encode_s).decode())

    s_list = [s for s in s.split('\n') if s.strip()]
    translate_s_list = [s for s in translate_s.split('\n') if s.strip()]

    for s_line in s_list:
        print(s_line)
        print()

    for s_line in translate_s_list:
        print(s_line)
        print()

    for s_line in zip(s_list, translate_s_list):
        print(s_line)
        print()


if __name__ == '__main__':
    # print(get_uuid())
    # mac_id = get_mac_address()
    # print(mac_id)
    pass
