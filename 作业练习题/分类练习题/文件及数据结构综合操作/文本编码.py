



"""
test_w.txt 是用记事本编写的文本
这段代码表明 windows默认编码是GBK
"""
with open('test_w.txt', 'r', encoding='gbk') as f:
    print(f.read())

print('💎'.encode())
print('中'.encode())
print('ё'.encode())
print('a'.encode())

print(b'\xf0\x9f\x92\x83'.decode())
