from Lists import cards
import random


class Player:
    def __init__(self):
        self.cards = []
        self.number_of_cards = 0
        self.score = 0
        self.winner = ""

    def deal_cards(self, number_of_cards):
        while number_of_cards > 0:
            card_selected = random.choice(cards)
            self.cards.append(card_selected)
            number_of_cards -= 1

    def display_cards(self, number_of_display_cards):
        '''to display all cards "number_of_display_cards" should be 1, to display 1 card, "number_of_display_cards"
        should be 0'''
        if number_of_display_cards == 2:
            return self.cards

        if number_of_display_cards == 1:
            return self.cards[0]

    def reset(self):
        '''cards to 0'''
        self.cards = []
        self.number_of_cards = 0

    def score_hand(self):
        (sum(self.cards))
        if 11 in self.cards and sum(self.cards) > 21:
            self.score = sum(self.cards) - 10
        else:
            self.score = sum(self.cards)

    # def compare_score(self, score_hand2):
    #
    #     if self.score == 21 and score_hand2 != 21 and len(self.cards) == 2:
    #         self.winner = "BlackJack"
    #
    #     elif self.score == 21 and score_hand2 == 2:
    #         self.winner = "dealer"
    #
    #     elif self.score > 21:
    #         self.winner = "dealer"
    #
    #     elif self.score <= 21 and self.score > score_hand2:
    #         self.winner = "player"
    #
    #     elif self.score <= 21 and self.score <= score_hand2:
    #         self.winner = "dealer"
