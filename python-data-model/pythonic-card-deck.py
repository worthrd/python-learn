import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()
    # suits = "\u2660 \u2662 \u2663 \u2661".split()

    def __init__(self) -> None:
        self._cards = [
            Card(rank, suit) for rank in self.ranks for suit in self.suits
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

print(len(deck))

# print(deck._cards)

print(deck[12::13])
