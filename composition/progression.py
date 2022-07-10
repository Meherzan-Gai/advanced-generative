
class Progression:

    def __init__(self, chords):
        # chords is a sequence of Chord instances
        self.chords = chords

    def append(self, chord): 
        #return Progression([self.chords, chord])
        newProgression = Progression(self.chords)
        newProgression.chords.append(chord)
        return newProgression

    def delete(self):
        pass