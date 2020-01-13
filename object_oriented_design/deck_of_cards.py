import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


class CardDeck:
    def __init__(self, cards):
        if cards:
            self.cards = cards
        else:
            self.cards = list()

    def shuffle(self):
        for i in range(len(self.cards)):
            card_to_swap = random.randint(i)
            self.cards[i], self.cards[card_to_swap] = self.cards[card_to_swap], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class BlackJack(CardDeck):
    def value(self):
        value, aces = 0, 0
        for card in self.cards:
            value += min(card.number, 10)
            aces += 1
        while value <= 11:
            if aces:
                value += 10
                aces -= 1
        return value