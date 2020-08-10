#!/usr/bin/python3
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=0, clubs=0)
def spades_high(card):
    rand_value = FrenchDeck.ranks.index(card.rank)
    return rand_value * len(suit_values) + suit_values[card.suit]

def test():
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck), deck[0])
    print(deck[:3])
    print(deck[12::13])
    for card in deck:
        print('\t', card)
    for card in sorted(deck, key=spades_high):
        print("sorted", card)

if __name__ == '__main__':
    test()
    