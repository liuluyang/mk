



for i in range(1, 10):

    for y in range(1, i+1):
        print('%s * %s = %s '%(y, i, y*i), end='')

    # print('*'*10)
    print('')


# range(10)
# print(list(range(100000)))

# print()

# print('我是', end='')
# print('老王')

# print('我是', '老王', sep='-------------')


for i in range(1, 365):
    print('第%s天'%(i))

    num = 1
    for thing in ['吃饭', '睡觉', '打豆豆']:
        print(num, thing)
        num += 1

    print('*'*10)


for i in range(5, 10):
    for y in range(i, i + 6):
        print('%s * %s = %s '%(i, y, i*y), end='')
    print()