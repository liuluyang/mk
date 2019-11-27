

import hashlib, hmac, base64


"""
信息摘要算法
"""

"""
hashlib.md5() =》 获取MD5对象
update() =》添加加密的数据
注：加密的数据类型是字节
hexdigest() =》获取加密结果


输入任意长度的信息，经过处理，输出为128位的信息（数字指纹）；
这个结果在任何一个平台任何一门语言中，同一个对象的MD5值永远都是一样的。
不同的输入得到的不同的结果（唯一性）

压缩性：任意长度的数据，算出的MD5值的长度都是固定的
容易计算：从原数据计算出MD5值很容易
抗修改性：对原数据进行任何改动，修改一个字节生成的MD5值区别也会很大
强抗碰撞：已知原数据和MD5，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。

MD5不可逆的原因是其是一种散列函数，使用的是hash算法，在计算过程中原文的部分信息是丢失了的。
"""

# m = hashlib.md5()
# m.update('hello'.encode())
# m.update('world'.encode())
# r = m.hexdigest()
# print(r)
# m.update(''.encode())
# r2 = m.hexdigest()
# print(r2)
#
#
# m2 = hashlib.md5(('hello world'*1000000).encode())
# r2 = m2.hexdigest()
#
# print(r2)


############################################## sha256


# m3 = hashlib.sha512(('123456' + 'abc').encode())
# r3 = m3.hexdigest()

# print(r3, len(r3))


############################################## 加盐

# key = 'mk'
# passwd = 'helloworld'
# passwd_all = key + passwd
#
# m2 = hashlib.md5(passwd_all.encode())
# r2 = m2.hexdigest()
#
# print(r2)


############################################### hmac


# h = hmac.new(key.encode())
# h.update(passwd.encode())
# print(h.hexdigest())


############################################### base64



# 编码
b = base64.b64encode('hello'.encode())
print(b, type(b), len(b))

# 解码
print(base64.b64decode(b))



def encode_b64(string, encoding='utf8'):
    string = string.encode(encoding)
    print(string)
    oldstr = ''
    newstr = []
    base = ''
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    #把原始字符串转换为二进制，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in string:
        oldstr += '{:08}'.format(int(str(bin(i)).replace('0b', '')))
    print(oldstr, 6 - len(oldstr) % 6)
    #把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
    for j in range(0, len(oldstr), 6):
        newstr.append('{:<06}'.format(oldstr[j:j + 6]))
    print(newstr)
    #在base_list中找到对应的字符，拼接
    for l in range(len(newstr)):
        base += base64_list[int(newstr[l], 2)]
    #判断base字符结尾补几个‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return base


print(encode_b64('hello'))


