import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


def eval_model(model, X_test, y_test):
    y_predict = model.predict(X_test)

    mse = mean_squared_error(y_test, y_predict)
    rmse = mse ** 0.5

    print("MSE: ", mse)
    print("R-MSE: ", rmse)

    score = r2_score(y_test, y_predict)

    print("Score: ", score)


def create_model(input_data: pd.DataFrame, use_fake_data=False, fake_data: pd.DataFrame = None):
    X_train, y_train, X_test, y_test = None, None, None, None
    if not use_fake_data:
        # test/train split
        pass
    else:
        if fake_data is None:
            raise Exception('use_fake_data is True but no fake_data was specified')

        X_test, y_test = input_data.iloc[:, 0:input_data.shape[1] - 1], input_data.iloc[:, input_data.shape[1] - 1]
        X_train, y_train = fake_data.iloc[:, 0:fake_data.shape[1] - 1], fake_data.iloc[:, fake_data.shape[1] - 1]

    rfr = RandomForestRegressor(n_estimators=100, max_depth=None)
    rfr.fit(X_train, y_train)

    eval_model(rfr, X_test, y_test)

    return rfr


if __name__ == '__main__':
    ML_dir = os.path.abspath(os.curdir)

    notes_df = pd.read_csv(f'{ML_dir}/note_data/UPKW+mp3_notes.csv', header=0)
    sdv_notes_df = pd.read_csv(f'{ML_dir}/note_data/sdv_notes.csv', header=0)

    m = create_model(notes_df, use_fake_data=True, fake_data=sdv_notes_df)

    print("Would you like to save this model? [y/n]")
    choice = input()

    if choice == 'y':
        import time
        import pickle

        timestr = time.strftime("%Y%m%d-%H%M%S")
        model_name = f'{timestr}_rfr_model.pkl'

        with open(f'{ML_dir}/models/{model_name}', 'wb') as f:
            pickle.dump(m, f)

    elif choice == 'n':
        exit(0)

    # TODO: Use GridSearchCV to evaluate different param values
