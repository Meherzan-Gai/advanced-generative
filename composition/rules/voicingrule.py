from chord import Chord
from progression import Progression

class VoicingRule:

    instances = []

    def __init__(self):
        VoicingRule.instances.append(self)

    
    def getPossibleVoicing(self,progression):
        return self.getVoicing(progression)

    def checkVoicing(self,progression):
        return self.voiceCheck(progression)





