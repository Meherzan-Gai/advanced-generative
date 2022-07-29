from rules.rule import Rule
from chord import Chord
from progression import Progression

class BaseNote(Rule):
    def __init__(self,level):
        super().__init__()
        self.ruleType = level

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        pass

    def ruleCheck(self, **kwargs):
        return True