
import random



# 上下文管理器 自动关闭文件

with open('我的名字.txt', 'w', encoding='utf8') as f:
    # for i in range(100):
    #     f.write('晓明\n')
    f.write('晓明\n'*100)


with open('车牌号.txt', 'r', encoding='utf8') as f:
    cards = f.read().split()
    nums = 0
    for card in cards:
        if '6' in card:
            nums += 1

    print(len(cards), nums)


######################################################### 查找替换

# 查找

with open('车牌号.txt', 'r', encoding='utf8') as f: # 打开文件

    data = f.read()                                 # 读取内容

    # while True:
    check_text = input('请输入你要查找的内容：')    # 接收输入
    check_nums = data.count(check_text)             # 统计匹配到的内容个数
    print(data.replace(check_text, '\033[1;%sm%s\033[0m'%(random.randint(31, 36), check_text)))
    print('找到%s个'%check_nums)

# 修改

with open('车牌号.txt', 'w', encoding='utf8') as f: # 打开文件

    check_new = input('请输入你要修改的内容：')    # 接收输入

    data_new = data.replace(check_text, check_new) # 替换

    f.write(data_new)                               # 写入

    print('修改完成')

