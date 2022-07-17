#imports
from composer import Composer
from progression import Progression
from chord import Chord
from rules.sharedtone import SharedTone
from rules.numnotes import NumNotes
from rules.interval import Interval
import json

# use this as a template for importing all your classes
# SharedTone rule is setup correctly, so also use that as template for structuring all other rule imports

# Goal: get this to run without errors (doesn't need to produce real results)

if __name__ == "__main__":
    with open('composition/config/config.json', 'r') as inputFile:
        ruleData = json.load(inputFile)
        rule1 = NumNotes(ruleData.get("NumNotes").get("numNotes"))
        rule2 = SharedTone(ruleData.get("SharedTone").get("numShared"))
        rule3 = Interval(ruleData.get("Interval").get("intervals"))
    ruleList = [rule1,rule2,rule3]
    composer = Composer([60, 64, 67], ruleList)
    composer.makeChordProgression()
    composer.printProgressions()
    print(len(composer.progressions),"progressions generated")