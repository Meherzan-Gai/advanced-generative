from rules.buildingrule import BuildingRule
from chord import Chord
from progression import Progression
import random

class NumNotes(BuildingRule):
    def __init__(self,notesAmount):
        super().__init__()
        self.notesAmount = notesAmount

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        pitchIn = kwargs.get("pitch")
        return self.generateChords(pitchIn, 50)


    def generateChords(self, pitchIn, numChords):
        chordList = []
        notesList = []  
        

        #generates base note and pitch class
        for x in range (0,numChords):
            notes = []
            #generates the notes for each chord
            possibleNotes = [0,1,2,3,4,5,6,7,8,9,10,11]
            notes.append(pitchIn%12)
            possibleNotes.remove(pitchIn%12)
            for n in range (0,self.notesAmount-1):
                randomPitch = possibleNotes[random.randrange(0,len(possibleNotes),1)]
                possibleNotes.remove(randomPitch)
                notes.append(randomPitch)
            notesList.append(notes)


        #REMOVES DUPLICATE CHORDS
        for notes in notesList[:]:
            if notesList.count(notes) > 1:
                notesList.remove(notes)

        #TURNS NOTES INTO CHORDS
        for notes in notesList:
            chordList.append(Chord(notes))

        return chordList

    def ruleCheck(self, **kwargs):
        return True
        #progression = kwargs.get("progression", None)
        #chordsIn = progression.chords
        #chordsOut = []
        #chordsOut = chordsIn
        #return Progression(chordsOut)

        


    #findNumNotes() method in chord class finds number of notes

