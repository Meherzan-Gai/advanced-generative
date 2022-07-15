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

#if __name__ == "main":
print("hi")
with open('composition/config/config.json', 'r') as inputFile:
    ruleData = json.load(inputFile)
    rule1 = SharedTone(ruleData.get("SharedTone").get("numShared"))
rule2 = NumNotes(3)
rule3 = Interval([3,4])
ruleList = [rule2,rule3]
composer = Composer([60, 64, 67], ruleList)
composer.makeChordProgression()
#composer.printProgressions()
print(len(composer.progressions),"progressions generated")

