import os
import os.path
import librosa
import pandas as pd

from audio_analysis import analyzer


def _get_sample_data(path: str, filename: str, n_bins_per_sample: int) -> pd.DataFrame:
    S, freq_range, onsets = analyzer.get_audio_info(path)

    note = S[:, onsets[0]:]
    note_df = analyzer.get_note_data(note, n_bins=100, for_ML=True)

    # does not include freq b number
    working_df = note_df.iloc[0:n_bins_per_sample]
    final = working_df.stack(level=0).to_frame().T
    final.columns = final.columns.map(lambda x: '_'.join([str(i) for i in x]))

    note_name = filename[:filename.index('.')]
    target = librosa.note_to_hz(note_name)
    final['target_frequency'] = target

    return final


def format_train_data(train_data_dir: str, n_bins_per_sample: int) -> pd.DataFrame:
    filenames = os.listdir(train_data_dir)
    filepaths = list(map(lambda f: f'{train_data_dir}/{f}', filenames))

    frames = []
    for i in range(len(filepaths)):
        frames.append(_get_sample_data(filepaths[i], filenames[i], n_bins_per_sample=n_bins_per_sample))

    result = pd.concat(frames, ignore_index=True)
    result.insert(0, 'file_name', filenames)

    return result


if __name__ == '__main__':
    ML_dir = os.path.abspath(os.curdir)

    samples_path = f'{ML_dir}/mp3_samples'
    files = os.listdir(samples_path)

    data = format_train_data(samples_path, n_bins_per_sample=10)
    data.to_csv(path_or_buf=f'{ML_dir}/note_data/mp3_notes1.csv', index=False)
