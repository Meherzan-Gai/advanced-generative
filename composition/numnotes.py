from rules import rules

class numNotes(rules):
    def __init__(self,pitches,progression,notesAmount):
        super().__init__(pitches,progression)
        self.notesAmount = notesAmount

    #returns the possible chords that fit this rule
    def getChords(self):
        pass
    #finds the number of notes in the chord
    def findNumNotes(self):
        pass

