#imports
from composer import Composer
from rules.sharedtone import SharedTone
from rules.numnotes import NumNotes
from rules.interval import Interval

print(SharedTone, Interval, NumNotes)

# use this as a template for importing all your classes
# SharedTone rule is setup correctly, so also use that as template for structuring all other rule imports

# Goal: get this to run without errors (doesn't need to produce real results)
rule1 = SharedTone(1)
rule2 = NumNotes(3)
rule3 = Interval([3,4])
ruleList = [rule1,rule2]
composer = Composer([60, 64], ruleList)
composer.makeChordProgression()
composer.printProgressions()