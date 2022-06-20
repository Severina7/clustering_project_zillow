# Importing librairies for general use
import pandas as pd
import numpy as np
import scipy.stats as stats
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.impute


# Importing modules for modeling
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

#########################################################

def split_zillow(df):
     
# splits df into train_validate and test using train_test_split(),
# random state is set so that it is replicable
    train_validate, test = train_test_split(df,
                                            test_size=.2,
                                            random_state=174)

# splits train_validate into train and validate using train_test_split(),
# random state is set so that it is replicable
    train, validate = train_test_split(train_validate, 
                                        test_size=.3, 
                                        random_state=174)
    return train, validate, test

def min_max_scaler(train, validate, test):
    '''Takes in train, validate, test then returns their copies 
    (copy set to True) scaled to positive integers
    '''
    scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    validate_scaled = pd.DataFrame(scaler.transform(validate), columns=validate.columns.values).set_index([validate.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train_scaled, validate_scaled, test_scaled