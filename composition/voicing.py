from chord import Chord
from progression import Progression

class Voicing:

    def __init__(self):
        self.shiftAmt = 12

    def setProgression(self,progression):
        self.progression = progression

    def setMelody(self,melody):
        self.pitches = melody



    def getVoicing(self):
        self.setShiftAmt()
        self.moveBassline()
        self.moveNotes()
            
    def setShiftAmt(self):
        self.shiftAmt = 12
        bassNotes = []
        for chord in self.progression.chords:
            bassNotes.append(chord.stack[0])
        progressionHigh = Voicing.getHighest(bassNotes)
        pitchLow = Voicing.getLowest(self.pitches)
        pitchHigh = Voicing.getHighest(self.pitches)

        if (pitchHigh<36):
            self.shiftAmt = 48

        elif (pitchLow>progressionHigh):   
            while (pitchLow>progressionHigh+24+self.shiftAmt):
                self.shiftAmt+=12
        

    
    def moveBassline(self):
        for chord in self.progression.chords:
            chord.stack[0]+=self.shiftAmt


    def moveNotes(self):
        for chord in self.progression.chords:
            for noteIdx in range (1,len(chord.stack),1):
                while (chord.stack[noteIdx] < chord.stack[0]):
                    chord.stack[noteIdx]+=12

    
    def getLowest(notes):
        lowestNote = notes[0]
        for idx in range(1,len(notes),1):
            if (lowestNote>notes[idx]):
                lowestNote = notes[idx]
        return lowestNote

    
    def getHighest(notes):
        highestNote = notes[0]
        for idx in range(1,len(notes),1):
            if (highestNote<notes[idx]):
                highestNote = notes[idx]
        return highestNote



