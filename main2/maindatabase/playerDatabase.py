from main2.maindatabase.database import Database
from main2.maindatabase.mainCardObjects.asset import Asset

class PlayerDatabase(Database):
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
                if line[0] == 'Traits':
                    trait_list = []
                    line[1] = line[1].split()
                    for trait in line[1]:
                        trait_list.append(trait)
                if line[0] == 'Ref':
                    reference_list = []
                    line[1] = line[1].split(', ')
                    for ref in line[1]:
                        reference_list.append(ref)
                    self.pDatabase.append(cDict)
                    cDict = {}


    def create_cards(self):
        for card in self.pDatabase:
            if card['Type'].lower() == 'asset':
                asset = Asset(card["Name"], card['Class'], card['Level'], card['Type'], card['Slot'], card['Traits']
                    , card['Cost'], card['Pips'], card['Text'], card['Flavor'], card['Ref'])
                self.fDatabase[card["Name"]] = asset

    def copy_cards(self, card_name):
        for card in self.pDatabase:
            if card['Name'] == card_name:
                if card['Type'].lower() == 'asset':
                    copy = Asset(card["Name"], card['Class'], card['Level'], card['Type'], card['Slot'], card['Traits']
                        , card['Cost'], card['Pips'], card['Text'], card['Flavor'], card['Ref'])
        return copy

    def print_database(self):
        for card in self.pDatabase:
            for key in card:
                print(key + ' ' + card[key])




                


