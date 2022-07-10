from rules.base import Rule
from chord import Chord


class SharedTone(Rule):
    def __init__(self,numShared):
        super().__init__()
        self.numShared = numShared
        
    
    #gets chords that work for the rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChords", None)
        if prevChord is None: # on first chord
            pass
        print("sharedTone test") #PLACEHOLDER CHANGE THIS LATER

    #find the number of shared notes between two chords
    def numSharedBetween(chord1,chord2):
        return chord1.numSharedPitches(chord2)

    #find the pitches shared between two chords
    def findShared(chord1,chord2):
        pass

