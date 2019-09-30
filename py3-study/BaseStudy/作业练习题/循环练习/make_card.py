import random
import string

params = string.ascii_uppercase + string.digits


def make_cards():
    cards = ''
    for _ in range(20):
        card = ''
        for i in range(5):
            card += random.choice(params)
        cards += card + ' '
    cards += '\n'
    return cards


def make_cards_file():

    with open('车牌号.txt', 'a', encoding='utf8') as f:
        for _ in range(50):
            cards = make_cards()
            f.write(cards)


if __name__ == '__main__':
    make_cards_file()
