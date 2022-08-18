import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris

if __name__ == '__main__':
    import os
    file = f'{os.getcwd()}/audio_analysis/notes.csv'
    note_dataset = pd.read_csv(file, header=0)
    
    X, y = note_dataset.iloc[:, 0:35], note_dataset.iloc[:, 35]
    
