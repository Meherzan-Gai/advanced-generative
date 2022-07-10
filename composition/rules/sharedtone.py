#imports
from rules.base import Rule
from chord import Chord


class SharedTone(Rule):
    def __init__(self,numShared):
        super().__init__()
        self.numShared = numShared
        
    
    #gets chords that work for the rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChords", None)
        pitchIn = kwargs.get("pitch")

        if prevChord is None: # on first chord

            #PLACEHOLDER RETURNS MAJOR TRIAD AND MINOR SEVENTH
            return [Chord([pitchIn,pitchIn+4,pitchIn+7]), Chord([pitchIn,pitchIn+3,pitchIn+7,pitchIn+10])]

        else:

            #PLACEHOLDER RETURNS MAJOR SEVENTH AND MINOR TRIAD
            return [Chord([pitchIn,pitchIn+4,pitchIn+7,pitchIn+11], Chord([pitchIn,pitchIn+3,pitchIn+7]))]

    #find the number of shared notes between two chords
    def numSharedBetween(chord1,chord2):
        return chord1.numSharedPitches(chord2)

    #find the pitches shared between two chords
    def findShared(chord1,chord2):
        return chord1.findSharedPitches(chord2)

