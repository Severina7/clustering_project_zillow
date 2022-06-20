import pandas as pd 
import numpy as numpy
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

import warnings
warnings.filterwarnings("ignore")


def multi_frequency(df,vars):
    '''multi_frequency takes a dataframe in *arg 
    and a *kwarg in the form of a list of columns,
    drops any duplicated entry and return a dataframe
    with the count and the frequency of the data
    '''
    df.drop_duplicates(keep='first')
    frequency=df[vars].isnull().sum()
    percentage=df[vars].isnull().sum()*100/(len(df))
    df=pd.concat([frequency,percentage], axis=1, keys=['num_rows_missing', 'pct_rows_missing'])
    return df
    
    
def handle_missing_values(df):
    '''Takes in a df and impute values with KNN (n_neighbors=1),
    then drop the rest of the null values
    '''
    imputer = KNNImputer(n_neighbors=1)
    imputer.fit_transform(df[['lotsizesquarefeet',
                                  'yearbuilt',
                                  'structuretaxvaluedollarcnt',
                                  'calculatedfinishedsquarefeet']])
    df = df.dropna()
    return df



def handle_missing_values2(df):
    '''
    Takes in a df and impute values with KNN (n_neighbors=2),
    then drop the rest of the null values
    '''
    imputer = KNNImputer(n_neighbors=2)
    imputer.fit_transform(df[['lotsizesquarefeet',
                                  'yearbuilt',
                                  'structuretaxvaluedollarcnt',
                                  'calculatedfinishedsquarefeet']])
    df = df.dropna()
    return df

def prepare_zillow(df):
    '''
    Takes in the df and changes county numbers
    to a boolean column,  indicating county names 
    for properties and another one the age
    '''
# Creating df with counties as booleans
    counties = pd.get_dummies(df.fips)
    counties.columns = ['Los_Angeles', 'Orange', 'Ventura']
    df = pd.concat([df, counties], axis = 1)
# Dropping columns
    df.drop(columns=['transactiondate'], inplace=True)
    df.drop(columns=['fips'], inplace=True)
    df.drop(columns=['parcelid'], inplace=True)
# Calculating age of houses
# (will be useful when scaling but also maybe clustering as a 'new' feature)
    df['age'] = 2017 - df.yearbuilt
    df.drop(columns=['yearbuilt'], inplace=True)
# Renaming columns
    cols_to_rename = {
    'calculatedfinishedsquarefeet': 'habitable_sqft',
    'taxvaluedollarcnt': 'parcel_tax_value',
    'bedroomcnt': 'bedrooms',
    'bathroomcnt': 'bathrooms',
    'taxamount': 'tax_amount',
    'lotsizesquarefeet': 'lot_sqft',
    'structuretaxvaluedollarcnt': 'building_tax_value',
    'landtaxvaluedollarcnt': 'land_tax_value',
}
    df = df.rename(columns=cols_to_rename)
    return df


def tax_rate(df):
    '''    
    tax_rate takes in a dataframe and creates a new column
    tax_rate from tax_amount and parcel_tax_value, drops the tax_amount column
    and returns a dataframe
    '''
    
    df['tax_rate'] = df.tax_amount / df.parcel_tax_value
    df.drop(['tax_amount'], axis=1, inplace=True)
    return df


def value_per_sqft(df):
    '''    
    value_per_sqft takes in a dataframe and creates a new column
    value_per_sqft from lot_sqft and parcel_tax_value, drops the tax_amount column
    and returns a dataframe
    '''
    
    df['value_per_sqft'] = df.parcel_tax_value / df.lot_sqft
    return df