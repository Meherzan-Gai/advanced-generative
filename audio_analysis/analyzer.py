import os.path
import librosa
import librosa.onset
import numpy as np
import pandas as pd

def get_audio_info(path, n_fft=2048):
    y, sr = librosa.load(path)
    
    S = np.abs(librosa.stft(y, n_fft=n_fft))
    freq_range = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    o_env = librosa.onset.onset_strength(y=y, sr=sr, max_size=S.shape[0])
    onsets = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr, units='frames', pre_max=3, post_max=3, pre_avg=3, post_avg=5)

    # onset strength graph
    import matplotlib.pyplot as plt
    times = librosa.times_like(o_env, sr=sr)
    plt.plot(times, o_env, label='Onset Strength')
    plt.xlabel('Time (seconds)')
    plt.vlines(times[onsets], 0, o_env.max(), color='r', alpha=0.9, linestyle='--', label='Onsets')
    plt.legend(loc='upper right')
    plt.show()

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

def analyze(path):
    S, freq_range, onsets = get_audio_info(path)

    note = S[:, onsets[0]:onsets[1]]
    data = get_note_data(note, num_bins=30)

    df = pd.DataFrame(data.T, columns=['Frequency Bin', 'Max. Magnitude', 'Min. Magnitude', 'Avg. Magnitude', 'SD Magnitude', 'Avg. Difference', 'SD Difference'])
    df.sort_values('Avg. Magnitude', inplace=True, ascending=False)

    working_df = df.iloc[0:5]
    results = {}
    for i in range(0, working_df.shape[0]):
        for col_name in working_df.columns[1:]:
            freq_bin = int(working_df.iloc[i]['Frequency Bin'])
            results[f'Bin {freq_bin} {col_name}'] = working_df.iloc[i][col_name]
    final = pd.DataFrame([results])

    basename = os.path.basename(path)
    note_name = basename[:basename.index('.')]
    target = librosa.note_to_hz(note_name)
    final['Target'] = target

    return final

if __name__ == '__main__':
    import os
    # temp path
    path = os.getcwd() + '/audio_analysis/samples/C4.wav'
    print(analyze(path))