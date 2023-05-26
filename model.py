from sklearn import linear_model
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def read_dataset():
    df = pd.read_csv('generated_data.csv')
    sns.lineplot(x="credits", y="hours", data=df)
    plt.show()


def model():
    reg = linear_model.LinearRegression()


read_dataset()