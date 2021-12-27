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


def set_card(deck, position, card):
    deck._card[position] = card

FrenchDesk.__setitem__ = set_card

a = FrenchDesk()

shuffle(a)
print(a[:5])