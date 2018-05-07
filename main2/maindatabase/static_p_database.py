
from main2.maindatabase.playerDatabase import PlayerDatabase


class StaticPDatabase:
    def __init__(self):

        self.database = PlayerDatabase(r'C:\Users\Gwen\PycharmProjects\ArkhamHorror\main2\PlayerCards.txt')

