import pandas as pd
import numpy as np


def create_county_cols(df):
    county_df = pd.get_dummies(df.fips)
    county_df.columns = ['LA', 'Orange', 'Ventura']
    county = []
    for row in df['fips']:
        if row == 6037:
            county.append('Los Angelas')
        elif row == 6059:
            county.append('Orange')
        elif row == 6111:
            county.append('Ventura')
        
    df['county'] = county        
    df = pd.concat([df, county_df], axis=1)
    return df




