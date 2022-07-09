#make new rule interface
class Rule(object):
   #def __new__(cls, *args, **kwargs):
    instances = []


    def __init__(self):
        self.countPitchIndex = 0

        Rule.instances.append(self)


    #finds the order of priority for the rules
    def getPriority():
        pass
    
    def setActiveProgression(self, progression):
        self.activeProgression = progression

    #creates a list of possible chords that fit the rules
    def getPossibleChords(self, **kwargs):
        return self.getChords(**kwargs)


    def getPreviousChord(self, progression):
        return progression[self.countPitchIndex]


