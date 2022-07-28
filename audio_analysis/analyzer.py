import librosa
import librosa.onset

import numpy as np

def get_audio_info(path, n_fft=2048):
    y, sr = librosa.load(path)
    
    S = np.abs(librosa.stft(y, n_fft=n_fft))
    freq_range = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    o_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=S.shape[0])
    onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='frames')
    return S, freq_range, onsets

def get_note_data(note, num_highest=3):
    a = np.amax(note, axis=1)
    return a

if __name__ == '__main__':
    import os
    # temp path
    path = os.getcwd() + '/audio_files/test_audio/test_piano_old.wav'
    S, freq_range, onsets = get_audio_info(path)

    note = S[:, onsets[0]:onsets[1]]
    a = np.argpartition(get_note_data(note))
    print(a)