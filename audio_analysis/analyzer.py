import librosa
import librosa.onset
import numpy as np


def get_audio_info(path, n_fft=2048):
    y, sr = librosa.load(path)

    S = np.abs(librosa.stft(y, n_fft=n_fft))
    freq_range = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    o_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=S.shape[0])
    onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='frames', pre_max=3, post_max=3, pre_avg=3, post_avg=5)

    # onset strength graph
    # import matplotlib.pyplot as plt
    # times = librosa.times_like(o_env, sr=sr)
    # plt.plot(times, o_env, label='Onset Strength')
    # plt.xlabel('Time (seconds)')
    # plt.vlines(times[onsets], 0, o_env.max(), color='r', alpha=0.9, linestyle='--', label='Onsets')
    # plt.legend(loc='upper right')
    # plt.show()

    return S, freq_range, onsets


def get_note_data(note, n_bins, for_ML=False) -> np.ndarray:
    # list of the maximum values of each bin across the frames
    bin_maxes = np.amax(note, axis=1)
    # nth highest bins ordered from least to greatest
    bins = np.argpartition(bin_maxes, range(len(bin_maxes) - n_bins, len(bin_maxes)))[-n_bins:]

    bin_magnitudes = note[bins, :]

    avg_magnitudes = np.mean(bin_magnitudes, axis=1)

    if not for_ML:
        data = np.concatenate(([bins], [avg_magnitudes]), axis=0)
        return data.T

    max_magnitudes = np.max(bin_magnitudes, axis=1)
    min_magnitudes = np.min(bin_magnitudes, axis=1)
    std_magnitudes = np.std(bin_magnitudes, axis=1)

    bin_differences = np.diff(bin_magnitudes)
    avg_differences = np.mean(bin_differences, axis=1)
    std_differences = np.std(bin_differences, axis=1)

    data = np.concatenate(([bins], [max_magnitudes], [min_magnitudes], [avg_magnitudes], [std_magnitudes], [avg_differences], [std_differences]), axis=0)
    return data
