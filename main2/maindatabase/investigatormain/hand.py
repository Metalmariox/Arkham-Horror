from main2.maindatabase.investigatormain.deck import Deck
from main2.story.story_functions import *
from main2.story.printing import *

class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.investigator = 0
        self.hand = []
        self.setup()



    def setup(self):
        x = 0
        while x < 5:
            self.draw_card()
            x += 1

    def draw_card(self):
        self.hand.append(self.deck.deck[0])
        self.deck.deck.pop(0)

    def read_hand(self):
        print_wait("Cards in hand:")
        for card in self.hand:
            card.read_card_name()
