#importing pitch class set module (pcsets)
import pcsets as ps
from pcsets import pcset
from rules import rules

class interval(rules):
    def __init__(self,pitches,progression,intervalLengths):
        super().__init__(pitches,progression)
        super().allInstances.append(self)
        self.intintervalLengths = intervalLengths
    
    #gets chords that work for the rule
    def getChords(self):
        print("interval test") #PLACEHOLDER CHANGE THIS LATER
        
    #finds the notes one interval distance above the current note with all the possible interval lengths
    def intUp(intervalLength,note):
        pass

    #finds the notes one interval distance below the current note with all the possible interval lengths
    def intDown(intervalLength,note):
        pass
