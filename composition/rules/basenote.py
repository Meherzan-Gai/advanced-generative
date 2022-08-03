from rules.voicingrule import VoicingRule
from rules.buildingrule import BuildingRule
from chord import Chord
from progression import Progression

class BaseNote(BuildingRule,VoicingRule):
    def __init__(self,level):
        super().__init__()
        if (level==1):
            self.maxDistance = 2
        elif (level==2):
            self.maxDistance = 4
        elif (level==3):
            self.maxDistance = 12

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        pass

    def ruleCheck(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        newChord = kwargs.get("newChord", None)
        distance = abs(prevChord.stack[0]-newChord.stack[0])
        if (distance<(12-self.maxDistance) and distance > self.maxDistance):
            return False
        return True