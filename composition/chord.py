#importing pitch class set module (pcsets)
from pcsets.pcset import PcSet as ps
import librosa

class Chord:
    key = "C:maj"

    def __init__(self, stack):
        self.stack = stack
        # e.g stack = [60, 64, 67]

    #finds the number of shared pitches between two chords
    def numSharedPitches(self, c2):
        # c2 is a Chord instance
        total = 0
        for pitch in self.stack:
            for otherPitch in c2.stack:
                if pitch%12 == otherPitch%12:
                    total+=1
        return total

    def findSharedPitches(self, c2):
        # c2 is a Chord instance
        sharedPitches =[]
        for pitch in self.stack:
            for otherPitch in c2.stack:
                if pitch%12 == otherPitch%12:
                    sharedPitches.append(pitch%12)
        return sharedPitches

    #finds and returns the interval vector of the chord
    def findIntervals(self):
        return ps(self.stack).ivec()

    def findIntervalsBoolean(self):
        ivec = self.findIntervals()
        booleanIvec = []
        for interval in ivec:
            if (interval>0):
                booleanIvec.append(True)
            else:
                booleanIvec.append(False)
        return booleanIvec

    #finds and returns the pitch class sets that make up the chord (the pitches that make up the chord with no duplicates)
    def findPitchSets(self):
        return ps(self.stack)

    #finds and returns the number of notes in the chord
    def findNumNotes(self):
        return len(self.stack)

    def arrNotes(self):
        bassNote = self.stack[0]
        notes = sorted(self.stack[1:])
        notes.insert(0,bassNote)
        self.stack=notes

    def clone(self):
        notesList = []
        for note in self.stack:
            notesList.append(note)
        return Chord(notesList)

    def __str__(self):
        noteString = "["
        for note in self.stack:
            noteString += librosa.midi_to_note(note, key = Chord.key) + ", "
        noteString = noteString[:-2]
        
        return noteString + "]"

    def octaveUp(self):
        for noteIdx in range(0,len(self.stack),1):
            self.stack[noteIdx]+=12
            if (self.stack[noteIdx]>127):
                print("Warning: Note is above maximum pitch of 127, pitching down to 127")
                print()
                self.stack[noteIdx]=127

    def octaveDown(self):
        for noteIdx in range(0,len(self.stack),1):
            self.stack[noteIdx]-=12
            if (self.stack[noteIdx]<0):
                print("Warning: Note is below minimum pitch of 0, pitching up to 0")
                print()
                self.stack[noteIdx]=0


    def setKey(key):
        Chord.key = key