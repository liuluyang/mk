
import time
import random

for i in range(100):
    num = i%7 + 30
    print('\r\033[0;{num}m {} \033[0m'.format(i, num=num), end='')
    time.sleep(0.05)


def set_color(s):

    return '\033[1;%sm%s\033[0m'%(random.randrange(30, 38), s)

print('\033[1;33m你好\033[0m\033[1;32m你好\033[0m')


for i in range(20):
    if i % 2 == 1:
        s = '\033[1;%sm%s\033[0m'%(i%7 + 30,'*'*i)
        print(s.center(40))
for i in range(18, 0, -1):
    if i % 2 == 1:
        s = '\033[1;%sm%s\033[0m'%(i%7 + 30,'*'*i)
        print(s.center(40))

for i in range(20):
    if i % 2 == 1:
        s = ''.join([set_color('*') for i in range(i)])
        print(' '*((28 - i)//2), s, set_color(str(len(s))))


while True:
    s = ''.join([set_color('*') for i in range(random.randrange(1, 100))])
    print(s)
    time.sleep(0.1)