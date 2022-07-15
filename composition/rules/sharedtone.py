#imports
from rules.base import Rule
from chord import Chord


class SharedTone(Rule):
    def __init__(self,numShared):
        super().__init__()
        self.numShared = numShared
        
    
    #gets chords that work for the rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        pitchIn = kwargs.get("pitch")

    
    def generateChords(self, prevChord, pitchIn, cutoff):
        pass

    #find the number of shared notes between two chords
    def numSharedBetween(chord1,chord2):
        return chord1.numSharedPitches(chord2)

    #find the pitches shared between two chords
    def findShared(chord1,chord2):
        return chord1.findSharedPitches(chord2)

