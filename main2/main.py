from main2.maindatabase.playerDatabase import PlayerDatabase
from main2.maindatabase.investigatormain.deck import Deck
from main2.maindatabase.investigatormain.hand import Hand
from main2.maindatabase.investigatormain.investigator import Investigator

index = 'PlayerCards.txt'
database = PlayerDatabase(index)
database.fDatabase[".45 Automatic"].read_card()
deck = Deck()
hand = Hand(deck)
investigator = Investigator('banks')