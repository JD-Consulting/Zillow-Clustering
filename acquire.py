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
    '''
    
    '''
    if csv_exist():
        print('- csv already exist')
    else:
        df = get_data_from_zillow()
        df.to_csv('zillow_data.csv')
        print('- zillow_data.csv successfully created')


def acquire_data():
    '''
    Returns a dataframe:
    
    - acquire_data()
        - call generate_csv function to generate a csv file of the SQL data
        - reads the csv to a dataframe and returns it
    
    - generate_csv()
        - calls csv_exit to determines if a local csv file exist
            - if a csv file exist, prints a message
            - if a csv file does not exist
                - calls get_data_from_zillow()
                - writes dataframe to csv
                
    - csv_exist()
        - uses os.path.isfile
        - returns a boolean 
    
    - get_data_from_zillow()
        - acquires data from SQL database
        - return to generate_csv as a dataframe
    
    
    '''
    print('Acquiring data ...\n')
    generate_csv()
    print('\nData has been acquired')
    df = pd.read_csv('zillow_data.csv')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    return df
    