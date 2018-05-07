from main2.maindatabase.mainCardObjects.cardMethods import *
from main2.story.story_functions import *

class PlayerCard:
    def __init__(self, c_name, c_class, c_level, c_type, c_slot, c_traits, c_cost, c_pips, c_text, c_flavor):
        self.name = str(c_name)
        self.c_class = str(c_class)
        self.level = c_level
        self.type = str(c_type)
        if c_slot is "N/A":
            self.slot = ""
        else:
            self.slot = str(c_slot)
        self.traits = str(c_traits)
        self.cost = int(c_cost)
        self.pips = str(c_pips)
        self.text = str(c_text)
        self.flavor = str(c_flavor)

    def read_card(self):
        print_wait(self.name.capitalize() + "\n" + self.c_class + "\t" + self.type + "\n" + "Level: " + self.level
                   + "\n" + self.slot + "\n" + self.traits + "\nCost:" + str(self.cost) + "\nPips:" + self.pips
                   + "\n" + self.text + "\n" + self.flavor)

    def read_card_name(self):
        print_wait(self.name)



