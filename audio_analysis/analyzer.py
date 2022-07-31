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

if __name__ == '__main__':
    import os, pdb
    # temp path
    path = os.getcwd() + '/audio_files/test_audio/test_piano_old.wav'
    S, freq_range, onsets = get_audio_info(path)

    note = S[:, onsets[1]:onsets[2]]
    data = get_note_data(note, num_bins=30)

    import pandas as pd
    df = pd.DataFrame(data.T, columns=['Frequency Bin', 'Average Magnitude', 'Average Difference of Magnitude'])
    # df.sort_values('Average Magnitude', inplace=True, ascending=False)
    print(df)

    # df['Note'] = df['Frequency Bin'].apply(lambda x: librosa.hz_to_note(freq_range[int(x)]))
    working_df = df.iloc[0:5]
    results = {}
    for i in range(0, working_df.shape[0]):
        results[f'Bin {i} Average Magnitude'] = working_df.iloc[i]['Average Magnitude']
        results[f'Bin {i} Average Diff of Mag'] = working_df.iloc[i]['Average Difference of Magnitude']
    
    final = pd.DataFrame([results])
    final['Target'] = 391.995
    print(final)

    # print(df)