import numpy as np
import librosa
import json

import analyzer


def determine_pitches(melody, freq_range) -> np.ndarray:
    result = []
    for note in melody:
        max_bin_index = np.argmax(note[:, 1])
        result.append(int(note[max_bin_index, 0]))

    return librosa.hz_to_midi(freq_range[result])


def determine_pitches_ML(melody_data):
    pass


# if for_ML is true, it should build the full note_data df
# should
def analyze_audio_file(path, n_fft=2048, for_ML=False):
    S, freq_range, onsets = analyzer.get_audio_info(path, n_fft=n_fft)

    melody_data = []
    for i in range(0, len(onsets) - 1):
        note = S[:, onsets[i]:onsets[i + 1]]
        note_data = analyzer.get_note_data(note, n_bins=100, for_ML=for_ML)
        melody_data.append(note_data)

    if for_ML:
        determine_pitches_ML(melody_data)
        raise Exception('Not implemented yet.')
    else:
        return determine_pitches(melody_data, freq_range)


if __name__ == '__main__':
    # Range of allowed notes is C3-C5
    # Bounds for synthetic data
    # Frequency: [130.8127826502993, 523.2511306011972]
    # Bin:

    import os.path

    PROJECT_ROOT = os.path.dirname(os.path.abspath(os.curdir))

    filepath = f'{PROJECT_ROOT}/audio_files/test_audio/test_piano_old.wav'

    m = analyze_audio_file(filepath, for_ML=False).tolist()
    print(librosa.midi_to_note(m))

    with open(f'{PROJECT_ROOT}/midi_melodies/{os.path.basename(filepath)}.json', 'w') as out:
        json.dump(m, out)
