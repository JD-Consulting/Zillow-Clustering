import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
    
    
def show_distribution(df):
    newdf = pd.DataFrame()
    for col in df:
        if col in df.corr() >= 0.5:
            newdf[f'{col}'] = df[f'{col}']
    return sns.pairplot(newdf, palette='hus1')
        
        
    sns.pairplot(df, palette='hus1', corner=True, diag_kind='hist')
    plt.show()



    for col in df:
        if df[f'{col}'].isna().sum() > 0:
            df[f'{col}'] = df[f'{col}'].fillna(df[f'{col}'].median())
    return df


