from main2.maindatabase.investigatormain.investigator import Investigator
import random
from main2.story.story_functions import *
from main2.maindatabase.mainCardObjects.playerCardMethods import PlayerCardMethod
class Campaign:
    def __init__(self, investigator, chaos_bag):
        self.investigator = Investigator(investigator)
        self.chaos_bag = chaos_bag
        self.yes = ['ye', 'yes', 'y']
        self.no = ['no', 'n']
        self.pcm = PlayerCardMethod()

    def skill_test(self, skill, test, investigator):
        self.check_for_skill_actions(skill, test, investigator)
        print(investigator.str)
        argument_to_get = getattr(Investigator, skill)
        skill = Investigator.argument_to_get
        self.draw_chaos_bag(skill, test, investigator)

    def draw_chaos_bag(self, skill, test, investigator):
        modifier = random.choice(self.chaos_bag)
        print_wait("You pulled a " + modifier + "!")
        modifier = int(modifier)
        if skill + modifier >= test:
            return "pass"
        else:
            return "fail"

    def check_for_skill_actions(self, skill, test, investigator):
        if len(investigator.skillactions) >= 1:
            for card in investigator.skillactions:
                print_wait("Would you like to use your " + card.name + "?")
                answer = input()
                if answer in self.yes:
                    used_card = "use_" + card.name
                    used_card = used_card.replace(" ", "_").lower()
                    method_to_call = getattr(PlayerCardMethod, used_card)
                    result = method_to_call(self.pcm, card, investigator)
                    self.skill_test(skill, test, investigator)
                    return
                elif answer in self.no:
                    break

