import pandas as pd
import numpy as np


def create_county_cols(df):
    county_df = pd.get_dummies(df.fips)
    county_df.columns = ['LA', 'Orange', 'Ventura']

    df = pd.concat([df, county_df], axis=1)
    df = df.drop(columns=['regionidcounty', 'fips'])
    return df




