from main2.story.campaign import Campaign
from main2.story.story_functions import *
from main2.story.printing import *
from main2.maindatabase.enemy.static_e_database import StaticEDatabase

class Testing(Campaign):
    def __init__(self, investigator):
        self.chaos_bag = ["+1", "0", "0", "-1"]
        super().__init__(investigator, self.chaos_bag)
        self.enemy_database = StaticEDatabase()
        self.start_testing()

    def start_testing(self):
        self.ghoul = self.enemy_database.database.copy_enemy("Ghoul Minion", self)
        self.ghoul.engage_investigator(self.investigator)
        self.investigator.player_turn()
        self.practice_skill_test()

    def practice_skill_test(self):
        result = skill_test('str', 5, self.investigator, self.chaos_bag)
        if result == 'pass':
            print_wait("You passed the test!")
        elif result == 'fail':
            print_wait("You failed the test!")
        else:
            print_wait("You shouldn't see this")

if __name__ == '__main__':
    test = Testing("banks")