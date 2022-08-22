import os
import librosa
import pandas as pd
# from sdv.lite import TabularPreset
from sdv.tabular import GaussianCopula


def generate_data():
    import os

    file = f'{os.getcwd()}/notes.csv'
    note_data = pd.read_csv(file, header=0)

    # model = TabularPreset(name='FAST_ML', metadata=metadata)
    model = GaussianCopula()
    model.fit(note_data)

    synthetic_data = model.sample(num_rows=100)
    return synthetic_data


if __name__ == '__main__':
    frequencies = librosa.fft_frequencies(sr=22050, n_fft=2048)

    working_df = generate_data()
    working_df.to_csv(path_or_buf=f'{os.getcwd()}/gaussian_copula_notes.csv', index=False)
