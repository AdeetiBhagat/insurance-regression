import warnings
warnings.simplefilter('ignore') # to suppress unnecessary warnings

import io

import pandas as pd
import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    print(df.head(2))
    print("Size of Dataset:", len(df))
    print(df.info())
    print(df.head())
    df = pd.get_dummies(df, drop_first=True)
    df = df.dropna()
    X = df.drop('charges', axis=1)
    y = df['charges']
    return X, y

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return model, mse

def main():
    data = load_data('insurance-1.csv')
    X, y = preprocess_data(data)
    model, mse = train_model(X, y)
    print(f'Model trained with MSE: {mse}')

if __name__ == "__main__":
    main()
