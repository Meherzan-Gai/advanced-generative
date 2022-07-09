from rules.base import Rule

class Interval(Rule):
    def __init__(self):
        super().__init__()
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
