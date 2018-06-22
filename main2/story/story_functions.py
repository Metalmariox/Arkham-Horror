import time
import random
from main2.maindatabase.mainCardObjects.playerCardMethods import PlayerCardMethod
from main2.story.printing import *

yes = ['ye', 'yes', 'y']
no = ['no', 'n']





def check_campaign_title(campaigns):
    print_wait("Which campaign would you like to play?")
    print_wait("\n".join(campaigns))
    selection = input().lower()
    flag = 0
    while flag == 0:
        if selection == 'night' or selection == 'zealot' or selection == 'night of the zealot':
            print_wait('Do you want to play the Night of the Living Zealot?')
            choice = input().lower()
            if choice == 'y' or choice == 'yes' or choice == 'ye':
                return 'zealot'
            elif choice == 'n' or choice == 'no':
                check_campaign_title(campaigns)
            else:
                print_wait("I don't understand that selection.")
        elif selection == 'test':
            print_wait("Would you like to go into the testing area?")
            choice = input().lower()
            return 'test'

        else:
            print_wait("I don't understand that selection.")
            check_campaign_title(campaigns)


def check_investigator(investigators):
    print_wait("Who would you like to play as?")
    print_wait("\n".join(investigators))
    selection = input()
    flag = 0
    while flag == 0:
        if selection.lower() == 'banks' or selection.lower() == 'roland' or selection.lower() == 'roland banks':
            print_wait('Do you want to play as Roland Banks?')
            choice = input().lower()
            if choice == 'y' or choice == 'yes' or choice == 'ye':
                return 'banks'
            elif choice == 'n' or choice == 'no':
                flag = 1
                check_investigator(investigators)
            else:
                print_wait("I don't understand that selection.")

        else:
            print_wait("I don't understand that selection.")
            check_investigator(investigators)


def skill_test(skill, test, investigator, chaos_bag):
    # Skill is a shorthand string of the skill being tested
    # Test is the value of the test that needs to be beat
    # investigator is the investigator
    check_for_skill_actions(skill, test, investigator)
    used_skill = return_used_skill(skill, investigator)
    long_skill = return_skill_longform(skill)
    print_pretest(used_skill, test, long_skill)
    return draw_chaos_bag(used_skill, test, chaos_bag, long_skill)


def print_pretest(used_skill, test, long_skill):
    print_wait(
        "You test your " + long_skill + " of " + str(used_skill) + " against a test of " + str(test) + ".")


def return_skill_longform(skill):
    if skill == 'str':
        return "strength"
    if skill == 'dex':
        return "dexterity"
    if skill == 'wis':
        return "wisdom"
    if skill == 'int':
        return "intelligence"


def return_used_skill(skill, investigator):
    if skill == 'str':
        used_skill = investigator.str
    if skill == 'dex':
        used_skill = investigator.dex
    if skill == 'wis':
        used_skill = investigator.wis
    if skill == 'int':
        used_skill = investigator.int
    return used_skill


def draw_chaos_bag(skill, test, chaos_bag, long_skill):
    modifier = int(random.choice(chaos_bag))
    print_wait("You pulled a " + str(modifier) + "!")
    m_skill = skill + modifier
    print_wait("This changes your " + str(long_skill) + " to " + str(m_skill) + "!" )
    return calculate_skill_test(skill, test, modifier)



def calculate_skill_test(skill, test, modifier):
    modifier = int(modifier)
    if skill + modifier >= test:
        return "pass"
    else:
        return "fail"


def check_for_skill_actions(skill, test, investigator):
    if len(investigator.skillactions) >= 1:
        for card in investigator.skillactions:
            print_wait("Would you like to use your " + card.name + "?")
            answer = input()
            if answer in yes:
                used_card = "use_" + card.name
                used_card = used_card.replace(" ", "_").lower()
                method_to_call = getattr(PlayerCardMethod, used_card)
                result = method_to_call("", card, investigator)
                skill_test(skill, test, investigator)
                return
            elif answer in no:
                break
