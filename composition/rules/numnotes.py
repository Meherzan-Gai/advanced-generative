from rules.base import Rule
from chord import Chord

class NumNotes(Rule):
    def __init__(self,notesAmount):
        super().__init__()
        self.notesAmount = notesAmount

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChords", None)
        pitchIn = kwargs.get("pitch")

        if prevChord is None: # on first chord

            #PLACEHOLDER RETURNS MAJOR TRIAD AND MINOR SEVENTH
            return [Chord([pitchIn,pitchIn+4,pitchIn+7]), Chord([pitchIn,pitchIn+3,pitchIn+7,pitchIn+10])]

        else:

            #PLACEHOLDER RETURNS MAJOR SEVENTH AND MINOR TRIAD
            return [Chord([pitchIn,pitchIn+4,pitchIn+7,pitchIn+11], Chord([pitchIn,pitchIn+3,pitchIn+7]))]


    #findNumNotes() method in chord class finds number of notes

