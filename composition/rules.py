#make new rule interface
class rules():
    def __init__(self,pitches,progression):
        self.pitches = pitches
        self.progression = progression
        self.countPitchIndex = 0

    #finds the order of priority for the rules
    def getPriority():
        pass

    #creates a list of possible chords that fit the rules
    def getPossibleChords(self,pitchIn,previousChord):
        self.countPitchIndex+=1
        return ["F",pitchIn,"C"]

    def getPreviousChord(self):
        return self.progression[self.countPitchIndex]

    def getPitch(self):
        return self.pitches[self.countPitchIndex]

