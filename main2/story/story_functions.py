import time


def print_wait(text):
    print(text)
    time.sleep(.5)


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
