from typing import OrderedDict
from rules.base import Rule
from chord import Chord
from progression import Progression
import random

class NumNotes(Rule):
    def __init__(self,notesAmount):
        super().__init__()
        self.notesAmount = notesAmount

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        pitchIn = kwargs.get("pitch")
        return self.generateChords(pitchIn, 250)


    def generateChords(self, pitchIn, numChords):
        chordList = []
        notesList = []  
        maxDistance = 0
        if (self.notesAmount == 2):
            maxDistance = 15
        elif (self.notesAmount == 3):
            maxDistance = 10
        elif (self.notesAmount == 4):
            maxDistance = 7
        elif (self.notesAmount == 5):
            maxDistance = 5
        else:
            maxDistance = 4
        #generates chords 
        for x in range (0,numChords):
            currPitch = 36+(pitchIn%12) #puts the chord towards the lower pitch end as melody is typically higher pitched
            notes = []
            notes.append(currPitch)
            #generates the notes for each chord
            for n in range (0,self.notesAmount-1):
                randomPitch = random.randrange(1,maxDistance,1)+currPitch
                currPitch = randomPitch
                notes.append(randomPitch)

            notes.append(pitchIn) #ADDS THE PITCH IN AT THE END OF THE CHORD
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

