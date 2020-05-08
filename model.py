import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from math import sqrt, log



def calculate_logerror(actual, predicted, df):
    df[actual] = np.log(df[actual])
    df[predicted] = np.log(df[predicted])
    df['logerror'] = df[predicted] - df[actual]
    return df
    
    