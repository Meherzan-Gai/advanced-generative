from rules import rules


class sharedTone(rules):
    def __init__(self,pitches,progression,numShared):
        super().__init__(pitches,progression)
        super().allInstances.append(self)
        self.numShared = numShared
    
    #gets chords that work for the rule
    def getChords(self):
        print("sharedTone test") #PLACEHOLDER CHANGE THIS LATER

    #find the number of shared notes between two chords
    def numSharedBetween(chord1,chord2):
        pass

    #find the pitches shared between two chords
    def findShared(chord1,chord2):
        pass

