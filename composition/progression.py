from chord import Chord
class Progression:

    def __init__(self, chords):
        # chords is a sequence of Chord instances
        self.chords = chords

    def length(self):
        return len(self.chords)
        

    def appendChord(self, chord): 
        #return Progression([self.chords, chord])      ORIGINAL

        #newProgression = Progression(self.chords)     2nd VERSION 
        #newProgression.chords.append(chord)
        #return newProgression

        newProgression = self.clone()
        newProgression.chords.append(chord.clone())
        return newProgression
        
    def clone(self):
        newChordList = []
        for chord in self.chords:
            newChordList.append(chord.clone())
        return Progression(newChordList)  

    def delete(self):
        del self

    def __str__(self):
        progressionString = ""
        for chord in self.chords:
            progressionString += str(chord) + ", "
        return progressionString[:-2]

    def arrChords(self):
        for chord in self.chords:
            chord.arrNotes()