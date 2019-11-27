#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Date: 2019/7/14
from base64 import b64decode
from Crypto.Cipher import AES


b64 ={'nonce': 'GH0NhqPl2Csw0TZrbi/bzA==', 'header': 'aGVhZGVy', 'ciphertext': 'kIzFfW0U3w==', 'tag': 'vScsoRy2k0CX3IaDUDBgdg=='}


json_k = ['nonce', 'header', 'ciphertext', 'tag']

jv = {k: b64decode(b64[k]) for k in json_k}


key = b'\x08de#w\xe2\\\xee\x0e\xdam6\xec\xa4j\xcf'  # 这个就是前面的生成的密钥。

cipher = AES.new(key, AES.MODE_EAX, nonce=jv["nonce"])


cipher.update(jv["header"])
cipher.update(b'miller')

plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])

print(plaintext.decode())
