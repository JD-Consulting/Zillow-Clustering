import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def split_my_data(df, test_pct, validate_pct):
    '''
    Takes in df, train_pct,  validate_pct and returns 3 items:
    
        - train:    larger portion of the dataframe for training the model
        - test:     smaller portion of the dataframe that has not being fit 
        - validate: smaller portion of the dataframe that can be used to test different models
        
    When using this function, in order to have usable datasets, be sure to call it thusly:
    train, test, validate = split_my_data(df, train_pct, validate_pct)
    '''
    train, test = train_test_split(df, test_size = test_pct, random_state = 7)
    validate, test = train_test_split(test, test_size = validate_pct, random_state = 7)
    
    return train, test, validate


def save_train_test_validate(train, test, validate):
    '''
    Return train and validate dataframes:
    
        - train, test, and validate dataframes are saved to csv files
        - train and validate are read from those csv files
          and returned
              - train.csv
              - validate.csv
        
        - for test dataframe see get_test()
    '''
    train.to_csv('train.csv')
    test.to_csv('test.csv')
    validate.to_csv('validate.csv')
    print('\n- train, test, validate csv files created\n')
    train = pd.read_csv('train.csv')
    validate = pd.read_csv('validate.csv')
    train.drop(columns=('Unnamed: 0'), inplace=True)
    validate.drop(columns=('Unnamed: 0'), inplace=True)
    
    return train, validate


def get_test():
    '''
    Return test dataframe from csv file
    
        - test.csv
    '''
    test = pd.read_csv('test.csv')
    test.drop(columns=('Unnamed: 0'), inplace=True)
    
    return test



# SCALING


    






