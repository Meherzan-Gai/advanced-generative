#importing pitch class set module (pcsets)
from pcsets.pcset import PcSet as ps

class Chord:

    def __init__(self, stack):
        self.stack = stack
        # e.g stack = [60, 64, 67]

    #finds the number of shared pitches between two chords
    def sharedPitches(self, c2):
        # c2 is a Chord instance
        total = 0
        for pitch in self.stack:
            for otherPitch in c2.stack:
                if pitch == otherPitch:
                    total+=1
        return total

    #finds and returns the interval vector of the chord
    def findIntervals(self):
        return ps(self.stack).ivec()