from sklearn import linear_model
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def plot_data():
    df = read_dataset()
    sns.lineplot(x="credits", y="hours", data=df)
    plt.show()


def read_dataset():
    df = pd.read_csv('generated_data.csv')
    return df


def model_build():
    df = read_dataset()
    hours = np.array(df['hours'].values)
    credits = np.array(df['credits'].values).reshape((-1, 1))
    # print(hours)
    # print(credits)
    model = linear_model.LinearRegression()
    model = model.fit(credits, hours)
    intercept = model.intercept_
    slope = model.coef_

    # print(f"intercept: {intercept}")
    # print(f"slope: {slope} ")
    # print(f"score: {model.score(credits, hours)}")
    return [intercept, slope]


def prediction(x):
    [intercept, slope] = model_build()
    y = slope * x + intercept
    return y[0]
