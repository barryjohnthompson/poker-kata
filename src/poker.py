from itertools import product
from random import shuffle

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'S', 'C')

HAND_TYPES = (
        'High Card',
        'Pair',
        'Two Pairs',
        'Three of a Kind',
        'Straight',
        'Flush',
        'Full House',
        'Four of a Kind',
        'Straight Flush',
        'Royal Flush'
)

class Card:
    def __init__(self, value, suit):
        value = str(value)
        suit = str(suit)
        if value not in VALUES:
            raise ValueError
        self.value = value
        if suit not in SUITS:
            raise ValueError
        self.suit = suit

    def __repr__(self):
        return '<Card object {}{}>'.format(self.value, self.suit)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value_index < other.value_index

    def __gt__(self, other):
        return self.value_index > other.value_index

    @property
    def value_index(self):
        return VALUES.index(self.value)


class PokerHand:
    def __init__(self, cards):
        if any(not isinstance(card, Card) for card in cards):
            raise ValueError
        if len(cards) != 5:
            raise ValueError
        card_set = {repr(card) for card in cards}
        duplicate_cards = len(card_set) < len(cards)
        if duplicate_cards:
            raise ValueError
        self.cards = sorted(cards)

    def __repr__(self):
        return '<PokerHand object {}>'.format(', '.join(str(card) for card in self))

    def __iter__(self):
        return iter(self.cards)

    def __gt__(self, other):
        return self.cards[-1] > other.cards[-1]

    def __lt__(self, other):
        return self.cards[-1] < other.cards[-1]

    def __eq__(self, other):
        return self.cards[-1] == other.cards[-1]

    @property
    def hand_type(self):

        dic = {
            'H':0,
            'D':0,
            'S':0,
            'C':0
        }
        val_dic = {
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            'T': 0,
            'J': 0,
            'Q': 0,
            'K': 0,
            'A': 0
        }
        all_same_suit = False
        #this loops through each card in the hand
        for n in range(len(self.cards)):
            # increment the counter for the suit of card[n]
            dic[self.cards[n].suit] += 1

        for n in range(len(self.cards)):
            # increment the counter for the value of card[n]
            val_dic[self.cards[n].value] += 1

        # royal flush?
        if max(dic.values()) == 5 and self.cards[-1].value == 'A' and self.cards[0].value == 'T':
            return 'Royal Flush'

        # straight Flush
        lowest_value = self.cards[0].value
        lowest_index = VALUES.index(lowest_value)

        if max(dic.values()) == 5 and self.cards[-1].value == VALUES[lowest_index + 4]:
            return 'Straight Flush'

        # Flush
        if max(dic.values()) == 5 and self.cards[-1].value != VALUES[lowest_index + 4]:
            return 'Flush'

        # four of a Kind
        if max(val_dic.values()) == 4:
            return 'Four of a kind'

        # full House
        if 3 in val_dic.values() and 2 in val_dic.values():
            return 'Full house'

        # straight
        if self.cards[-1].value == VALUES[lowest_index + 4]:
            return 'Straight'

        # Three of a kind
        if 3 in val_dic.values() and 2 not in val_dic.values():
            return 'Three of a kind'

        # Two Pair or pair
        pair_count = 0
        for k, v in val_dic.items():
            # increment the counter for the value of card[n]
            if val_dic. == 2:
                pair_count += 1

        if pair_count == 2:
            return 'Two pair'
        #if pair_count == 1:
        #    return 'Pair'



def create_deck():
    cards = [Card(value, suit) for value, suit in product(VALUES, SUITS)]
    shuffle(cards)
    return cards

def deal_hand(n, deck):
    return [deck.pop() for i in range(n)]
