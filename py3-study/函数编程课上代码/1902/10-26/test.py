
import time


for i in range(1, 101):
    print('\r', '*'*i, '%%%s'%i, end='')
    time.sleep(0.1)
