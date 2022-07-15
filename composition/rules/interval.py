from rules.base import Rule
from chord import Chord

class Interval(Rule):
    def __init__(self,intervalLengths):
        super().__init__()
        self.intintervalLengths = intervalLengths
    
    #gets chords that work for the rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        pitchIn = kwargs.get("pitch")

        if prevChord is None: # on first chord

            #PLACEHOLDER RETURNS MAJOR TRIAD AND MINOR SEVENTH
            return [Chord([pitchIn,pitchIn+4,pitchIn+7]), Chord([pitchIn,pitchIn+3,pitchIn+7,pitchIn+10])]

        else:

            #PLACEHOLDER RETURNS MAJOR SEVENTH AND MINOR TRIAD
            return [Chord([pitchIn,pitchIn+4,pitchIn+7,pitchIn+11]), Chord([pitchIn,pitchIn+3,pitchIn+7])]

        
    #finds the notes one interval distance above the current note with all the possible interval lengths
    def intUp(intervalLength,note):
        pass

    #finds the notes one interval distance below the current note with all the possible interval lengths
    def intDown(intervalLength,note):
        pass
