from main2.maindatabase.investigatormain.investigator import Investigator
from main2.maindatabase.enemy.static_e_database import StaticEDatabase
from main2.story.story_functions import *
from main2.maindatabase.mainCardObjects.playerCardMethods import PlayerCardMethod
class Campaign:
    def __init__(self, investigator, chaos_bag):
        self.chaos_bag = chaos_bag
        self.investigator = Investigator(investigator, self.chaos_bag)
        self.enemies = {}
        self.enemy_database = StaticEDatabase()
        self.yes = ['ye', 'yes', 'y']
        self.no = ['no', 'n']
        self.pcm = PlayerCardMethod()

    def add_enemy(self, enemy):
        self.enemies[enemy.name] = enemy



