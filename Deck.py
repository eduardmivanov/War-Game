from Card import Card
import random

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                current_card = Card(rank, suit)
                self.all_cards.append(current_card)


    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()