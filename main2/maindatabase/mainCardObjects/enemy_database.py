from main2.maindatabase.database import Database
from main2.maindatabase.enemy.enemy import Enemy

class EnemyDatabase(Database):
    def __init__(self, index):
        super().__init__(index)
        self.pDatabase = []
        self.fDatabase = {}
        self.create_card_dictionary()
        self.create_cards()

    def create_card_dictionary(self):
        cDict = {}
        with open(self.index, 'r') as f:
            for line in f:
                line = line.split(maxsplit=1)
                # Splits the line into a list
                cDict[line[0]] = line[1].rstrip()
                if line[0] == 'Tags':
                    trait_list = []
                    line[1] = line[1].split()
                    for trait in line[1]:
                        trait_list.append(trait)
                if line[0] == 'Flavor':
                    self.pDatabase.append(cDict)
                    cDict = {}

    def create_cards(self):
        for card in self.pDatabase:
            enemy = Enemy(card["Name"], card["Str"], card["Hp"], card["Dex"], card["Tags"], card['Damage'], card['SanityDmg']
                          , card['Flavor'])
            self.fDatabase[card["Name"]] = enemy

    def copy_enemy(self, card_name, campaign):
        for card in self.pDatabase:
            if card['Name'] == card_name:
                copy = Enemy(card["Name"], card["Str"], card["Hp"], card["Dex"], card["Tags"], card['Damage'], card['SanityDmg']
                        , card['Flavor'])
            return copy

    def print_database(self):
        for card in self.pDatabase:
            for key in card:
                print(key + ' ' + card[key])

