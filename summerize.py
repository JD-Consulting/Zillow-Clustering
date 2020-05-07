import pandas as pd
import numpy as np

# returns a series for the summerize
def convert_to_series(df):
    '''
    helper function for the summarize function
    that converts a dataframe into a series and grabs 
    the value counts from that dataframe
    '''
    series = pd.Series([])
    for _, col in enumerate(df.columns.values):
        if df[col].dtype == 'object':
            col_count = df[col].value_counts()
        else:
            col_count = df[col].value_counts(bins=10)
        series = series.append(col_count)
    return series


# prints a summerization of the dataframe
def summarize_data(df):
    print("******** Info")
    df.info()
    print()
    print("******** Shape {}".format(df.shape))
    print()
    print("******** Describe")      
    print(df.describe)
    print()
    print("******** Value Counts")      
    print(convert_to_series(df))





