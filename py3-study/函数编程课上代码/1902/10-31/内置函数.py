



################################ abs
# 求绝对值

# print(abs(-123.1))

################################ all
# 判断所有元素是否为真

# print(all( [1, 2, []] ))
# print(bool(1 and 2 and []))

################################ any
# 判断至少有一个元素为真

# print(any( [1, 2, []] ))
# print(bool(1 or 2 or []))


################################ bin
# 把一个十进制的数转换成二进制的表示形式

# print(bin(100))

################################ oct
# 把一个十进制的数转换成八进制的表示形式

# print(oct(100))

################################ hex
# 把一个十进制的数转换成十六进制的表示形式

# print(hex(100))

################################ int
# 把整数数字字符串转换成整数 默认转换成十进制的数

# print(int('255'))
# print(int('255.11'))  # 错误
# print(int('11111111', base=2))
# print(int('ff', base=16))
# print(int(10.6))


################################ bool *
# 判断一个对象的真假

# print(bool(' '))


############################### callable
# 判断一个对象是否可调用

# print(callable(1))
# print(callable(lambda x:x))

############################### divmod *
# 计算两个数整除和取余的结果

# print(divmod(10, 2))

# print(divmod(10.5, 2))
# print(10.5 // 2)
# print(10.5 % 2)

############################### enumerate *
# 把一个对象的数据和索引同时计算出来

# for index, res in enumerate('abc', 10):
#     print(index, res)

# print(list(enumerate('abc', 10)))


############################### eval
# 可以把字符串形式的list,dict,set,tuple,再转换成其原有的数据类型

# r = eval('[1, 2, 3]')
# print(r, type(r))
# print(repr("[1, 2, 3]"), type('[1, 2, 3]'))

# print(eval('1 > 2'))

################################ exec
# 把字符串格式的代码，进行解义并执行

# exec('print("h")')

# exec('n = 11')
# print(n)


################################ filter *
# 筛选函数

# nums = filter(lambda x:x>5, range(10))
# print(list(nums))
#
# print([i for i in range(10) if i > 5])


################################ float * 可选
# 把整数或浮点字符串转换成浮点数

# print(float(10))
# print(10 * 1.0)
# print(float('10.11'))

################################ round
# 对浮点数进行四舍五入
# 当不指定保留几位小数时，会四舍五入为整数

# print(round(10.6671, 2))
# print(round(10.65, 1))

# print(round(10.995, 2))

################################ hash
# 哈希
# 不可变对象都可以被哈希

# for i in range(10):
#     print(hash('a'*100000))

# print(hash([]))

################################ id
# 查看对象的内存地址

# a = []
# b = []
# a.append(1)
# print(a, b)
#
# print(id(a))
# print(id(b))

# print(id([]))
# print(id([]))

################################ repr
# 查看字符串的原始形态

# print(repr('hello'))

################################ reversed
# 列表取反

# nums = [1, 2, 'a', 'b']
# print(list(reversed(nums)))

################################# pow
# 乘方计算

# print(pow(2, 5))
# print(2**5)

################################# slice
# 切片

# s = slice(0, 100, 2)
# print(['a', 'b', 'c', 1, 3, 3][0:100:2])
# print(['a', 'b', 'c', 1, 3, 3][s])

################################# sorted
# 排序

# nums = list(range(10))
# print(sorted(nums, reverse=True))
# print(nums)

################################# zip *
# 并行迭代

# a = [1,2,3,4]
# b = [4,5]
# c = [7,8,9]
# d = '12345'
#
# z = zip(a, b, c, d)
# print(list(z))


"""
int()
str()
list()
tuple()
set()
dict()

input()
print()

range(10)
enumerate('abc')
isinstance(1, int)
len('abc')
zip([1, 2, 3], 'abc')

filter(lambda x: x > 5, range(10))
map(lambda x:x*2, range(10))

round(10.11, 1)
"""

int()
str()
list()
tuple()
set()
dict()

input()
print()

range(10)
enumerate('abc')
isinstance(1, int)
len('abc')
zip([1, 2, 3], 'abc')

filter(lambda x: x > 5, range(10))
map(lambda x:x*2, range(10))

round(10.11, 1)
type(1)
