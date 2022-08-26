from pickle import TRUE
from rules.rule import Rule
from chord import Chord
from progression import Progression

class FirstChord(Rule):
    def __init__(self,priority,ruleOn):
        super().__init__(priority)
        self.ruleOn = ruleOn

    def getChords(self,**kwargs):
        pass

    def ruleCheck(self,**kwargs):
        pitchIn = kwargs.get("pitch")
        newChord = kwargs.get("newChord")
        pitchIdx = kwargs.get("pitchIdx")
        if (self.ruleOn):
            if (pitchIdx==0):
                if (pitchIn%12!=newChord.stack[0]):
                    return False
        return True