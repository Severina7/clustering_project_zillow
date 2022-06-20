import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.stats as stats
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.impute
import os

from env import host, user, password
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans, dbscan


def get_zillow_data():
    '''
    zillow_data() gets the zillow (only properties_2017 table) data from Codeup db, then writes it to a csv file,
    and returns the DF.
    '''
    # Creating a SQL query
    sql_query = '''
                SELECT DISTINCT
      properties_2017.parcelid,
      bathroomcnt,
      bedroomcnt,
      calculatedfinishedsquarefeet,
      fips,
      latitude,
      longitude,  
      lotsizesquarefeet,
      yearbuilt, 
      structuretaxvaluedollarcnt,
      taxvaluedollarcnt, 
      landtaxvaluedollarcnt,
      taxamount,                      
      predictions_2017.logerror,                       
      predictions_2017.transactiondate
   FROM properties_2017
   JOIN predictions_2017 USING(parcelid)
   LEFT JOIN airconditioningtype USING(airconditioningtypeid)
   LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
   LEFT JOIN buildingclasstype USING(buildingclasstypeid)
   LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
   LEFT JOIN propertylandusetype USING(propertylandusetypeid)
   LEFT JOIN storytype USING(storytypeid)
   LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)
   WHERE
      latitude IS NOT NULL
      AND longitude IS NOT NULL
      AND transactiondate BETWEEN '2017-01-01' AND '2017-12-31';
                '''
    
    # Reading in the DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))
    return df

def get_local_zillow():
    '''
    get_local_zillow reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DF.
    '''
    if os.path.isfile('houses.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('houses.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = get_zillow_data()
        
        # Cache data
        df.to_csv('houses.csv')
        
    return df


def handle_nulls(df):
    '''
    Transforms data brought in from SQL to handle nulls 
    Add calculated fields
    '''
    # Set nulls to be the median

    median = df.calculatedfinishedsquarefeet.median()
    df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.fillna(median)

    median = df.lotsizesquarefeet.median()
    df.lotsizesquarefeet = df.lotsizesquarefeet.fillna(median)

    median = df.taxvaluedollarcnt.median()
    df.taxvaluedollarcnt = df.taxvaluedollarcnt.fillna(median)

    median = df.taxamount.median()
    df.taxamount = df.taxamount.fillna(median)

    median = df.structuretaxvaluedollarcnt.median()
    df.structuretaxvaluedollarcnt = df.structuretaxvaluedollarcnt.fillna(median)

    # Use the mode for nulls

    mode = df.yearbuilt.mode()
    df.yearbuilt = df.yearbuilt.fillna(mode)

    mode = df.landtaxvaluedollarcnt.mode()
    df.landtaxvaluedollarcnt = df.landtaxvaluedollarcnt.fillna(mode)

    # drop all remaining rows with null values
    df = df.dropna()
    return df


def prepare_zillow(df):
    '''
    Takes in a df and returns the same df with: 
    Boolean columns indicating which county each observation is in,
    Column indicating age of home
    '''

    # create df with counties as booleans
    county_df = pd.get_dummies(df.fips)
    county_df.columns = ['Los_Angeles', 'Orange', 'Ventura']
    df = pd.concat([df, county_df], axis = 1)


    # calculate age of home
    df['age'] = 2017 - df.yearbuilt
    df.drop(columns=['yearbuilt'], inplace=True)
    return df


def summarize(df):
    '''sunnarize takes in a dataframe and  returns summarized information about the dataframe'''
    print('Shape: {}'.format(df.shape), '\n\n##########\n\n')
    print('Info')
    df.info()
    print('\n\n##########\n\n')
    print('Statistical description\n')
    print(df.describe(include='all').T)