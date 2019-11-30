# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/11 9:43


"""
属性：
    名字  生命值  攻击力
方法：
    攻击
    是否死亡
"""

class Hero:

    def __init__(self, name, hp, atk, words):

        self.name = name
        self.hp = hp        # 生命值
        self.atk = atk      # 攻击力
        self.words = words  #

    def attack(self, other):
        """
        攻击
        :return:
        """
        print(self.words)

        other.hp -= self.atk

    @property
    def isDead(self):
        """
        是否死亡
        :return:
        """
        if self.hp <= 0:
            print(self.words[::-1])
            return True

        return False





Raven = Hero('Raven', 480, 67, '断剑重铸之日，骑士归来之时！')
Galen = Hero('Galen', 580, 57, '德玛西亚！')
heros = [Raven, Galen]

# import time
# while True:
#     Raven.attack(Galen)
#     if Galen.isDead:
#         break
#     print(Galen.hp)
#     time.sleep(0.5)


import time
import random
while True:

    random.shuffle(heros)

    heros[0].attack(heros[1])
    if heros[1].isDead:
        break
    print('%s 剩余血量：'%heros[1].name, heros[1].hp)
    time.sleep(0.5)




