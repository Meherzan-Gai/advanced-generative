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

    df = pd.DataFrame(data.T, columns=['FreqBin', 'MaxMag', 'MinMag', 'AvgMag', 'SDMag', 'AvgDiff', 'SDDiff'])
    df.sort_values('AvgMag', inplace=True, ascending=False, ignore_index=True)

    # does not include freq bin number
    working_df = df.iloc[0:5]
    final = working_df.stack(level=0).to_frame().T
    final.columns = final.columns.map(lambda x: '_'.join([str(i) for i in x]))

    note_name = filename[:filename.index('v')]
    target = librosa.note_to_hz(note_name)
    final['TrgtFreq'] = target

    return final

def main():
    # notes in sample folders are just for testing
    for root, dirs, files in os.walk(f'{os.getcwd()}/audio_analysis/samples'):
        pass
    paths = list(map(lambda file: f'{root}/{file}', files))

    frames = []
    for i in range(len(paths)):
        frames.append(format_train_data(paths[i], files[i]))
    
    result = pd.concat(frames, ignore_index=True)
    print(result)

    result.to_csv(path_or_buf=f'{os.getcwd()}/audio_analysis/notes.csv', index=False)

if __name__ == '__main__':
    main()