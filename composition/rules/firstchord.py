from pickle import TRUE
from rules.voicingrule import VoicingRule
from chord import Chord
from progression import Progression

class FirstChord(VoicingRule):
    def __init__(self,ruleOn):
        super().__init__()
        self.ruleOn = ruleOn
