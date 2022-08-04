from pickle import TRUE
from rules.rule import Rule
from chord import Chord
from progression import Progression

class FirstChord(Rule):
    def __init__(self,ruleOn):
        super().__init__()
        self.ruleOn = ruleOn

    def voiceCheck(self,progression,pitches):
        if (self.ruleOn):
            if (progression.chords[0].stack[0]!=pitches[0]%12):
                return False
        return True
