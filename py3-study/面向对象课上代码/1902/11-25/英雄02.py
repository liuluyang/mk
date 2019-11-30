


"""
Hero
英雄：
    属性：
        名字、生命值、攻击力、座右铭
    方法：
        攻击
"""

class Hero:

    def __init__(self, name, hp, atk, words):

        self.name = name
        self.__hp = hp
        self.__atk = atk
        self.words = words

    def attack(self, other):
        """
        攻击
        :return:
        """
        print(self.words)

        # 生命值减少
        # print(other, other.__hp)
        other.__hp -= self.__atk

    @property
    def isDead(self):
        """
        是否死亡
        :return:
        """

        return self.__hp <= 0

    @property
    def info(self):
        """
        查看所有属性
        :return:
        """

        return self.name, self.__hp, self.__atk

################################################

galen = Hero('盖伦', 560, 60, '德玛西亚！')
sword = Hero('剑圣', 480, 80, '你的剑就是我的剑！')

import time
import random

# while True:
#     galen.attack(sword)
#     print(sword.info)
#     if sword.isDead:
#         break
#     time.sleep(1)


heros = [galen, sword]


while True:

    random.shuffle(heros)
    heros[0].attack(heros[1])
    print(heros[1].info)
    if heros[1].isDead:
        print(heros[1].words[::-1])
        break

    time.sleep(1)










