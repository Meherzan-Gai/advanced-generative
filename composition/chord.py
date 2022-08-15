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
            noteString += "btw:" + str(note)+ "    , "
        noteString = noteString[:-2]
        
        return noteString + "]"

    def setKey(key):
        Chord.key = key