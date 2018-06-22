from main2.story.story_functions import *
from main2.story.printing import *

class Enemy:
    def __init__(self, name, str, hp, dex, tags, damage, sanitydmg, flavor):
        self.str = int(str)
        self.hp = int(hp)
        self.dex = int(dex)
        self.name = name
        self.flavor = flavor
        self.tags = tags
        self.damage = int(damage)
        self.sanitydmg = int(sanitydmg)

    def check_health(self, investigator):
        if self.hp <= 0:
            self.death(investigator)
            return

    def death(self, investigator):
        print_wait("The " + self.name.lower() + " falls to the ground, unmoving.")
        investigator.enemies_at_location.remove(self)
        if self in investigator.engaged_with:
            investigator.engaged_with.remove(self)

    def engage_investigator(self, investigator):
        investigator.engaged_with.append(self)
        if self not in investigator.enemies_at_location:
            investigator.enemies_at_location.append(self)
        print_wait("The " + self.name + " turns its attention to you.")

    def opportunity_attack(self, investigator):
        print_wait("The " + self.name + " makes an opportunity attack while your guard is down!")
        if self.damage > 0:
            investigator.health -= self.damage
            print(investigator.full_name, "suffered", self.damage, "damage!")
        if self.sanitydmg > 0:
            investigator.sanity -= self.sanitydmg
            print(investigator.full_name, "suffered", self.sanitydmg, "sanity damage!")
        investigator.check_status()
