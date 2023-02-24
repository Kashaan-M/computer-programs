# Chapter 18 : Think Python 2nd Ed.
class Card:
    """Represents a standard playing card."""

    # Class Attributes
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [
        None,
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self, suit=0, rank=2):
        # Here 'suit' and 'rank' are called Instance Attributes because they are associated with a particular instance
        self.suit = suit % 4
        self.rank = rank % 14

    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    # IMPORTANT
    # Every Card has its own 'suit' and 'rank' but there is only one copy of 'suit_names' and 'rank_names'

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False

        # suits are the same... check ranks
        return self.rank < other.rank

    # you can write this more concisely using tuple comparison
    # def __lt__(self, other):
    #    t1 = self.suit, self.rank
    #    t2 = other.suit, other.rank
    #    return t1 < t2


class Deck:
    """Represents a Card Deck

    Remember a Deck has 52 playing Cards, so it reasonable to use a list
    of Cards as an instance attribute
    """

    def __init__(self):
        self.cards = []

        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(card.__str__())
            # alternate : res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle(self):
        from random import shuffle

        shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, hands=1, cards=52):
        # Parameters
        # hands: number of hands
        # cards: number of cards per hand
        total_hands = []
        for i in range(hands):
            hand = Hand()
            self.move_cards(hand, cards // hands)
            total_hands += [hand]

        return total_hands


# Inheritance
class Hand(Deck):
    """Represents a hand or playing cards."""

    def __init__(self, label=""):
        self.cards = []
        self.label = label
