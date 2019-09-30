import redis
import time
import json


r = redis.Redis(password='redis', db=0, decode_responses=True)

def listen_01():
    """
    阻塞模式
    :return:
    """
    print(r.ping())
    sub = r.pubsub()
    sub.psubscribe(['chat'])
    for item in sub.listen():
        print(item)


def listen_02():
    """
    非阻塞监听
    :return:
    """
    sub = r.pubsub()
    sub.psubscribe(['chat'])
    num = 0
    while True:
        item = sub.get_message()
        if item:
            print(item)
        num += 1
        print(num)
        time.sleep(1)

if __name__ == '__main__':
    # listen_01()
    # listen_02()
    pass