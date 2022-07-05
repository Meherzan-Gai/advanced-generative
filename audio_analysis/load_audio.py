import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# monophonic example audio
filename = librosa.ex('trumpet')
y, sr = librosa.load(filename)

n_fft = 2048

freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
freqs_mHz = [i / 1000 for i in freqs]

S = np.abs(librosa.stft(y))

print(S)
print(freqs)

# frequency domain graph of n-th frequency bin
n = 1

plt.plot(freqs_mHz, S[:, n])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()