from main2.story.printing import *
from main2.story.story_functions import *

class PlayerCardMethod:
    def __init__(self):
        self.yes = ['ye', 'yes', 'y']
        self.no = ['no', 'n']

    def _45_automatic(self, card, investigator):
        _45 = _45_Automatic(card, investigator)
        investigator.assets[card] = _45


class _45_Automatic():
    def __init__(self, card, investigator):
        self.ammo = 4
        self.card = card
        self.investigator = investigator
        print_wait("You load up your .45 Automatic and turn off the safety.")
        investigator.assets[card] = self
        investigator.fightactions.append(card)

    def use(self, target):
        if self.ammo > 0:
            self.investigator.fight(target, 1, 2, hit_flavor= "You manage to shoot the " + target.name + "!",
                                    miss_flavor= "Your shot misses!")
            self.ammo -= 1
        else:
            print_wait("You're out of ammo!")
        return "skip"

    def _physical_training(self, card, investigator):
        print_wait("Your muscles tense from months of harsh training.")
        investigator.assets.append(card)
        investigator.skillactions.append(card)

    def use_physical_training(self, card, investigator):
        while investigator.resources > 0:
            print_wait("Would you like to spend a resource?  You have " + str(investigator.resources) + " left.")
            answer = input()
            if answer in self.yes:
                print_wait("Which skill would you like to boost?")
                print_wait("STR\t\tWIS")
                answer2 = input()
                if answer2.lower() == "str":
                    print_wait("You tighten your fist as you gather your strength")
                    initial_strength = int(investigator.str)
                    investigator.str += 1
                    print_wait("Your STR increased from " + str(initial_strength) + " to " + str(investigator.str)
                               + " until the end of the turn.")
                    investigator.resources -= 1

                elif answer2.lower() == 'wis':
                    investigator.wis += 1
                    print_wait("You calm your mind to strengthen your willpower.")
                    initial_wisdom = investigator.wis
                    print_wait("Your WIS increased from " + initial_wisdom + " to " + investigator.wis
                               + " until the end of the turn.")
                    investigator.resources -= 1

                else:
                    print_wait("That is not a valid option.")
                    self.use_physical_training(card, investigator)
            elif answer in self.no:
                return

        print_wait("You don't have enough resources to keep going.")
        return
