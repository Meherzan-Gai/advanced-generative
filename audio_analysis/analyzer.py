import librosa
import librosa.onset
import numpy as np


def get_audio_info(path, n_fft=2048):
    y, sr = librosa.load(path)

    S = np.abs(librosa.stft(y, n_fft=n_fft))
    freq_range = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    o_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=S.shape[0])
    onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='frames', pre_max=3, post_max=3, pre_avg=3,
                                        post_avg=5)

    # onset strength graph
    # import matplotlib.pyplot as plt
    # times = librosa.times_like(o_env, sr=sr)
    # plt.plot(times, o_env, label='Onset Strength')
    # plt.xlabel('Time (seconds)')
    # plt.vlines(times[onsets], 0, o_env.max(), color='r', alpha=0.9, linestyle='--', label='Onsets')
    # plt.legend(loc='upper right')
    # plt.show()

    return S, freq_range, onsets


def get_note_data(note, num_bins=3):
    # list of the maximum values of each bin across the frames
    bin_maxes = np.amax(note, axis=1)
    # "num_bins"th highest bins ordered from least to greatest
    bins = np.argpartition(bin_maxes, range(len(bin_maxes) - num_bins, len(bin_maxes)))[-num_bins:]

    bin_mags = note[bins, :]
    mag_maxes = np.max(bin_mags, axis=1)
    mag_mins = np.min(bin_mags, axis=1)
    # average magnitude of each bin across the frames
    mag_means = np.mean(bin_mags, axis=1)
    mag_stds = np.std(bin_mags, axis=1)

    bin_diffs = np.diff(bin_mags)
    diff_avgs = np.mean(bin_diffs, axis=1)
    diff_stds = np.std(bin_diffs, axis=1)

    data = np.concatenate(([bins], [mag_maxes], [mag_mins], [mag_means], [mag_stds], [diff_avgs], [diff_stds]), axis=0)
    return data
