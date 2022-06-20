# Importing librairies for general use and visuals
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.stats as stats
import sklearn.preprocessing
import sklearn.model_selection

# Importing modules for modeling
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

def elbow_method(variables):
    cluster_vars = variables

    ks = range(2,10)
    sse = []
    for k in ks:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(cluster_vars)

        # inertia: Sum of squared distances of samples to their closest cluster center.
        sse.append(kmeans.inertia_)

    print(pd.DataFrame(dict(k=ks, sse=sse)))

    plt.plot(ks, sse)
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.title('The Elbow Method to find the optimal k')
    plt.show()


def get_clusters(k, cluster_vars, cluster_name, train_scaled, validate_scaled, test_scaled):
    """
    get_clusters takes in scaled train, validate, test, k for nuber of clusters,
    cluster_vars for number and names of variables in a cluster
    cluster_name for the name of the cluster which are setup in the cells above
    takes in k and returns the kmeans fitted object, 
    dataframe of the train clusters with their observations, validate and
    test clusters and their observations, and a df of the number 
    of observations per cluster on train. 
    """
    
    # find clusters
    kmeans = KMeans(n_clusters=k, random_state = 174)
    train_array = kmeans.fit_predict(train_scaled[cluster_vars])
    validate_array = kmeans.fit_predict(validate_scaled[cluster_vars])
    test_array = kmeans.predict(test_scaled[cluster_vars])
    
    # create df of cluster id with each observation
    train_clusters = pd.DataFrame(train_array, columns = [cluster_name], index = train_scaled.index)
    validate_clusters = pd.DataFrame(validate_array, columns = [cluster_name], index = train_scaled.index)
    test_clusters = pd.DataFrame(test_array, columns = [cluster_name], index = test_scaled.index)
    
    # output number of observations in each cluster
    cluster_counts = train_clusters[cluster_name].value_counts()
    
    return train_clusters, validate_clusters, test_clusters, cluster_counts