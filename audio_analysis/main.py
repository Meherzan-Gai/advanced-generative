import numpy as np
import pandas as pd
import librosa
import json
import pickle

import analyzer


def format_data_for_ML(note_df, n_bins_per_note):
    working_df = note_df.iloc[0:n_bins_per_note]
    final = working_df.stack(level=0).to_frame().T
    final.columns = final.columns.map(lambda x: '_'.join([str(i) for i in x]))

    return final


def determine_pitches_ML(melody_data, model, n_bins_per_note):
    frames = []
    for note_df in melody_data:
        frames.append(format_data_for_ML(note_df, n_bins_per_note))

    melody_df = pd.concat(frames, ignore_index=True)

    result = model.predict(melody_df)
    return result


def determine_pitches(melody_data, freq_range) -> np.ndarray:
    result = []
    for note in melody_data:
        max_bin_index = np.argmax(note[:, 1])
        result.append(int(note[max_bin_index, 0]))

    return librosa.hz_to_midi(freq_range[result])


def analyze_audio_file(path, n_fft=2048, for_ML=False, model=None, n_bins_per_note=None):
    S, freq_range, onsets = analyzer.get_audio_info(path, n_fft=n_fft)

    melody_data = []
    for i in range(0, len(onsets) - 1):
        note = S[:, onsets[i]:onsets[i + 1]]
        note_data = analyzer.get_note_data(note, n_bins=100, for_ML=for_ML)
        melody_data.append(note_data)

    if for_ML:
        if model is None or n_bins_per_note is None:
            raise Exception('for_ML was set as True, but certain params were not set.')

        return determine_pitches_ML(melody_data, model, n_bins_per_note)
    else:
        return determine_pitches(melody_data, freq_range)


if __name__ == '__main__':
    import time
    import os.path

    PROJECT_ROOT = os.path.dirname(os.path.abspath(os.curdir))
    print(PROJECT_ROOT)

    filepath = f'/app/audio_files/test_audio/test_piano_old.wav'
    # filepath = f'{PROJECT_ROOT}/audio_files/test_audio/test_piano_old.wav'

    for_ML = False

    model_name = '20220826-164627'
    # model_path = f'{PROJECT_ROOT}/audio_analysis/ML/models/{model_name}_rfr_model.pkl'
    model_path = f'/app/audio_analysis/ML/models/{model_name}_rfr_model.pkl'

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    m = analyze_audio_file(filepath, for_ML=for_ML, model=model, n_bins_per_note=10).tolist()

    print(librosa.midi_to_note(m))

    timestr = time.strftime("%Y%m%d-%H%M%S")
    # with open(f'{PROJECT_ROOT}/midi_melodies/{timestr}_{os.path.basename(filepath)}.json', 'w') as out:
    # with open(f'/app/midi_melodies/{timestr}_{os.path.basename(filepath)}.json', 'w') as out:
    with open(f'/app/midi_melodies/melody.json', 'w') as out:
        json.dump(m, out)
