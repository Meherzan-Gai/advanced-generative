from rules.base import Rule

class NumNotes(Rule):
    def __init__(self,notesAmount):
        super().__init__()
        self.notesAmount = notesAmount

    #returns the possible chords that fit this rule
    def getChords(self):
        print("numNotes test") #PLACEHOLDER CHANGE THIS LATER

    #finds the number of notes in the chord
    def findNumNotes(self):
        pass

