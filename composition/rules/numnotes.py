from rules.base import Rule
from chord import Chord

class NumNotes(Rule):
    def __init__(self,notesAmount):
        super().__init__()
        self.notesAmount = notesAmount

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        pitchIn = kwargs.get("pitch")

        if prevChord is None: # on first chord

            #PLACEHOLDER RETURNS MAJOR TRIAD AND MINOR SEVENTH
            return [Chord([pitchIn,pitchIn+1,pitchIn+2]), Chord([pitchIn,pitchIn+1,pitchIn+2,pitchIn+3])]

        else:

            #PLACEHOLDER RETURNS MAJOR SEVENTH AND MINOR TRIAD
            return [Chord([pitchIn,pitchIn-1,pitchIn-2,pitchIn-3]), Chord([pitchIn,pitchIn-1,pitchIn-2])]


    #findNumNotes() method in chord class finds number of notes

