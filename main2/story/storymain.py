from main2.story.story_functions import *
from main2.story.printing import *
from main2.story.testing import Testing

class Story:
    def __init__(self):
        self.campaign_list = ["Testing" + "\t" + "Night of the Zealot"]
        self.investigator_list = ["Roland Banks"]
        self.setup()

    def setup(self):
        choice1 = check_campaign_title(self.campaign_list)
        choice2 = check_investigator(self.investigator_list)
        print_wait("Selection : " + choice1 + "\nInvestigator: " + choice2)
        self.start_campaign(choice1, choice2)

    def start_campaign(self, campaign, investigator):
        if campaign == 'test':
            self.campaign = Testing(investigator)






Story()