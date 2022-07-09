
class Chord:

    def __init__(self, stack):
        self.stack = stack
        # e.g stack = [60, 64, 67]

    def sharedPitches(self, c2):
        # c2 is a Chord instance
        total = 0
        for pitch in self.stack:
            for otherPitch in c2.stack:
                if pitch == otherPitch:
                    total+=1
        return total