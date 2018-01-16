from poker import Card, PokerHand, create_deck, deal_hand

# some useful card suit/value constants
T = 'T'
J = 'J'
Q = 'Q'
K = 'K'
A = 'A'
H = 'H'
D = 'D'
S = 'S'
C = 'C'
# you can use integers for the others (but not 10 - use T)

# test single card
card_1 = Card(A, S)
card_2 = Card(A, D)
assert card_1 == card_2
card_3 = Card(K, S)
assert card_1 != card_3
assert card_1 > card_3
assert not card_1 < card_3

# test comparing two poker hands
# test for highest card
cards = [Card(v, s) for v, s in [(A, S), (2, D), (4, C), (7,  H), (K, S)]]
hand_1 = PokerHand(cards)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
assert hand_1 == hand_2
assert hand_2 == hand_1

cards = [Card(v, s) for v, s in [(A, S), (2, D), (4, C), (7,  H), (K, S)]]
hand_1 = PokerHand(cards)
cards = [Card(v, s) for v, s in [(Q, S), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
assert hand_1 > hand_2
assert hand_2 < hand_1

# test comparing two poker hands
# test for royal flush
cards = [Card(v, s) for v, s in [(T, S), (J, S), (Q, S), (K,  S), (A, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
#cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
#hand_2 = PokerHand(cards)
# assert hand_1 == hand_2
# assert hand_2 == hand_1

# test comparing two poker hands
# test for straight flush
cards = [Card(v, s) for v, s in [(4, S), (5, S), (6, S), (7,  S), (8, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
# assert hand_1 == hand_2
# assert hand_2 == hand_1

# test comparing two poker hands
# test for a flush
cards = [Card(v, s) for v, s in [(4, S), (9, S), (Q, S), (7,  S), (2, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
#assert hand_1 == hand_2
#assert hand_2 == hand_1

# test comparing two poker hands
# test for four of a kind
cards = [Card(v, s) for v, s in [(5, S), (5, C), (5, H), (5,  D), (2, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
#assert hand_1 == hand_2
#assert hand_2 == hand_1

# test for full house
cards = [Card(v, s) for v, s in [(5, S), (5, C), (5, H), (8,  D), (8, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
#assert hand_1 == hand_2
#assert hand_2 == hand_1

# test for a straight
cards = [Card(v, s) for v, s in [(5, S), (8, C), (7, H), (6,  D), (9, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
#assert hand_1 == hand_2
#assert hand_2 == hand_1

# test for three of a kind
cards = [Card(v, s) for v, s in [(8, S), (8, C), (8, H), (6,  D), (9, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
#assert hand_1 == hand_2
#assert hand_2 == hand_1

# test for two pair
cards = [Card(v, s) for v, s in [(8, S), (8, C), (6, H), (6,  D), (9, S)]]
hand_1 = PokerHand(cards)
print(hand_1.hand_type)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
#assert hand_1 == hand_2
#assert hand_2 == hand_1

# test creating a deck
deck = create_deck()
assert len(deck) == 52
assert all(isinstance(card, Card) for card in deck)

# test creating a hand from the deck
cards = deal_hand(5, deck)
hand_1 = PokerHand(cards)
cards = deal_hand(5, deck)
hand_2 = PokerHand(cards)
