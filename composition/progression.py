
class Progression:

    def __init__(self, chords):
        # chords is a sequence of Chord instances
        self.chords = chords

    def append(self, chord): 
        return Progression([self.chords, chord])

    def delete(self):
        pass