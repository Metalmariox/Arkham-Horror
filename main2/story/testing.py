from main2.story.campaign import Campaign
from main2.story.story_functions import *
from main2.maindatabase.investigatormain.investigator import Investigator

class Testing(Campaign):
    def __init__(self, investigator):
        chaos_bag = ["+1", "0", "0", "-1"]
        super().__init__(investigator, chaos_bag)
        self.start_testing()

    def start_testing(self):
        self.investigator.hand.read_hand()
        self.investigator.player_turn()
        self.practice_skill_test()

    def practice_skill_test(self):
        result = self.skill_test('str', 5, self.investigator)
        if result == 'pass':
            print_wait("You passed the test!")
        else:
            print_wait("You failed the test!")

if __name__ == '__main__':
    test = Testing("banks")
    test.practice_skill_test()