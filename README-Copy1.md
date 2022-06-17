# The Clustering Project using Zillow data

## *General background about the project*:

> Clustering is an unsupervised machine learning methodology. It is used to group and identify similar observations when we do not have labels that identify the groups.

>It is often a preprocessing or an exploratory step in the data science pipeline

> In this project, I am using clusters to help my exploration, understanding, and modeling of the data.

# Specification

## *Goals*

Use clusters to help my exploration, understanding, and modeling of the Zillow data using the <ins>logerror</ins> column as a 'target' and determining the best suitable clusters that impact <ins>logerror</ins>

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

## *Pipeline stages breakdown*

### PLANNING with README

> I decided to write the README first as it will give me a bird's eye view of the project and lead seamslessly my progression. 

> I wrote down the background, the goal, and delivreables of the project. 

> I also thought about the process of importing the data as a first step to understanding what I am dealing with and start asking questions about the preparation and later on, the exploration phase.

>It helps me brainstorm hypothesis and ask the right question on how variables might impact or relate to each other, both within independent variables and between the independent variables and dependent variable, do I need to create new features with the one I have gotten in the dataframe? Writing the README and going through these processes is all done concomitantly but the first two points were done first.


### ACQUIRE:

**Objective**

>Get the right tables through a SQL query as a dataframe and write it to a csv file locally in order to avoid long queries. Since the data does not change this is safe and the result will be as if I were using the Codeup database.

>This includes displaying and summariziing statiscally parts or the entirety of the data.

>Write my findings in a Takeaways markdown

>The result is a acquire.py file containing functions to acquire, display and summarize the data.

### PREP:

**Objective**

>Transforme the dataframe to get it in a state that is suitable for analysis. Data types are appropriate, missing values have been addressed, as have any data integrity issues.

>This includes:
  - Getting rid of nulls and unnecessary column
  - Plotting the distributions of individual variables and using those plots to identify outliers
  - Decide whether or not and if yes, how to handled outliers
  - Determine which variable needs scaling and what scler to use depending on the shape of its distribution plot

>Process:

- [X] Handle Missing Values<br>
- [X] split data to train/test
- [X] Handle erroneous data and/or outliers you wish to address
- [X] encode variables as needed
- [X] scale data as needed
- [X] cluster the target variable
- [X] cluster independent variables
- [X] test the significance of and visualize clusters

>Write my findings in a Takeaways markdown

>This process results in a prepare.py file

### DATA EXPLORATION & FEATURE SELECTION

**Objectives**

>I asked myself the following questions in order to find some insights:
  - What is the distribution of each of the variables? This is important as we move forward into testing and modeling.

  - Does the spending score differ across gender?

  - Is there a relationship between spending score and annual income? (Linear or otherwise).

  - Is there a relationship between age and spending score? (Linear or otherwise).

  - If we control for age (by decade), does spending score differ across annual income?

  - If we control for annual income, does spending score differ across age decades?

>Write my findings in a Takeaways markdown

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