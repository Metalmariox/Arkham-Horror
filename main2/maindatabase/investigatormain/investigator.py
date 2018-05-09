from main2.maindatabase.investigatormain.investigatorstatic import InvestigatorStatic
from main2.story.story_functions import *
from main2.maindatabase.investigatormain.deck import Deck
from main2.maindatabase.investigatormain.hand import Hand
from main2.maindatabase.mainCardObjects.playerCardMethods import PlayerCardMethod


class Investigator:

    def __init__(self, name):
        self.static = InvestigatorStatic()
        self.deck = Deck()
        self.hand = Hand(self.deck)
        self.reset_banks()
        self.str = 4
        self.name = name
        self.skillactions = []
        self.setup()
        self.assets = []


    def setup(self):
        self.resources = self.static.STARTING_RESOURCES
        self.actions = self.static.STARTING_ACTIONS

    def reset_banks(self):
        self.str = 4
        self.int = 3
        self.wis = 4
        self.dex = 2

    def player_turn(self):
        if self.actions >= 1:
            print(self.actions)
            print_wait("It is your turn.  What do you do?\n"
                       + "Look at hand\t\t Play a card")
            print_wait("You have " + str(self.resources) + " resources.")
            selection = input()
            if selection in self.static.VInputLook:
                self.hand.read_hand()
                self.player_turn()
            elif selection in self.static.VInputPlay:
                self.hand.read_hand()
                print_wait("What card would you like to play?")
                chosen_card = input()
                self.play_card(chosen_card)
            elif selection == 'pass':
                self.actions = 0
                self.player_turn()
            else:
                print_wait("That's not a valid option.")
                self.player_turn()

    def play_card(self, chosen_card):
        for card in self.hand.hand:
            if chosen_card.lower() in card.ref:
                if self.resources >= card.cost:
                    played_card = card.name
                    played_card = played_card.replace(" ", "_").lower()
                    method_to_call = getattr(PlayerCardMethod, played_card)
                    self.resources -= card.cost
                    result = method_to_call("", card, self)
                    self.actions -= 1
                    self.hand.hand.remove(card)
                    self.player_turn()
                    return
                elif self.resources <= card.cost:
                    remaining_resources = card.cost - self.resources
                    print_wait("You are short on resources.  You need to obtain " + str(remaining_resources) + " more resources.")
                    self.player_turn()
                    return
                else:
                    break
        print_wait("Sorry that's not a valid card.")
        self.player_turn()


if __name__ == '__main__':
    test = Investigator('banks')
    p = PlayerCardMethod()
    p.use_physical_training(5, test)
