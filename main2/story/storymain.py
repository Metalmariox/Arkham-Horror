from main2.story.story_functions import *


class Story:
    def __init__(self):
        self.campaign_list = ["Testing" + "\t" + "Night of the Zealot"]
        self.investigator_list = ["Roland Banks"]
        self.setup()

    def setup(self):
        choice1 = check_campaign_title(self.campaign_list)
        choice2 = check_investigator(self.investigator_list)
        print_wait("Selection : " + choice1 + "\nInvestigator: " + choice2)





Story()