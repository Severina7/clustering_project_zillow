# The Clustering Project using Zillow data

## *General background about the project*:

> Clustering is an unsupervised machine learning methodology. It is used to group and identify similar observations when we do not have labels that identify the groups.

>It is often a preprocessing or an exploratory step in the data science pipeline

> In this case, I am using clusters to help my exploration, understanding, and modeling of the data.

# Specification

## *Goals*

Use clusters to help your exploration, understanding, and modeling of the Zillow data using the logerror column as a 'target'

## *Audience*
> A data science team. The presentation will consist of a notebook demo of the discoveries I made and work I have done related to uncovering what the drivers of the error in the zestimate is.

## *Deliverables*

**A github repository with the following content**

1. A report (in the form of a detailed, high level notebook)

2. A README explaining what the project is, how to reproduce my work, and my notes from project planning

3. Python modules that automate the data acquisistion and preparation process. These modules are imported and used in your final notebook.

# Data Dictionary

| Feature        | Count                  | Description                                                                                                               |
|----------------|------------------------|---------------------------------------------------------------------------------------------------------------------------|
| latitude       | 59930 non-null float64 | Geographic coordinate that specifies the north–south position of each home on the Earth's surface                         |
| longitude      | 59930 non-null float64 | Geographic coordinate that specifies the east–west position of each home on the Earth's surface                           |
| age            | 59930 non-null int64   | Derived column which indicates the age of the home at the time it was sold                                                |
| square_footage | 59930 non-null float64 | Total square foot of home                                                                                                 |
| lot_size       | 59930 non-null float64 | Total square foot of entire lot                                                                                           |
| full_value     | 59930 non-null float64 | Total actual price of home                                                                                                |
| Los_Angeles    | 59930 non-null int64   | Indicates if the home is in Los Angeles county                                                                            |
| Orange         | 59930 non-null int64   | Indicates if the home is in Orange county                                                                                 |
| Ventura        | 59930 non-null int64   | Indicates if the home is in Ventura county                                                                                |
| logerror       | 59930 non-null float64 | Log of the error between actual home price and estimated home price                                                       |
| lot_cluster    | 59930 non-null int64   | Derived column which indicates if each home is in the cluster containing lot_size, age and full value                     |
| loc_cluster    | 59930 non-null int64   | Derived column which indicates if each home is in the cluster containing latitude, longitude, lot size and square footage |

## *The Pipeline*

### PROJECT PLANNING & README

> Brainstorming ideas, hypotheses, related to how variables might impact or relate to each other, both within independent variables and between the independent variables and dependent variable, and also related to any ideas for new features you may have while first looking at the existing variables and challenge ahead of you.

> In addition: we will summarize our project and goals. We will task out how we will work through the pipeline, in as much detail as we need to keep on track.

### ACQUIRE:

**Goal**: leave this section with a dataframe ready to prepare.

The ad hoc part includes summarizing your data as you read it in and begin to explore, look at the first few rows, data types, summary stats, column names, shape of the data frame, etc.

acquire.py: The reproducible part is the gathering data from SQL.

### PREP:

**Goal**: leave this section with a dataset that is ready to be analyzed. Data types are appropriate, missing values have been addressed, as have any data integrity issues.

The ad hoc part includes plotting the distributions of individual variables and using those plots to identify outliers and if those should be handled (and if so, how), identify unit scales to identify how to best scale the numeric data, as well as finding erroneous or invalid data that may exist in your dataframe.

Some items to consider:

- [X] split data to train/test<br>
- [X] Handle Missing Values
- [X] Handle erroneous data and/or outliers you wish to address
- [X] encode variables as needed
- [X] scale data as needed
- [X] cluster the target variable
- [X] cluster independent variables
- [X] test the significance of and visualize clusters

prep.py: The reproducible part is the handling of missing values, fixing data integrity issues, changing data types, etc.

### DATA EXPLORATION & FEATURE SELECTION

**Goal**: Address each of the questions posed in our planning and brainstorming phase - as time permits. As well as any uncovered that come up during the visual or statistical analysis.

When you have completed this step, we will have the findings from our analysis that will be used in the final notebook, and information to move forward toward building a model.

### MODELING & EVALUATION

**Goal**: use regression models against the results found while clustering to identify a model that performs better than a baseline.

1. Train (fit, transform, evaluate) multiple different models, varying the model type and your meta-parameters.

2. Compare evaluation metrics across all the models, and select the best performing model.

3. Test the final model (transform, evaluate) on your out-of-sample data (the testing data set). Summarize the performance. Interpret your results.

model.py: will have the functions to fit, predict and evaluate the model

# SUMMARY

## *SQL Data Acquisition*

Must use your own env file to access data.

***

## *Technical Skills used*

* Python
* SQL
* Sequel Pro
* Jupyter Notebook
* VS Code
* Various data science libraries (Pandas, Numpy, Matplotlib, Seaborn, Sklearn, etc.)
* Stats (Hypothesis testing, correlation tests)
* Clustering Model (KMeans)
* Regression Models (Linear Regression, Decision Tree Regressor, Random Forest Regressor)

***

## *Executive Summary*

1. Hypothesis and conclusion is unclear. Our derived variables proved useful, but not significantly. 

2. Our main drivers appeared to hover around the overarching geological data and clustering using the selected features associated with those data points. 

3. The linear regression model performed quite poorly. However, the decision tree and random forest regressors did slightly better than baseline.

4. We observed some statistical difference between log error with regards to these features:
    - Longitude/Latitude
    - Lot size
    - Square footage
    - Age of the home
    
It appears either more time is necessary to evaluate the different clustering opportunities within the data. Or that, perhaps, clustering is not the best approach for this data.