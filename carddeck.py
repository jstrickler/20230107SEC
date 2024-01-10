import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
#    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if len(self._cards) == 0:
            raise ValueError("No more cards!")
        return self._cards.pop(0)
    

if __name__ == "__main__":
    d1 = CardDeck()
    print(d1.cards)
    print()
    d1.shuffle()

    for i in range(5):
        c = d1.draw()
        print(f"{c = }")
        