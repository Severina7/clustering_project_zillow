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

3. Python modules that automate the data acquisistion and preparation process and any other automated process.

# Data Dictionary

| Feature        | Count                  | Description                                                                                                               |
|----------------|------------------------|---------------------------------------------------------------------------------------------------------------------------|
| latitude       | 38664 non-null float64 | Geographic coordinate that specifies the north–south position of each home on a map  |
| longitude      | 38664 non-null float64 | Geographic coordinate that specifies the east–west position of each home on a map    |
| age            | 38664 non-null int64   | Synthetic column indicating age of the houses at the time it was sold                |
| square_footage | 38664 non-null float64 | Total square foot of houses                                                          |
| lot_size       | 38664 non-null float64 | Area of the lot in square feet                                                       |
| full_value     | 38664 non-null float64 | Total actual price of house                                                          |
| Los_Angeles    | 38664 non-null uint8   | Indicates if the house is in Los Angeles county                                                                            |
| Orange         | 38664 non-null uint8   | Indicates if the house is in Orange county                                                                                 |
| Ventura        | 38664 non-null uint8   | Indicates if the house is in Ventura county                                           |
| logerror       | 38664 non-null float64 | Log of the error between actual house price and estimated home price                  |
| habitable_sqft | 38664 non-null float64   | The square footage of the habitable parts of the house (garage not included i.e.)     |
| building_tax_value| 38664 non-null float64| The assessed value of the land area of the parcel                                |
| parcel_tax_value| 38664 non-null float64 | The square footage of the house including the lot and the building                     |
| land_tax_value  | 38664 non-null float64 | The assessed value of the land area of the parcel                                      |
| age             | 38664 non-null float64 | The age of the houses from the year they were built                                  |
| tax_rate        | 38664 non-null float64 | The quotient of tax amount () and the total tax assessed value of the parcel (parcel_tax_value) |
| value_per_sqft  | 38664 non-null float64 | The quotient of the total tax assessed value of the parcel (parcel_tax_value) and the area of the lot in square feet (lot_sqft)  |

## *Pipeline stages breakdown*

### PLANNING with README

> I decided to write the README first as it will give me a bird's eye view of the project and lead seamslessly my progression. 

> I wrote down the background, the goal, and delivreables of the project. 

> I also thought about the process of importing the data as a first step to understanding what I am dealing with and start asking questions about the preparation and later on, the exploration phase.

>It helps me brainstorm hypothesis and ask the right question on how variables might impact or relate to each other, both within independent variables and between the independent variables and dependent variable, do I need to create new features with the one I have gotten in the dataframe? Writing the README and going through these processes is all done concomitantly but the first two points were done first.


### ACQUIRE:

**Objective**

>Get the right tables through a SQL query as a dataframe and 
write it to a csv file locally in order to avoid long queries. 
Since the data does not change this is safe and the result will be as if I were using the Codeup database.

>This includes displaying and summariziing statiscally parts or the entirety of the data.

>Write my findings in a Takeaways markdown

>I will make a wrangle.py file

### PREP:

**Objective**

>What I'll do
  - Getting rid of nulls and unnecessary column
  - Renaming difficult to read columns
  - Decide whether or not and if yes, how to handled outliers
  - Determine which variable needs scaling and what scaler to use depending on the shape of its distribution plot

>Process:

- [X] Getting rid of nulls and unnecessary column<br>
- [X] Renaming difficult to read columns
- [X] Handle erronous vallues by either imputing and/or dropping them
- [X] Perform a univariate exam of the data
- [X] Split and scale data

>Write my findings in a Takeaways markdown

>I will make a prep.py file

### DATA EXPLORATION & FEATURE SELECTION

**Objectives**

I asked myself the following questions in order to find some insights:

  >Is there a pattern in the data? Where?</font>

  >What features are driving the logerror? What are the most prominent ones?</font>

  >Is the impact of those features meaningful?</font>

  >Write my findings in a Takeaways markdown

>Process:
- [X] cluster the target variable
- [X] cluster independent variables
- [X] test the significance of variables and clusters and visualize clusters

### MODELING & EVALUATION

**Goal**: Use a regression models with clusters to identify the one that performs better than a baseline.

>Train (fit, transform, evaluate) multiple different models.

>Compare evaluation metrics across all the models, and select the best performing model.

>Test the final model (transform, evaluate) on your out-of-sample/test data. 

>Summarize the performance and interpret my results.

>I will make a cluster_model.py file

# SUMMARY

## *SQL Data Acquisition*

An env file is necessary for access to the database (including username and password).

***

## *Technical Skills used*

* Python
* MySQL Workbench
* Jupyter Notebook
* VS Code
* Various data science libraries (Pandas, Numpy, Matplotlib, Seaborn, Sklearn, etc.)
* Stats (Hypothesis testing, correlation tests)
* Clustering Model (KMeans)
* Regression Models (Linear Regression and others if time permits)

***

## *Executive Summary*

>The original variables are not useful in detecting changes in logerror

>The value cluster seemd to be promissing with the lowest set of SSEs but that is not enough to make some conclusions since I was not able to run a model. 

>I planned on using a OLS, LASSOLARS, and a Tweedie Regressor

>Physical position: latitude, longitude, Los_Angeles, Orange, Ventura,

>Value: building_tax_value, parcel_tax_value, land_tax_value, tax_rate, value_per_sqft

>Home features: bathrooms, bedrooms, lot_sqft
    
