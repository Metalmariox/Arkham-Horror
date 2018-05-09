from main2.maindatabase.static_p_database import StaticPDatabase
import random

class Deck:

    def __init__(self):
        # cards is a list of card objects to include in the deck
        data = StaticPDatabase()
        self.database = data.database
        self.deck = []
        self.generate_deck()

    def generate_deck(self):
        x = 0
        while (x < 5):
            new_card = self.database.copy_cards("Physical Training")
            self.deck.append(new_card)
            x = x + 1

    def print_deck(self):
        for card in self.deck:
            print(card)

