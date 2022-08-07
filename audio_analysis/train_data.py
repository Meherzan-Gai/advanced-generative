import os
import os.path
import pandas as pd
import analyzer

def main():
    # notes in sample folders are just for testing
    for root, dirs, files in os.walk(os.getcwd() + '/audio_analysis/samples'):
        pass

    paths = list(map(lambda file: f'{root}/{file}', files))

if __name__ == '__main__':
    main()