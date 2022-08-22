import os
import os.path
import librosa
import pandas as pd

import analyzer


def get_sample_data(path, filename, num_bins):
    S, freq_range, onsets = analyzer.get_audio_info(path)

    note = S[:, onsets[0]:]
    data = analyzer.get_note_data(note, num_bins=100)

    df = pd.DataFrame(data.T,
                      columns=['frequency_bin', 'max_magnitude', 'min_magnitude', 'avg_magnitude', 'sd_magnitude',
                               'avg_difference', 'sd_difference'])
    df.sort_values('avg_magnitude', inplace=True, ascending=False, ignore_index=True)

    # does not include freq bin number
    working_df = df.iloc[0:num_bins]
    final = working_df.stack(level=0).to_frame().T
    final.columns = final.columns.map(lambda x: '_'.join([str(i) for i in x]))

    note_name = filename[:filename.index('v')]
    target = librosa.note_to_hz(note_name)
    final['target_frequency'] = target

    return final


def format_train_data(num_bins=10):
    # notes in sample folders are just for testing
    for root, dirs, files in os.walk(f'{os.getcwd()}/samples'):
        pass
    paths = list(map(lambda file: f'{root}/{file}', files))

    frames = []
    for i in range(len(paths)):
        frames.append(get_sample_data(paths[i], files[i], num_bins=num_bins))

    frequencies = librosa.fft_frequencies(sr=22050, n_fft=2048)

    result = pd.concat(frames, ignore_index=True)

    # columns to view bins/hz in note notation
    # def bin_to_note(b):
    #     return librosa.hz_to_note(frequencies[int(b)])
    #
    # for i in range(0, num_bins):
    #     result[f'{i}_note'] = result[f'{i}_frequency_bin'].apply(bin_to_note)
    # result['target_note'] = result['target_frequency'].apply(librosa.hz_to_note)

    return result


if __name__ == '__main__':
    data = format_train_data(num_bins=10)
    print(data)
    data.to_csv(path_or_buf=f'{os.getcwd()}/notes.csv', index=False)
