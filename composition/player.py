import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from midiutil.MidiFile import MIDIFile
from midiutil import MidiFile


class Player:
    def __init__(self,fileName):
        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffer = 1024    # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.set_volume(0.8)
        self.fileName = fileName


    def writeMusic(self,progression):
        midiPlayer = MIDIFile(
            numTracks = 1,
            removeDuplicates=True,
            deinterleave=True,
            adjust_origin=False,
            file_format = 1,
            ticks_per_quarternote = MidiFile.TICKSPERQUARTERNOTE,
            eventtime_is_ticks=False
        )
        track = 0
        channel = 0
        time = 0
        duration = 1
        volume = 100


        chordIdx = 0
        while(chordIdx < len(progression.chords)):
            noteIdx = 0
            chord = progression.chords[chordIdx]
            while(noteIdx < len(chord.stack)):
                note = chord.stack[noteIdx]
                midiPlayer.addNote(track,channel,note,time,duration,volume)
                noteIdx+=1
            time+=1
            chordIdx+=1
        
        with open(self.fileName, 'wb') as outputFile:
            midiPlayer.writeFile(outputFile)


    def playMusic(self):
        """
        stream music with mixer.music module in blocking manner
        this will stream the sound from disk while playing
        """
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(self.fileName)
            print("Music file %s loaded!" % self.fileName)
        except pygame.error:
            print("File %s not found! (%s)" % (self.fileName, pygame.get_error()))
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)



'''
CODE TO TEST THAT MIDI WAS WRITTEN AND PLAYED

track = 0
channel = 0
pitch = 60
time = 0
duration = 1
volume = 100
midiPlayer.addNote(track,channel,pitch,time,duration,volume)
time = 1
pitch = 61
midiPlayer.addNote(track,channel,pitch,time,duration,volume)
time = 2
pitch = 62
midiPlayer.addNote(track,channel,pitch,time,duration,volume)
time = 3
pitch = 63
midiPlayer.addNote(track,channel,pitch,time,duration,volume)
time = 4
pitch = 64
midiPlayer.addNote(track,channel,pitch,time,duration,volume)
time = 5
pitch = 65
midiPlayer.addNote(track,channel,pitch,time,duration,volume)

with open("composition/player.mid", 'wb') as output_File:
        midiPlayer.writeFile(output_File)

playMusic('composition/player.mid')

'''
