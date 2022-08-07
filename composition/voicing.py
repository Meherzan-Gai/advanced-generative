from chord import Chord
from progression import Progression

class VoicingRule:

    def __init__(self,progression,pitches):
        self.shiftAmt = 12
        self.progression = progression
        self.pitches = pitches

    def getVoicing(self):
        self.setShiftAmt()
        self.moveBassline()
        self.moveNotes()
            
    def setShiftAmt(self):
        bassNotes = []
        for chord in self.progression.chords:
            bassNotes.append(chord.stack[0])
        progressionLow = VoicingRule.getLowest(bassNotes)
        progressionHigh = VoicingRule.getHighest(bassNotes)
        pitchLow = VoicingRule.getLowest(self.pitches)
        pitchHigh = VoicingRule.getHighest(self.pitches)

        if (pitchLow>progressionHigh):   
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



