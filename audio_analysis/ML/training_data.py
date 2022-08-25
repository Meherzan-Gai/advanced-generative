import os
import os.path
import librosa
import pandas as pd

from audio_analysis import analyzer


def get_sample_data(path: str, filename: str, n_bins_per_sample) -> pd.DataFrame:
    S, freq_range, onsets = analyzer.get_audio_info(path)

    note = S[:, onsets[0]:]
    note_data = analyzer.get_note_data(note, n_bins=100)

    df = pd.DataFrame(note_data.T,
                      columns=['frequency_bin', 'max_magnitude', 'min_magnitude', 'avg_magnitude', 'sd_magnitude',
                               'avg_difference', 'sd_difference'])
    df.sort_values('avg_magnitude', inplace=True, ascending=False, ignore_index=True)

    # does not include freq bin number
    working_df = df.iloc[0:n_bins_per_sample]
    final = working_df.stack(level=0).to_frame().T
    final.columns = final.columns.map(lambda x: '_'.join([str(i) for i in x]))

    note_name = filename[:filename.index('v')]
    target = librosa.note_to_hz(note_name)
    final['target_frequency'] = target
    final['file_name'] = filename

    return final


def format_train_data(n_bins_per_sample=10):
    # notes in sample folders are just for testing
    for root, dirs, files in os.walk(f'{os.getcwd()}/samples'):
        pass
    paths = list(map(lambda file: f'{root}/{file}', files))

    frames = []
    for i in range(len(paths)):
        frames.append(get_sample_data(paths[i], files[i], n_bins_per_sample=n_bins_per_sample))

    result = pd.concat(frames, ignore_index=True)

    return result


if __name__ == '__main__':
    data = format_train_data(n_bins_per_sample=10)
    print(data)
    data.to_csv(path_or_buf=f'{os.getcwd()}/notes.csv', index=False)
