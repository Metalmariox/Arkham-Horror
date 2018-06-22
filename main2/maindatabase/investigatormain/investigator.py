from main2.maindatabase.investigatormain.investigatorstatic import InvestigatorStatic
from main2.story.story_functions import *
from main2.maindatabase.investigatormain.deck import Deck
from main2.maindatabase.investigatormain.hand import Hand
from main2.maindatabase.mainCardObjects.playerCardMethods import PlayerCardMethod
from main2.maindatabase.enemy.enemy import Enemy
from main2.story.printing import *

class Investigator:

    def __init__(self, name, chaos_bag):
        self.static = InvestigatorStatic()
        self.deck = Deck()
        self.chaos_bag = chaos_bag
        self.hand = Hand(self.deck)
        self.reset_banks()
        self.str = 4
        self.name = name
        name_to_call = "init_" + name.lower()
        method_to_call = getattr(Investigator, name_to_call)
        result = method_to_call(self)
        self.skillactions = []
        self.fightactions = []
        self.assets = {}
        self.engaged_with = []
        self.enemies_at_location = []
        self.setup()

    def init_banks(self):
        self.health = 9
        self.sanity = 5
        self.full_name = "Roland Banks"

    def setup(self):
        self.resources = self.static.STARTING_RESOURCES
        self.actions = self.static.STARTING_ACTIONS

    def reset_banks(self):
        self.str = 4
        self.int = 3
        self.wis = 4
        self.dex = 2

    def player_turn(self):
        while self.actions >= 1:
            self.player_turn_intro()
            self.get_player_turn_input()

    def fight(self, target, modifier=0, damage=1, hit_flavor='', miss_flavor=''):
        if hit_flavor == '':
            hit_flavor = "You deliver a powerful blow onto the " + str(target.name) + "!"
        if miss_flavor == '':
            miss_flavor = "You attack but you miss the " + target.name + "!"
        keep_going = self.check_fight_actions(target)
        if keep_going == "skip":
            return
        self.str = self.str + modifier
        result = skill_test('str', target.str, self, self.chaos_bag)
        if result == "pass":
            target.hp -= damage
            print_wait(hit_flavor)
            target.check_health(self)
            return
        else:
            print_wait(miss_flavor)

    def check_fight_actions(self, target):
        if len(self.fightactions) > 0:
            for index in range(len(self.fightactions)):
                print_wait("Would you like to use your " + self.fightactions[index].name + "?")
                answer = input()
                if answer in yes:
                    for key in self.assets.items():
                        if key.name == self.fightactions[index].name:
                            print("HERE")
                            return_value = value.use(target)
                            return return_value
                            break
                elif answer in no:
                    break

    def get_player_turn_input(self):
        selection = input()
        if selection.lower() in self.static.VInputLook:
            self.selection_read_card()
        elif selection.lower() in self.static.VInputPlay:
            self.selection_play_card()
        elif selection.lower() in self.static.VInputFight:
            self.selection_fight_enemy()
        elif selection.lower() in self.static.VInputDodge:
            self.selection_dodge_enemy()
        elif selection == 'pass':
            self.actions = 0
            return
        else:
            print_wait("That's not a valid option.")
            return

    def selection_play_card(self):
        self.hand.read_hand()
        print_wait("What card would you like to play?")
        chosen_card = input()
        self.play_card(chosen_card)

    def selection_read_card(self):
        self.hand.read_hand()
        print_wait("Which card would you like to look at?")
        chosen_card = input()
        for card in self.hand.hand:
            valid = self.is_card_in_hand(chosen_card)
            if valid is True:
                card.read_card()
                return
        print_wait("That's not a valid choice.")

    def selection_fight_enemy(self):
        valid_choice = ''
        print_wait("Enemies at location: ")
        for enemy in self.enemies_at_location:
            print_wait(enemy.name)
        if len(self.enemies_at_location) > 1:
            chosen_enemy = input("Which enemy do you want to fight?")
            for enemy in self.enemies_at_location:
                if enemy.name == chosen_enemy:
                    valid_choice = 't'
                    self.fight(enemy)
            if valid_choice == '':
                print_wait("That is not a valid selection.")
        else:
            self.fight(self.enemies_at_location[0])






    def player_turn_intro(self):
        if self.actions >= 1:
            self.player_status()
            self.check_enemies()
            self.give_player_options()
            return
        elif self.actions <= 0:
            self.end_turn()

    def player_status(self):
        print_wait("You have " + str(self.actions) + " actions left.")
        print("You have", self.health, "health remaining.")
        print("You have", self.sanity, "sanity remaining.")
        print_wait("You have " + str(self.resources) + " resources.")

    def check_enemies(self):
        if len(self.engaged_with) >= 1:
            print_wait("You are currently engaged with:")
            for enemy in self.engaged_with:
                print_wait(enemy.name)
            if len(self.enemies_at_location) >= 1 and len(self.engaged_with) == 0:
                for enemy in self.enemies_at_location:
                    print_wait("There is a " + enemy + " at your location.")

    def give_player_options(self):
        if self.enemies_at_location == 0:
            print_wait("It is your turn.  What do you do?\n"
                       + "{0:>15} {1:>15}".format("Look at a card", "Play a card"))
        else:
            print_wait("It is your turn.  What do you do?\n"
                       + "{0:>15} {1:>15} {2:>7} {3:>7}".format("Look at a card", "Play a card", "Fight", "Dodge"))

    def is_card_in_hand(self, chosen_card):
        for card in self.hand.hand:
            if chosen_card.lower() in card.ref:
                return True

    def check_status(self):
        if self.health < 0:
            print("You have been defeated!")

    def play_card(self, chosen_card):
        if len(self.engaged_with) != 0:
            for enemy in self.engaged_with:
                enemy.opportunity_attack(self)
        for card in self.hand.hand:
            if chosen_card.lower() in card.ref:
                if self.resources >= card.cost:
                    played_card = card.name
                    played_card = played_card.replace(" ", "_").lower()
                    played_card = "_" + played_card
                    method_to_call = getattr(PlayerCardMethod, played_card)
                    self.resources -= card.cost
                    result = method_to_call(PlayerCardMethod(), card, self)
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
        return
