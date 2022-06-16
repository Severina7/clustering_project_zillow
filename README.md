# The Clustering Project using Zillow data

## Project Specifications

  - This project will contain a clearly named final notebook, with profuse markdown. This notebook will be what you present and should contain plenty of markdown documentation and cleaned up code.
  - A README that explains what the project is, how to reproduce you work, and your notes from project planning.
  - A Python module or modules that automate the data acquisistion and preparation process. These modules should be imported and used in your final notebook.
## Business Goals
  - Construct an ML Regression model that predict propery tax assessed values ('taxvaluedollarcnt') of Single Family Properties using attributes of the properties.
  - Find the key drivers of property value for single family properties.
  - Deliver a report that the data science team can read through and replicate, understand what steps were taken, why and what the outcome was.
  - Make recommendations on what works or doesn't work in prediction these homes' values.
## Audience
  - My (virtual) customer/end user is the Zillow data science team.
## Project Deliverables
### A github repo containing the following:
  - A Readme (.md) file
  
  - A Final Report (.ipynb)
    
  - Acquire & Prepare Modules (.py)

  - My project will also have 1+ non-final Notebooks (.ipynb) created while working on the project
### A final presentation

## Project Context
  - Dataset used came from Codeup database
  - The project is the second modeling project and is using regression models and the data processing that goes along with it.

## Data Dictionary
- Target data: taxvaluedollarcnt renamed tax_value
    * Content 52441 non-null values
    * Data type: float64
    * Definition: It is also called the Assessed value and is the dollar value assigned to a home or other piece of real estate for property tax purposes.
- Features:
    bedroomcnt renamed bedrooms, bathroomcnt renamed bathrooms, calculatedfinishedsquarefeet renamed indoor_sqft
    * bedrooms:
        - Content: 52442 non-null values
        - Data type: float64
        - Definition: This designates the number of bedrooms in each property
    * bathrooms:
        - Content: 52442 non-null values
        - Data type: float64
        - Definition: This designates the number of bathrooms in each property
    * indoor_sqft:
        - Content: 52360 non-null values
        - Data type: float64
        - Definition: this is the calculated total finished living area of the home
Size of the file: 2.8+ MB (safe for export to github)

## Initial Hypotheses
### First Hypothesis
    - Null hypothesis: $H_{0}$: there is no correlation between the number of bedrooms and the tax value of the properties
    - Alternative hypothesis: $H_{A}$: there is a correlation between the number of bedrooms and the tax value of the properties.

### Second Hypothesis
    - Null hypothesis: $H_{0}$: there is no correlation between the number of bathrooms and the tax value of the properties
    - Alternative hypothesis: $H_{A}$: there is a correlation between the number of bathrooms and the tax value of the properties.

### Third Hypothesis
    - Null hypothesis: $H_{0}$: there is no correlation between the indoor square footage and the tax value of the properties
    - Alternative hypothesis: $H_{A}$: there is a correlation between the indoor square footage and the tax value of the properties.

## Executive Summary - Conclusions & Next Steps
    - The goal of this project was to build a model that could predict propery tax assessed values ('taxvaluedollarcnt') of Single Family Properties using attributes of the properties.
    - Only Regression models were used ()
    - Findings:
        * The best model with the features used is the Decision Tree model.
        * Its accuray is 76%  compared to the baseline at 73%
        * Some features prevent churn and are worth examining

## Pipeline stages breakdown
  ### General Plan

    - Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
    - Acquire data from the Codeup Database and create a function to automate this process.
    - Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, add it to the Aquire function together to form a wrangle.py file.
    - Prepare data in Final Report Notebook by importing and using the funtion.
    - Clearly define three hypotheses, produce charts to observe the data, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
    - Establish a baseline RMSE and document well.
    - Train three different regression models.
    - Evaluate models on train and validate datasets.
    - Choose the model with that performs the best and evaluate that single model on the test dataset.
    - Document conclusions, takeaways, and next steps in the Final Report Notebook.

  ### General Plan -> Acquire
    I have created a function <font color = 'brown'>get_connection</font> that uses login info from env.py file to access Codeup database.
    It returns a string that can be used in another function <font color = 'brown'>wrangle_zillow</font> to return a dataframe from the SQL database
  
  ### General Plan -> Acquire -> Prepare
    * Main question: What can prevent me from having data without nulls, that is relevant to my modeling, that is compatible with my models?
    - Check for null values and drop them if they are not in great numbers (for example more than 15% of the data. This will also depend on the size of the data)
    - Check for hard to read columns names to rename them appropriately
    - Check for irrelevant columns (that won't impact the analysis and the modeling) and drop them
    - Check for incompatible data types (example: data should be int64 but is object or float)
    - Do a univariate exploration through charts and columns observation

  ### General Plan -> Acquire -> Prepare -> Explore
    **I will scale the data but assign the scaled data to a different variable tahn train and explore my train data with the train dataframe**
    - I will use Standard, Robust, and Quantile scalers
    - I will perform an exploration of the data to determine which columns are potential drivers of the tax value
    - For the exploration I will use appropriate charts and statistical tests to show that there is or there is not a correlation between the independent variables (bedrooms, bathrooms, and square footage) and tax value.   

  ### General Plan -> Acquire -> Prepare -> Explore -> Model
    - Examine the shape of the tax value column to determine what model would work best
    - Determine a baseline that will be used to compare the the models I will be creating
    - Create an OLS, a LassoLars with alpha=3, and a Tweedie Regressor with power=1 & 3 and alpha=3
    - Run the models on validate as well
    - Compute an RMSE for each model and its validate and compare them all
    - Choose the best model and run it on the test dataset

  ### General Plan -> Acquire -> Prepare -> Explore -> Model -> Deliver
    - Introduce myself and my project goals at the beginning of my notebook walkthrough.
    - Summarize my findings at the beginning like I would for an Executive Summary. (Don't throw everything out that I learned from Storytelling) .
    - Walk my audience through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.)
    - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.

  ## To Reproduce my project
    You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.
    - Read this README.md
    - Download he wrangle.py file
    - Add your own env file to your directory. (user, password, host)
    - Run the final_report.ipynb notebook