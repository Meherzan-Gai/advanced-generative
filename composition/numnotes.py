from rules import rules

class numNotes(rules):
    def __init__(self,pitches,progression,notesAmount):
        super().__init__(pitches,progression)
        super().allInstances.append(self)
        self.notesAmount = notesAmount

    #returns the possible chords that fit this rule
    def getChords(self):
        print("numNotes test") #PLACEHOLDER CHANGE THIS LATER

    #finds the number of notes in the chord
    def findNumNotes(self):
        pass

