import librosa
import librosa.onset
import numpy as np
import matplotlib.pyplot as plt

# monophonic example audio
# filename = librosa.ex('trumpet')
# y, sr = librosa.load(filename)

# piano sample (better suited for onset pitch detection)
path = 'D:\\Documents\\Github\\generative-music\\audio_files\\test_audio\\test_piano_old.wav'
y, sr = librosa.load(path)
print(f'Sample rate: {sr}')

n_fft = 2048

freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

S = np.abs(librosa.stft(y, n_fft=n_fft))
print(f'Number of frames: {len(S)}')

# frequency domain graph of n-th frame
# n = 1
# n_frame = S[:, n]

# print(f'Number of bins in frame: {len(n_frame)}')

# plt.plot(freqs, n_frame)
# plt.xlabel('Frequency (Hz)')

# plt.ylabel('Magnitude')
# plt.show()

# pitch onset tracking
o_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=1025)
times = librosa.times_like(o_env, sr=sr)
onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
print(f'Detected onsets:\n{onsets}')

plt.plot(times, o_env, label='Onset Strength')
plt.xlabel('Time (seconds)')
plt.vlines(times[onsets], 0, o_env.max(), color='r', alpha=0.9, linestyle='--', label='Onsets')
plt.legend(loc='upper right')
plt.show()