import os
import os.path
import librosa
import numpy as np
import pandas as pd

import analyzer

def format_train_data(path, filename):
    S, freq_range, onsets = analyzer.get_audio_info(path)

    note = S[:, onsets[0]:]
    data = analyzer.get_note_data(note, num_bins=30)

    df = pd.DataFrame(data.T, columns=['Frequency Bin', 'Max. Magnitude', 'Min. Magnitude', 'Avg. Magnitude', 'SD Magnitude', 'Avg. Difference', 'SD Difference'])
    df.sort_values('Avg. Magnitude', inplace=True, ascending=False)

    # does not include freq bin number
    working_df = df.iloc[0:5, 1:]
    final = working_df.unstack().to_frame().sort_index(level=1).T
    final.columns = final.columns.map(' '.join)

    note_name = filename[:filename.index('.')]
    target = librosa.note_to_hz(note_name)
    final['Target Frequency'] = target

    return final

def main():
    # notes in sample folders are just for testing
    for root, dirs, files in os.walk(os.getcwd() + '/audio_analysis/samples'):
        pass

    paths = list(map(lambda file: f'{root}/{file}', files))
    for path in paths:
        print(format_train_data(path))

if __name__ == '__main__':
    main()