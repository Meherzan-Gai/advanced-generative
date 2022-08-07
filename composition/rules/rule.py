

class Rule(object):

    instances = []

    def __init__(self,priority):
        Rule.instances.append(self)
        self.priority = priority


    #finds the order of priority for the rules
    def getPriority():
        pass
    

    #creates a list of possible chords that fit the rules
    def getPossibleChords(self, **kwargs):
        return self.getChords(**kwargs)

    #deletes progressions that don't fit rules
    def checkProgression(self, **kwargs):
        rules = kwargs.get("rules")
        for rule in rules:
            if (rule.ruleCheck(**kwargs) == False):
                return False
        return True
            


