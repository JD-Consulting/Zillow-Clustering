import os.path
import pandas as pd
import numpy as np

import env

def csv_exist():
    return os.path.isfile('zillow_data.csv')

def get_data_from_zillow():
    query ='''
        select 
            prop.parcelid
            , pred.logerror
            , pred.transactiondate
            , bathroomcnt
            , bedroomcnt
            , calculatedfinishedsquarefeet
            , fips
            , latitude
            , longitude
            , lotsizesquarefeet
            , regionidcity
            , regionidcounty
            , regionidneighborhood
            , regionidzip
            , yearbuilt
            , structuretaxvaluedollarcnt
            , taxvaluedollarcnt
            , landtaxvaluedollarcnt
            , taxamount
        from properties_2017 prop
        inner join predictions_2017 pred on prop.parcelid = pred.parcelid
        where propertylandusetypeid = 261 and structuretaxvaluedollarcnt < 1000000;
        '''
    return pd.read_sql(query, env.get_url('zillow'))


def generate_csv():
    if csv_exist():
        print('- csv already exist')
    else:
        df = get_data_from_zillow()
        df.to_csv('zillow_data.csv')
        print('- zillow_data.csv successfully created')


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


# need
def summarize(df):
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


# function returns missing rows in data set
def nulls_missing_rows(df):
    missing = df.isnull().sum()
    pct_rows_missing = missing / df.shape[0]*100
    number_missing = pd.DataFrame({'number_rows_missing':missing, 'pct_rows_missing': pct_rows_missing})
    return number_missing

# function returns missing columns in data set
def nulls_missing_columns(df):
    missing = df.isnull().sum(axis=1)
    pct_cols_missing = df.isnull().sum(axis=1) / df.shape[1]*100
    rows_missing = pd.DataFrame({'num_cols_missing': missing, 'pct_cols_missing':pct_cols_missing, 
                                'num_rows':missing })
    return rows_missing


def acquire_data():
    print('Acquiring data ...\n')
    generate_csv()
    print('\nData has been acquired')
    df = pd.read_csv('zillow_data.csv')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    return df
    