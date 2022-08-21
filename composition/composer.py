#imports
from threading import activeCount
from progression import Progression
from chord import Chord
from rules.rule import Rule

class Composer:
    
    #init function
    def __init__(self, pitches, rules, maxChords, maxRetries):
        self.pitches = pitches
        self.rules = rules # a list of rule 
        self.progressions = [] # holds instances of progressions
        self.maxChords = maxChords
        self.maxRetries = maxRetries
        self.retriesOn = maxRetries>0

    #generate chord progression function
    def makeChordProgression(self):  
        print(self.retriesOn)      
        pitchIdx = 0
        activeProgressions = []
        while pitchIdx < len(self.pitches):
            nextProgressions = []
            #GET POSSIBLE CHORDS AND ADD THEM TO THE ACTIVE PROGRESSIONS
            if len(activeProgressions) == 0:
                for rule in self.rules:
                    possibleChords = rule.getPossibleChords(
                        pitchIdx=pitchIdx,
                        pitch=self.pitches[pitchIdx],
                        prevChord=None,
                        maxChords=self.maxChords
                    )
                    if (possibleChords != None):
                        for chord in possibleChords:
                            nextProgressions.append(Progression([chord]))
            else:
                #for progression in activeProgressions: COMMENTED OUT TO NOT GENERATE RANDOM CHORDS FOR EACH PROGRESSION
                for rule in self.rules:
                    possibleChords = rule.getPossibleChords(
                        pitchIdx=pitchIdx,
                        pitch=self.pitches[pitchIdx],
                        #progression=progression,
                        #prevChord=progression.chords[len(progression.chords)-1],
                        maxChords=self.maxChords
                    )
                    if (possibleChords != None):
                        for chord in possibleChords:
                            for progression in activeProgressions: #GET RID OF THIS LINE TO GO BACK TO OLD VERSION
                                nextProgressions.append(progression.appendChord(chord))


            #DELETING PROGRESSIONS THAT DON'T WORK
            #for progression in nextProgressions:
            #    chordWorks = rule.checkProgression(
            #        rules = self.rules,
            #        pitchIdx=pitchIdx,
            #        pitch=self.pitches[pitchIdx],
            #        prevChord=progression.chords[len(progression.chords)-2],
            #        newChord=progression.chords[len(progression.chords)-1],
            #        progression=progression
            #    )
            #    if (chordWorks):
            #        activeProgressions.append(progression)

            if (self.retriesOn):
                workingProgressions = []
                retryCounter = self.maxRetries
                while(len(workingProgressions)==0 and retryCounter>0):
                    workingProgressions = Rule.trimProgressions(
                        progressions = nextProgressions,
                        rules = self.rules,
                        pitchIdx = pitchIdx,
                        pitch = self.pitches[pitchIdx],
                        retriesOn = (self.maxRetries>0),
                        retries = retryCounter
                    )
                    if (len(workingProgressions)==0):
                        print("NO PROGRESSIONS FOUND")
                        print()
                        print("RETRYING")
                        print()
                        retryCounter-=1
                        nextProgressions=[]
                        for rule in self.rules:
                            possibleChords = rule.getPossibleChords(
                                pitchIdx=pitchIdx,
                                pitch=self.pitches[pitchIdx],
                                #progression=progression,
                                #prevChord=progression.chords[len(progression.chords)-1],
                                maxChords=self.maxChords
                            )
                            if (possibleChords != None):
                                for chord in possibleChords:
                                    for progression in activeProgressions: #GET RID OF THIS LINE TO GO BACK TO OLD VERSION
                                        nextProgressions.append(progression.appendChord(chord))
                                    print("Appending this chord in retries. " + str(retryCounter) + "retry counter. "+ str(chord))
                activeProgressions=workingProgressions
            if (len(activeProgressions)==0):
                exit("Sorry no possible progressions were generated with the current input. Try rerunning the program or changing some of the rules")
                
            pitchIdx += 1

            #REMOVING OLD PROGRESSIONS 
            idx = 0
            while (idx < len(activeProgressions) and (activeProgressions[idx].length()<pitchIdx)):
                idx+=1
            activeProgressions = activeProgressions[idx:]
        self.progressions = activeProgressions #CHANGE THIS LATER ADDED RN TO SEE RESULTS
        return self.progressions



    #function to show the current chord progression generated by the composer to the user (mainly for testing purposes)
    def printProgressions(self):
        for progression in self.progressions:
            print("NEXT PROGRESSION...")
            print(progression)
            print()
            print()
            


    #function to output the chord progression chosen by the user
    def outputChords(self,fileFormat):
        pass
    

   


#testing
# obj = composer(["A","B","C","D","E","F"])
# obj.makeChordProgression()