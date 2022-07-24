import pygame
from midiutil.MidiFile import MIDIFile
from midiutil import MidiFile

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




def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file %s loaded!" % music_file)
    except pygame.error:
        print("File %s not found! (%s)" % (music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)


freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)
# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)
#for music_file in music_files():


play_music('composition/player.mid')