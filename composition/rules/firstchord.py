from pickle import TRUE
from rules.rule import Rule
from chord import Chord
from progression import Progression

class FirstChord(Rule):
    def __init__(self,ruleOn):
        super().__init__()
        self.ruleOn = ruleOn

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        pass

    def ruleCheck(self, **kwargs):
        pitchIdx = kwargs.get("pitchIdx")
        pitchIn = kwargs.get("pitch")
        newChord = kwargs.get("newChord")
        if (pitchIdx==0):
            if (self.ruleOn == True):
                if (newChord.stack[0]%12 != pitchIn%12):
                    return False
            

        return True
