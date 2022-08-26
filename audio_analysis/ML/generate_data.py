import os
import pandas as pd
from sdv.tabular import GaussianCopula


def generate_data(note_data) -> pd.DataFrame:

    # notable issues:
    # frequency bins don't line up with target freqs
    # bin values in a sample should be close to each other or multiples
    model = GaussianCopula()
    model.fit(note_data)

    synthetic_data = model.sample(num_rows=500)
    return synthetic_data


if __name__ == '__main__':
    ML_dir = os.path.abspath(os.curdir)
    UPKW_file = f'{ML_dir}/UprightPianoKW_notes.csv'
    mp3_file = f'{ML_dir}/mp3_notes.csv'

    UPKW_df = pd.read_csv(UPKW_file, header=0)
    mp3_df = pd.read_csv(mp3_file, header=0)

    combined_df = pd.concat([UPKW_df, mp3_df], ignore_index=True).iloc[:, 1:]

    working_df = generate_data(combined_df)
    working_df.to_csv(path_or_buf=f'{ML_dir}/sdv_notes.csv', index=False)
