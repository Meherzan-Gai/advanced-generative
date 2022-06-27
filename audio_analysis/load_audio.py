import librosa
import numpy as np

# temp input until user recording can be processed
# monophonic example audio
filename = librosa.example('trumpet')

y, sr = librosa.load(filename)
print(y, end='\n')

D = np.abs(librosa.stft(y))
print(D, end='\n')
