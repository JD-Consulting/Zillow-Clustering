# Wrangling
import pandas as pd
import numpy as np


# removing missing rows and columns 

def remove_columns(df, cols_to_remove):  
    '''
    helper function to remove unneeded columns
    '''
    df = df.drop(columns=cols_to_remove)
    return df



def handle_missing_values(df, prop_required_column = .5, prop_required_row = .60):
    '''
    helper function for data prep mother function that removes
    rows missing 50% of data and columns missing up to 50% of data
    '''
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df    


def data_prep(df, cols_to_remove=[], prop_required_column=.5, prop_required_row=.75):
    '''
     input a dataframe and a specific column or default parses all columns in dataframe 
     removes columns missing 50% of data and rows missing up to 75% of data
    '''
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)
    return df    




# outlier detection with IQR as a filter
def get_upper_outliers(s, k):
    '''
    Given a series and a cutoff value, k, returns the upper outliers for the
    series.

    The values returned will be either 0 (if the point is not an outlier), or a
    number that indicates how far away from the upper bound the observation is.
    '''
    q1, q3 = s.quantile([.25, .75])
    iqr = q3 - q1
    upper_bound = q3 + k * iqr
    return s.apply(lambda x: max([x - upper_bound, 0]))


def add_upper_outlier_columns(df, k):
    '''
    Add a column with the suffix _outliers for all the numeric columns
    in the given dataframe.
    '''
    # outlier_cols = {col + '_outliers': get_upper_outliers(df[col], k)
    #                 for col in df.select_dtypes('number')}
    # return df.assign(**outlier_cols)

    for col in df.select_dtypes('number'):
        df[col + '_outliers'] = get_upper_outliers(df[col], k)

    return df    

# needed
def zillow_single_unit_prop(df):
    criteria_1=df.calculatedfinishedsquarefeet>500
    criteria_2=df.bathroomcnt>0
    criteria_3=df.bedroomcnt>0
    criteria_4=df.calculatedfinishedsquarefeet<8_000
    criteria_5=df.bathroomcnt<6
    criteria_6=df.bedroomcnt<6
    df=df[(criteria_1) & (criteria_2) & (criteria_3) & (criteria_4) & (criteria_5) & (criteria_6)]
    return df

# needed
def fill_missing_values(df,fill_value):
    df.fillna(fill_value)
    return df

# Needed
def change_data_to_object(df, cols):
    """
    takes a dataframe and a list of columns and it 
    converts the columns listed that are in the dataframe into 
    objects in the same dataframe
    """
    newdf = pd.DataFrame(df, columns=cols)
    df = df.drop(columns=cols)
    newdf = newdf.astype(object)
    df = pd.concat([df, newdf], axis=1)
    return df

# Needed
def change_data_to_int(df, cols):
    """
    takes a dataframe and a list of columns and it 
    converts the columns listed that are in the dataframe into 
    objects in the same dataframe
    """
    newdf = pd.DataFrame(df, columns=cols)
    df = df.drop(columns=cols)
    newdf = newdf.astype(int)
    df = pd.concat([df, newdf], axis=1)
    return df

# Needed
def the_master_imputer(df):
    for col in df:
        if df[f'{col}'].isna().sum() > 0:
            df[f'{col}'] = df[f'{col}'].fillna(df[f'{col}'].median())
    return df
    
# Needed    
def percent_of_values_missing(df):
    return round(df.isna().sum()/len(df)*100,2)