from main2.maindatabase.investigatormain.investigatorstatic import InvestigatorStatic
from main2.story.story_functions import *
from main2.maindatabase.investigatormain.deck import Deck
from main2.maindatabase.investigatormain.hand import Hand

class Investigator:

    def __init__(self):
        self.static = InvestigatorStatic()
        self.deck = Deck()
        self.hand = Hand(self.deck)
        self.setup()

    def setup(self):
        self.resources = self.static.STARTING_RESOURCES
        self.hand.read_hand()



    def play_card(self, card):
        if self.resources >= card.cost:
            print_wait("You spend " + str(card.cost) + " resources.  To play " + card.name)
