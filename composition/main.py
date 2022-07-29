#imports
from composer import Composer
from progression import Progression
from chord import Chord
from rules.sharedtone import SharedTone
from rules.numnotes import NumNotes
from rules.interval import Interval
import json
from pcsets.pcset import PcSet as ps
from player import Player


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
    composer = Composer([60, 63, 67, 68, 67, 60, 59], ruleList)
    composer.makeChordProgression()
    print(len(composer.progressions),"progressions generated")

    print()
    print()
    if (len(composer.progressions) > 0):
        player = Player("composition/player.mid")
        while True:
            try:
                progressionChosen = int(input("Choose a progression to hear: "))
                player.writeMusic(composer.progressions[progressionChosen - 1])
                player.playMusic()
                break
            except IndexError:
                print("Index is out of range. Please select a number from 1 to:",len(composer.progressions))
