#imports
from rules.base import Rule
from chord import Chord
from progression import Progression
import random

class SharedTone(Rule):
    def __init__(self,numShared):
        super().__init__()
        self.numShared = numShared
        
    
    #gets chords that work for the rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        pitchIn = kwargs.get("pitch")
        return self.generateChords(prevChord,pitchIn, 5)

    
    def generateChords(self, prevChord, pitchIn, cutoff):
        return None

    def trimChord(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        progression = kwargs.get("progression", None)
        newChord = kwargs.get("newChord", None)
        chordsIn = progression.chords
        chordsOut = []

        if (prevChord!=None):
            if (SharedTone.numSharedBetween(prevChord,newChord)<self.numShared):
                progression.delete()

    
    #find the number of shared notes between two chords
    def numSharedBetween(chord1,chord2):
        return chord1.numSharedPitches(chord2)

    #find the pitches shared between two chords
    def findShared(chord1,chord2):
        return chord1.findSharedPitches(chord2)

