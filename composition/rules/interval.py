from rules.rule import Rule
from chord import Chord

class Interval(Rule):
    def __init__(self,intervalLengths):
        super().__init__()
        self.intervalLengths = intervalLengths
    
    #gets chords that work for the rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        pitchIn = kwargs.get("pitch")
        return self.generateChords(pitchIn, 5)

    
    def generateChords(self, pitchIn, cutoff):
        return None

    def ruleCheck(self, **kwargs):
        newChord = kwargs.get("newChord", None)
        if (newChord.findIntervalsBoolean() == self.intervalLengths):
            return True
        else:
            return False

    #finds the notes one interval distance above the current note with all the possible interval lengths
    def intUp(intervalLength,note):
        pass

    #finds the notes one interval distance below the current note with all the possible interval lengths
    def intDown(intervalLength,note):
        pass
