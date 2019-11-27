#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/7/14
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

# 1. 先获取一段用于加密和解密的密钥################
md = hashlib.md5(b'77b0b6eb-dc1e-45e7-b9b1-daef10f9c6cc')  # 自己指定一段用于加密的密钥
key = md.digest()

# key = get_random_bytes(16)  # 随机获取一段用于加密的密钥

# 这个密钥就是 长度为 128位的二进制流。 怎么得到无所谓, 有就好而且要保存好, 解密的时候也要用的。

# 2. 得到AES加密算法, EAX模式的一个 密码对象。
cipher = AES.new(key, mode=AES.MODE_EAX)


# 3. 盐值(salt) #####################
header = b"header"

cipher.update(header)   # 你可以理解为加了盐  salt
cipher.update(b'miller')   # 你可以理解为加了盐  salt

# 这个东西 可有可无，完全看需求来。
# ps 在加密时 加盐的顺序是啥，解密时也应该是啥。  否则就解不出来的。


# 4. 然后就可以加密数据了, 这个数据一般不会很大。 因为这毕竟是用来网络传输一些小数据的， 不是文件。

data = b"secrete"  # 这个就是你要进行加密的数据了。 注意这是二进制的数据。
ciphertext, tag = cipher.encrypt_and_digest(data)

# 5. 格式化处理以下。 搞成字典类型。 方便传到前端的时候，人家知道这是啥东西。
json_k = ['nonce', 'header', 'ciphertext', 'tag']
json_v = [b64encode(x).decode('utf-8') for x in [cipher.nonce, header, ciphertext, tag]]

# 在中间使用了 base64 格式化了一下
# Base64编码是从二进制到字符的过程，可用于在HTTP环境下传递较长的标识信息。采用Base64编码具有不可读性，需要解码后才能阅读。

# Base64作用
#
# 由于某些系统中只能使用ASCII字符。Base64就是用来将非ASCII字符的数据转换成ASCII字符的一种方法。
#
# base64特别适合在http，mime协议下快速传输数据。
#
# base64其实不是安全领域下的加密解密算法。虽然有时候经常看到所谓的base64加密解密。其实base64只能算是一个编码算法，对数据内容进行编码来适合传输。虽然base64编码过后原文也变成不能看到的字符格式，但是这种方式很初级，很简单。

# 6. json 转成字符串。然后你就 再专程二进制传输就Ok
result = json.dumps(dict(zip(json_k, json_v)))

print(result)
