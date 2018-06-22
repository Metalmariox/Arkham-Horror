
from main2.maindatabase.mainCardObjects.enemy_database import EnemyDatabase


class StaticEDatabase:
    def __init__(self):

        self.database = EnemyDatabase(r'C:\Users\Gwen\PycharmProjects\ArkhamHorror\main2\databases\Enemies.txt')