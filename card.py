class Card: # inherits from  'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
        
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('3', 'Diamonds')
    print(f"{c1 = }")
    # print(f"{type(c1) = }")
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    
    dan = Card('8', 'Clubs')
    print(f"{dan.rank = }")
    print(c1) #  print(str(c1))  # c1.__str_()_
    

    print(repr(str))
