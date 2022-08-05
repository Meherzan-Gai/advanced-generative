from chord import Chord
from progression import Progression

class VoicingRule:

    def __init__(self,shiftAmt):
        self.shiftAmt = 12

    def getVoicing(progression,pitches):
        basslineProgression = VoicingRule.moveBassline(progression,pitches)
        VoicingRule.moveNotes(basslineProgression)
            
    
    def moveBassline(progression,pitches):
        pass

    def moveNotes(progression):
        for chord in progression.chords:
            for x in range (1,len(chord.stack),1):
                while (chord.stack[x] < chord.stack[0]):
                    chord.stack[x]+=12

    



