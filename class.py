import random
from copy import copy

global_cards = [
    {'value': 6, 'suite': 'A'},
    {'value': 6, 'suite': 'B'},
    {'value': 6, 'suite': 'C'},
    {'value': 6, 'suite': 'D'},
    {'value': 7, 'suite': 'A'},
    {'value': 7, 'suite': 'B'},
    {'value': 7, 'suite': 'C'},
    {'value': 7, 'suite': 'D'},
    {'value': 8, 'suite': 'A'},
    {'value': 8, 'suite': 'B'},
    {'value': 8, 'suite': 'C'},
    {'value': 8, 'suite': 'D'},
    {'value': 9, 'suite': 'A'},
    {'value': 9, 'suite': 'B'},
    {'value': 9, 'suite': 'C'},
    {'value': 9, 'suite': 'D'},
    {'value': 10, 'suite': 'A'},
    {'value': 10, 'suite': 'B'},
    {'value': 10, 'suite': 'C'},
    {'value': 10, 'suite': 'D'},
    {'value': 11, 'suite': 'A'},
    {'value': 11, 'suite': 'B'},
    {'value': 11, 'suite': 'C'},
    {'value': 11, 'suite': 'D'},
    {'value': 12, 'suite': 'A'},
    {'value': 12, 'suite': 'B'},
    {'value': 12, 'suite': 'C'},
    {'value': 12, 'suite': 'D'},
    {'value': 13, 'suite': 'A'},
    {'value': 13, 'suite': 'B'},
    {'value': 13, 'suite': 'C'},
    {'value': 13, 'suite': 'D'},
    {'value': 14, 'suite': 'A'},
    {'value': 14, 'suite': 'B'},
    {'value': 14, 'suite': 'C'},
    {'value': 15, 'suite': 'D'},
]

PARA = [[6, 6],[7, 7],[8, 8],[9, 9],[10, 10],[11 ,11],[12, 12],[13, 13],[14, 14]]
TWO_PARA = [[6,6,7,7], [6,6,8,8], [7,7,8,8], [6,6,9,9], [7,7,9,9], [8,8,9,9], [6,6,10,10], [7,7,10,10], [8,8,10,10], [9,9,10,10], [6,6,11,11], [7,7,11,11], [8,8,11,11], [9,9,11,11], [10,10,11,11], [6,6,12,12], [7,7,12,12], [8,8,12,12], [9,9,12,12], [10,10,12,12], [11,11,12,12], [6,6,13,13], [7,7,13,13], [8,8,13,13], [9,9,13,13], [10,10,13,13], [11,11,13,13], [12,12,13,13], [6,6,14,14], [7,7,14,14], [8,8,14,14], [9,9,14,14], [10,10,14,14], [11,11,14,14], [12,12,14,14], [13,13,14,14]]
SET_COMBINATION = [[6,6,6], [7,7,7], [8,8,8],[9,9,9], [10,10,10], [11,11,11], [12,12,12], [13,13,13], [14,14,14]]
STRIT = [[6,7,8,9,10], [7,8,9,10,11], [8,9,10,11,12], [9,10,11,12,13], [10,11,12,13,14]]

COMBINATIONS = PARA + TWO_PARA + SET_COMBINATION + STRIT

random.shuffle(global_cards)

def check(combination, open_cards):
    check = 0
    cloned_open_cards = copy(open_cards)
    for row in combination:
        if row in cloned_open_cards:
            check += 1
            cloned_open_cards.remove(row)
    return len(combination) == check

def check_combination(user_cards, open_cards):
    last_combination = None
    last_combination_index = None
    cards = [card['value'] for card in (user_cards + open_cards)]
    for index, combination in enumerate(COMBINATIONS):
        if check(combination, cards):
            last_combination = combination
            last_combination_index = index
    return {
        'combination': last_combination,
        'index': last_combination_index
    }

class Player:
    is_human = False
    name = ''
    cards = []
    open_cards = []

    def __init__(self, is_human, name=''):
        self.is_human = is_human
        if not is_human:
            name = random.choice(['Comp', 'Test', 'Check', 'All'])
        self.name = name

    def get_cards(self, cards):
        self.cards.append(cards.pop())
        self.cards.append(cards.pop())
        return cards


def main():
    user_cards = []
    user = Player(True, 'Dima')
    computer_1 = Player(False)
    computer_2 = Player(False)
    computer_3 = Player(False)
    computer_4 = Player(False)
    players = [user, computer_1, computer_2, computer_3, computer_4]

    global global_cards
    cards = global_cards

    print(len(cards))
    for player in players:
        cards = player.get_cards(cards)

    print(len(cards))

    for index in range(0, 3):
        for player in players:
            result = check_combination(player, open_cards)

        get_cards_len = 3 if index == 0 else 1
        for _ in range(0, get_cards_len):
            open_cards.append(cards.pop())
    result = check_combination(player, open_cards)

    for player in players:
        result = check_combination(player, open_cards)
        print('result: ', result['combination'])


if __name__ == '__main__':
    main()