from carddeck import CardDeck
from card import Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call method in parent class
        self._cards.append(Card('JOKER', 'JOKER'))
        self._cards.append(Card('JOKER', 'JOKER'))


if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.draw())
    print(j.cards)
