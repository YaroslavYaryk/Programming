from collections import namedtuple
from random import choice, shuffle

Card = namedtuple('Card', ['rank', "suit"])

class FrenchDesk:
    ranks = [str(i) for i in range(2,11)] + list("JOKA") 
    suits = "spades diamonds clubs hearts".split()


    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._card) 


    def __getitem__(self,position):
        return self._card[position]                                       


suit_values = dict(spades = 3, diamonds = 2, clubs = 1, hearts = 0)

def spaders_hight(card):
    rank_values = FrenchDesk.ranks.index(card.rank)
    return rank_values * len(suit_values) + suit_values[card.suit]


deck = FrenchDesk()
for i in sorted(deck, key= spaders_hight):
    print(i)