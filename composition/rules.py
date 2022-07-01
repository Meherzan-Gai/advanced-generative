from sharedtone import *
from numnotes import *
from interval import *

#make new rule class
class rules:
    def __init__(self,intervalRule,sharedRule,numNotesRule):
        self.intervalRule = intervalRule
        self.sharedRule = sharedRule
        self.numNotesRule = numNotesRule

    #finds the order of priority for the rules
    def getPriority(self):
        pass



    #creates a list of possible chords that fit the rules
    def getPossibleChords(previousChord):
        pass


