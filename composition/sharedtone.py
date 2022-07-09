from rules import rules


class sharedTone(rules):
    def __init__(self,pitches,progression,numShared):
        super().__init__(pitches,progression)
        super().allInstances.append(self)
        self.numShared = numShared
    
    def getChords(self):
        print("sharedTone test")

    #find the number of shared notes between two chords
    def numSharedBetween(chord1,chord2):
        pass

    def findShared(chord1,chord2):
        pass
