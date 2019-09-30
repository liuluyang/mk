import hashlib, hmac, base64

"""
讯息摘要演算法(数字签名)
c654c7d824358e9050b29041753dfba7
"""
h = 'c654c7d824358e9050b29041753dfba7'
# with open('comments.txt', 'r', encoding='utf8') as f:
#     text = f.read()
#     print(len(text.split('\n')), text.split('\n'))
#     hash_text = hashlib.md5(text.encode()).hexdigest()
#     hash_hmac = hmac.new(b'', text.encode(), 'md5').hexdigest()
#     print(hash_text, hash_text == h, len(hash_text))
#     print(hash_hmac)

key = b'f'      # 口令
message = b'abc'
r1 = hashlib.md5(key + message).hexdigest()
r2 = hmac.new(key, message, 'md5').hexdigest()
# print(r1, r2)

# base64
# print(base64.b64encode('hello'.encode()))
# print(base64.urlsafe_b64encode('hello'.encode()))
# print(base64.b64decode(b'aGVsbG8='))
