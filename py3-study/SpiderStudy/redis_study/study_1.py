
import redis
import json
import time

"""连接"""

# r = redis.Redis(password='redis')
# print('连接对象：', r)

# pool = redis.ConnectionPool(password='redis')
# r2 = redis.Redis(connection_pool=pool)
# print('连接对象：', r2)

s = """
致橡树

我如果爱你
绝不学攀援的凌霄花
借你的高枝炫耀自己

我如果爱你
绝不学痴情的鸟儿
为绿荫重复单调的歌曲
"""

"""写入字符串数据"""
# for i in range(100):
#     r.set(i, s)
#     print(i)
"""获取字符串数据"""
# data = r.get(1)
# print(len(data), data)
#print(r.mget(1, -10))
"""删除键"""
# r.delete('a')

"""
检查key是否存在
"""
# print(r.exists(1))
"""
对key设置过期时间
"""
# r.set('a', 'hello')
# r.expire('a', 10)
# while True:
#     data = r.get('a')
#     print(data)
#     if not data:
#         break
#     time.sleep(1)

"""
随机返回一个key
"""
# print(r.randomkey())
#############################################################

"""
向列表插入值
"""
r = redis.Redis(password='redis', db=1, decode_responses=True)
# for i in range(100):
#     r.rpush(1, i)
# r.rpush(1, *list(range(100, 200)))

"""
列表取值
"""
# print(r.lrange(1, 0, 10))
# print(r.lindex(1, 0))
# print(r.lpop(1))
# print(r.rpop(1))
"""
获取列表长度
"""
#　print(r.llen(1))

##############################################################
"""
向集合中添加元素
"""
# for i in range(100):
#     r.sadd(2, i)
# r.sadd(2, *list(range(200)))
"""
判断一个元素是否在集合中
"""
# print(r.sismember(2, 10))
"""
获取集合所有元素
"""
# print(r.smembers(2))
"""
移除元素
"""
# print(r.srem(2, 100))
"""
获取元素总数
"""
# print(r.scard(2))

#########################################################
"""
有序集合
"""
import string
# for a, score in zip(string.ascii_lowercase, range(26)):
#     r.zadd(3, {a:score})

# print(r.zcard(3))
# print(r.zcount(3, 1, 10))
# print(r.zrank(3, 'aa'))
# print(r.zrangebyscore(3, 20, 30))
# print(r.zscore(3, 'z'))
#r.zadd(3, {'z':200})

#########################################################
"""
哈希
"""
"""
添加元素
"""
# for a, score in zip(string.ascii_lowercase, range(26)):
#     r.hset(4, a, score)
# r.hmset(4, {'name':'xx', 'age':20, 'data':json.dumps({'a':1})})

"""
获取元素
"""
# print(r.hgetall(4))
# print(r.hget(4, 'a'))
"""
删除元素
"""
# print(r.hdel(4, 'a'))

#############################################################
"""
获取所有key
"""
# print(r.keys())
"""
获取key的类型
"""
# print(r.type(1))