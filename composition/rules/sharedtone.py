#imports
from rules.rule import Rule
from chord import Chord
from progression import Progression
import random

class SharedTone(Rule):
    def __init__(self,priority,numShared):
        super().__init__(priority)
        self.numShared = numShared
        
    
    #gets chords that work for the rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        pitchIn = kwargs.get("pitch")
        return self.generateChords(prevChord,pitchIn, 5)

    
    def generateChords(self, prevChord, pitchIn, cutoff):
        return None

    def ruleCheck(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        newChord = kwargs.get("newChord", None)

        if (prevChord!=None):
            if (prevChord.numSharedPitches(newChord)<self.numShared):
                return False
        return True


