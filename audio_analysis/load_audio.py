import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# TODO: read file from audio_files folder

# monophonic example audio
filename = librosa.example('trumpet')

y, sr = librosa.load(filename)
print(y, end='\n')

D = librosa.stft(y)
print(D, end='\n')
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure()
librosa.display.specshow(S_db)
plt.colorbar()
plt.show()