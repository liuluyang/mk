

"""
取出文件最后一行
"""

f = open('我的作品.txt', 'rb')

index_ = -50
while True:
    f.seek(index_, 2)
    lines = f.readlines()
    print(lines)
    if len(lines) > 1:
        print(lines[-1].decode())
        break
    else:
        index_ -= 50