#imports
from composer import Composer
from voicing import VoicingRule
from progression import Progression
from chord import Chord
from rules.rule import Rule
from rules.sharedtone import SharedTone
from rules.numnotes import NumNotes
from rules.interval import Interval
from rules.firstchord import FirstChord
from rules.basenote import BaseNote
import json
from pcsets.pcset import PcSet as ps
from player import Player


# use this as a template for importing all your classes
# SharedTone rule is setup correctly, so also use that as template for structuring all other rule imports

# Goal: get this to run without errors (doesn't need to produce real results)

if __name__ == "__main__":
    with open('composition/config/config.json', 'r') as inputFile:
        ruleData = json.load(inputFile)
        rule2 = NumNotes(ruleData.get("NumNotes").get("priority"),ruleData.get("NumNotes").get("numNotes"))
        rule3 = SharedTone(ruleData.get("SharedTone").get("priority"),ruleData.get("SharedTone").get("numShared"))
        rule4 = Interval(ruleData.get("Interval").get("priority"),ruleData.get("Interval").get("intervals"))
        rule1 = FirstChord(ruleData.get("FirstChord").get("priority"),ruleData.get("FirstChord").get("ruleOn"))
        rule5 = BaseNote(ruleData.get("BaseNote").get("priority"),ruleData.get("BaseNote").get("level"))

    ruleList = [rule1,rule2,rule3,rule4,rule5]
    ruleList = sorted(ruleList, key=lambda rule: rule.getPriority()) #SORTS RULES

    #melody = [60, 63, 67, 68, 67, 60, 59]
    melody = [n+24 for n in [60,66,67]]
    composer = Composer(melody, ruleList)
    composer.makeChordProgression()
    composer.printProgressions()
    print(len(composer.progressions),"progressions generated")
    print()
    print()
    if (len(composer.progressions) > 0):
        player = Player("composition/player.mid")
        while True:
            try:
                progressionChosen = int(input("Choose a progression to hear: "))
                voicer = VoicingRule(composer.progressions[progressionChosen-1],melody)
                voicer.getVoicing()
                for chord in voicer.progression.chords:
                    print (chord.stack)
                player.writeMusic(voicer.progression, melody)
                player.playMusic()
                break
            except IndexError:
                print("Index is out of range. Please select a number from 1 to:",len(composer.progressions))