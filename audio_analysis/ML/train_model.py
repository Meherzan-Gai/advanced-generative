import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


if __name__ == '__main__':
    import os

    notes = f'{os.getcwd()}/notes.csv'
    test_df = pd.read_csv(notes, header=0)

    gc_notes = f'{os.getcwd()}/gaussian_copula_notes.csv'
    train_df = pd.read_csv(gc_notes, header=0)

    X_test, y_test = test_df.iloc[:, 0:71], test_df.iloc[:, 70]
    X_train, y_train = train_df.iloc[:, 0:71], train_df.iloc[:, 70]

    # TODO: Use GridSearchCV to evaluate different param values

    # fitting with synthetic data
    rfr = RandomForestRegressor(n_estimators=100, max_depth=None)
    rfr.fit(X_train, y_train)

    # testing with real data
    y_predict = rfr.predict(X_test)

    mse = mean_squared_error(y_test, y_predict)
    rmse = mse**.5

    # current error is bad likely because synthetic is yet to be adjusted
    print(mse)
    print(rmse)
