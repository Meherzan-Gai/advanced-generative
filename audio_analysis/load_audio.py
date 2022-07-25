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
print(f'Num of bins: {len(freqs)}')

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
onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='frames')
# print(f'Detected onsets:\n{onsets}')
# S.shape[1]

# ML PARAMS
# for each bin in each frame, get the magnitude when it was the highest
# then sort those bins from highest to lowest
# n highest bins are selected as the bins: "max bin"
# param: average magnitude of each max bin over each frame
# param: average difference of each max bin from one frame to another

curr_note = S[:, onsets[0]:onsets[1]]
print(curr_note.shape[0])

# array of max values of each bin
arr = np.amax(curr_note, axis=1)

num_highest = 3
max_ind = np.argsort(arr)[-num_highest:]
print(max_ind)


# testing peak pick
# pre_max
# post_max