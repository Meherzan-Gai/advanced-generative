#imports
from multiprocessing.sharedctypes import Value
from typing import Type
from composer import Composer
from voicing import Voicing
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


def arrProgression(progression,melody):
    progressionIn = progression.clone()
    voicer.setProgression(progressionIn)
    voicer.setMelody(melody)
    voicer.getVoicing()
    voicer.progression.arrChords()


if __name__ == "__main__":
    outputFile = Player('output.mid')
    with open('composition/config/config.json', 'r') as inputFile:
        ruleData = json.load(inputFile)
        melody = ruleData.get("Input").get("melody")
        key = ruleData.get("Input").get("key")
        Chord.setKey(key)
        maxRetries = ruleData.get("Settings").get("maxRetries")
        maxChords = ruleData.get("Settings").get("maxChords")
        rule2 = NumNotes(ruleData.get("NumNotes").get("priority"),ruleData.get("NumNotes").get("numNotes"))
        rule3 = SharedTone(ruleData.get("SharedTone").get("priority"),ruleData.get("SharedTone").get("numShared"))
        rule4 = Interval(ruleData.get("Interval").get("priority"),ruleData.get("Interval").get("intervals"))
        rule1 = FirstChord(ruleData.get("FirstChord").get("priority"),ruleData.get("FirstChord").get("ruleOn"))
        rule5 = BaseNote(ruleData.get("BaseNote").get("priority"),ruleData.get("BaseNote").get("level"))

    ruleList = [rule1,rule2,rule3,rule4,rule5]
    ruleList = sorted(ruleList, key=lambda rule: rule.getPriority()) #SORTS RULES

    composer = Composer(melody, ruleList, maxChords, maxRetries)
    composer.makeChordProgression()
    composer.printProgressions()
    print(len(composer.progressions),"progressions generated")
    print()
    print()
    if (len(composer.progressions) > 0):
        player = Player("composition/player.mid")
        voicer = Voicing()
        programQuit = False
        while (programQuit == False):
            choice = input("Type 1 to hear progressions, 2 to rerun progression generator, or 3 to end the program: ")
            print()
            if (choice == "1"):
                hearQuit = False
                while (hearQuit == False):
                    try:
                        hearOption = input("Choose a progression to hear or type 'q' to quit to the menu: ")
                        print()
                        if (hearOption == 'q'):
                            hearQuit = True
                        else:
                            hearOption = int(hearOption)
                            print("Progression #"+str(hearOption)+" selected:")
                            progressionChosen = composer.progressions[hearOption-1]
                            melodyIn = melody[:]
                            arrProgression(progressionChosen,melodyIn)
                            player.writeMusic(voicer.progression, melodyIn)
                            print(voicer.progression)
                            player.playMusic()

                            progressionQuit = False
                            while(progressionQuit == False):
                                try:
                                    progressionOption = input("Type '1' to download the progression, '2' to transpose the progression up one octave, '3' to transpose the progression AND the melody up one octave, '4' to transpose the progression down one octave, '5' to transpose the progression AND the melody down one octave, or '6' to hear another progression: ")
                                    progressionOption = int(progressionOption)
                                    if (progressionOption == 1):
                                        print()
                                        print("Progression downloading...")
                                        outputFile.writeMusic(voicer.progression,melodyIn)
                                        print()
                                        print("Progression downloaded")
                                        print()
                                    
                                    elif (progressionOption == 2):
                                        voicer.progression.octaveUp()
                                        player.writeMusic(voicer.progression, melodyIn)
                                        print(voicer.progression)
                                        player.playMusic()

                                    elif (progressionOption == 3):
                                        voicer.progression.octaveUp()
                                        for noteIdx in range(0,len(melodyIn),1):
                                            melodyIn[noteIdx]+=12
                                            if (melodyIn[noteIdx]>127):
                                                print("Warning: One or more notes in the melody is above the maximum pitch value of 127 and has been resolved to 127")
                                                print()
                                                melodyIn[noteIdx]=127
                                        player.writeMusic(voicer.progression, melodyIn)
                                        print(voicer.progression)
                                        player.playMusic()    
                                    
                                    elif (progressionOption == 4):
                                        voicer.progression.octaveDown()
                                        player.writeMusic(voicer.progression, melodyIn)
                                        print(voicer.progression)
                                        player.playMusic()

                                    elif (progressionOption == 5):
                                        voicer.progression.octaveDown()
                                        for noteIdx in range(0,len(melodyIn),1):
                                            melodyIn[noteIdx]-=12
                                            if (melodyIn[noteIdx]<0):
                                                print("Warning: One or more notes in the melody is below the minimum pitch value of 0 and has been resolved to 0")
                                                print()
                                                melodyIn[noteIdx]=0
                                        player.writeMusic(voicer.progression, melodyIn)
                                        print(voicer.progression)
                                        player.playMusic()

                                    elif (progressionOption == 6):
                                        progressionQuit = True
                                        print()
                                    
                                    else:
                                        print()
                                        print("Please enter a valid input")
                                        print()
                                        
                                except ValueError:
                                    print()
                                    print("Error: Value not recognized")
                                    print()
                        

                    except IndexError:
                        print("Error: Index is out of range. Please select a number from 1 to",len(composer.progressions))
                        print()
                    
                    except ValueError:
                        print()
                        print("Error: Value not recognized")
                        print()
            
            elif (choice == "2"):
                composer.makeChordProgression()
                composer.printProgressions()

            elif (choice == "3"):
                programQuit=True

            else:
                print("Error: Please enter a valid input")
                print()