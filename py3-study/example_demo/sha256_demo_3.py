#coding:utf8

import hashlib


"""
加密
"""
data = {
    'name':'liu',
    'password':'123456'
}
print(data)

password = data['password']

hash_password = hashlib.sha256(password.encode()).hexdigest()

data['password'] = hash_password

print(data)
