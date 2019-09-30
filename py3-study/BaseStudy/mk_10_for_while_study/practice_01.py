
import random
import string


"""
1.随机生成十组不相同车牌号
2.车牌号长度是5
3.必须包含大写字母和数字
4.给出限号号码，找出限号车牌号
5.限号规则：
 从最后一位倒着找，如果是字母跳过，如果是数字就进行是否限号的判断
"""

params = string.ascii_uppercase + '0123456789'
cards = set()
nums = [3, 8]
print(params)


while len(cards) < 10:
    card = ''
    for i in range(5):
        card += random.choice(params)
    if not card.isdigit() and not card.isalpha():
        print(card, '符合')
        cards.add(card)
    else:
        print(card, '不符合')

print(cards)

for card in cards:
    for c in card[::-1]:
        if c.isdigit():
            if int(c) in nums:
                print('被限号车牌：', card)
            break


