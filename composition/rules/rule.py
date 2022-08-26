

class Rule(object):

    instances = []

    def __init__(self,priority):
        Rule.instances.append(self)
        self.priority = priority


    #finds the order of priority for the rules
    def getPriority(self):
        return self.priority
    

    #creates a list of possible chords that fit the rules
    def getPossibleChords(self, **kwargs):
        return self.getChords(**kwargs)

    #deletes progressions that don't fit rules
    def checkProgression(self, **kwargs):
        rules = kwargs.get("rules")
        ruleLimit = kwargs.get("ruleLimit")
        for rule in rules[0:ruleLimit]:
            if (rule.ruleCheck(**kwargs) == False):
                return False
        return True

    def trimProgressions(**kwargs):
        workingProgressions=[]
        progressions = kwargs.get("progressions")
        rules = kwargs.get("rules")
        pitchIdx = kwargs.get("pitchIdx")
        pitch = kwargs.get("pitch")
        retriesOn = kwargs.get("retriesOn")
        ruleIdx = len(rules)
        #print("STARTING NEXT INDEX")
        #print()
        #print()
        if (retriesOn == False):
            while(len(workingProgressions)==0 and ruleIdx>=0):
                for progression in progressions:
                    chordWorks = []
                    for rule in rules[0:ruleIdx]:
                        chordWorks.append(rule.ruleCheck(
                            rules = rules,
                            pitchIdx=pitchIdx,
                            pitch = pitch,
                            prevChord=progression.chords[len(progression.chords)-2],
                            newChord=progression.chords[len(progression.chords)-1],
                            progression=progression
                        ))
                    #print()
                    #print()
                    #print("NEW PROGRESSION TESTING")
                    #print(progression)
                    #print(chordWorks)
                    if (chordWorks.count(False)==0):
                        workingProgressions.append(progression)
                ruleIdx-=1

        else:
            for progression in progressions:
                    chordWorks = []
                    for rule in rules[0:ruleIdx]:
                        chordWorks.append(rule.ruleCheck(
                            rules = rules,
                            pitchIdx=pitchIdx,
                            pitch = pitch,
                            prevChord=progression.chords[len(progression.chords)-2],
                            newChord=progression.chords[len(progression.chords)-1],
                            progression=progression
                        ))
                    #print()
                    #print()
                    #print("NEW PROGRESSION TESTING")
                    #print(progression)
                    #print(chordWorks)
                    if (chordWorks.count(False)==0):
                        workingProgressions.append(progression)
                
        print(len(workingProgressions))
        return workingProgressions
            


