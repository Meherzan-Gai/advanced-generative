class Rule(object):

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

    #deletes progressions that don't fit rules
    def checkProgression(self, **kwargs):
        return self.trimChord(**kwargs)


    def getPreviousChord(self, progression):
        return progression[self.countPitchIndex]


