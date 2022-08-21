import os
import librosa
import pandas as pd
# from sdv.lite import TabularPreset
from sdv.tabular import GaussianCopula

def generate_data():
    import os

    file = f'{os.getcwd()}/notes.csv'
    note_data = pd.read_csv(file, header=0)

    metadata = {
        'fields': {
            '0_frequency_bin': {'type': 'numerical', 'subtype': 'float'},
            '0_max_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '0_min_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '0_avg_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '0_sd_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '0_avg_difference': {'type': 'numerical', 'subtype': 'float'},
            '0_sd_difference': {'type': 'numerical', 'subtype': 'float'},
            '1_frequency_bin': {'type': 'numerical', 'subtype': 'float'},
            '1_max_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '1_min_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '1_avg_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '1_sd_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '1_avg_difference': {'type': 'numerical', 'subtype': 'float'},
            '1_sd_difference': {'type': 'numerical', 'subtype': 'float'},
            '2_frequency_bin': {'type': 'numerical', 'subtype': 'float'},
            '2_max_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '2_min_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '2_avg_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '2_sd_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '2_avg_difference': {'type': 'numerical', 'subtype': 'float'},
            '2_sd_difference': {'type': 'numerical', 'subtype': 'float'},
            '3_frequency_bin': {'type': 'numerical', 'subtype': 'float'},
            '3_max_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '3_min_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '3_avg_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '3_sd_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '3_avg_difference': {'type': 'numerical', 'subtype': 'float'},
            '3_sd_difference': {'type': 'numerical', 'subtype': 'float'},
            '4_frequency_bin': {'type': 'numerical', 'subtype': 'float'},
            '4_max_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '4_min_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '4_avg_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '4_sd_magnitude': {'type': 'numerical', 'subtype': 'float'},
            '4_avg_difference': {'type': 'numerical', 'subtype': 'float'},
            '4_sd_difference': {'type': 'numerical', 'subtype': 'float'},
            'target_frequency': {'type': 'numerical', 'subtype': 'float'}
        },
        'constraints': [],
        'path': 'notes.csv'
    }

    # model = TabularPreset(name='FAST_ML', metadata=metadata)
    model = GaussianCopula()
    model.fit(note_data)

    synthetic_data = model.sample(num_rows=100)
    return synthetic_data


if __name__ == '__main__':
    frequencies = librosa.fft_frequencies(sr=22050, n_fft=2048)

    def bin_to_note(bin):
        return librosa.hz_to_note(frequencies[int(bin)])

    working_df = generate_data()
    working_df['0_note'] = working_df['0_frequency_bin'].apply(bin_to_note)
    working_df['1_note'] = working_df['1_frequency_bin'].apply(bin_to_note)
    working_df['2_note'] = working_df['2_frequency_bin'].apply(bin_to_note)
    working_df['3_note'] = working_df['3_frequency_bin'].apply(bin_to_note)
    working_df['4_note'] = working_df['4_frequency_bin'].apply(bin_to_note)
    working_df['target_note'] = working_df['target_frequency'].apply(librosa.hz_to_note)

    print(working_df.iloc[:, -6:])
    working_df.to_csv(path_or_buf=f'{os.getcwd()}/gaussian_copula_notes.csv', index=False)
