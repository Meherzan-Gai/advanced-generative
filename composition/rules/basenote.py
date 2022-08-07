from rules.rule import Rule
from chord import Chord
from progression import Progression

class BaseNote(Rule):
    def __init__(self,priority,level):
        super().__init__(priority)
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
        if (distance>=(12-self.maxDistance)):
            newChord.stack[0]-=12
        return True