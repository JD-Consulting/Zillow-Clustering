# JD-Consulting Zillow Clustering Project

## Purpose
Can we improve the zillow logerror?

Some questions I have include:

1.  
2. 
3. 
4. 


## Deliverables
1. Report (jupyter notebook) answering the question:
    - "Why are our customers churning?"
    - I want to see the analysis you did to answer my questions and lead to your findings. Please clearly call out the **questions** and **answers** you are analyzing. 
    - End of notebook will produce .csv file with the customer_id, probability of churn, and the prediction of churn (1=churn, 0=not_churn).
2. Presentation: [Link] ()
    - Illustrates how the notebook
        - Include the features being used
        - Include how likely your model is to predict
3. Multiple .py files with their associated notebooks
    - aqcuire.py
    - model.py
    - prepare.py
    - preprocessiing.py
    - set_counties.py
    - summerize.py
     
4. Github Repository: [Link](https://github.com/JD-Consulting/Zillow-Clustering)
    - Readme (this file)
    - Final Jupyter notebook walking through the pipeline
    - .py files with all functions necessary to reproduce the model

# Pipeline


## Planning

## Acquire Data
- Goal: a prepared dataframe
    - Create a file called acquire.py with all necessary functions to generate this dataframe from SQL

## Data Preparation
- Goal: prepared dataframe using the functions listed below, found in prepare.py 
    - Split data into train/test/validate
        - split_my_data(df, test_percentage, validate_percetage)
    - Handle missing & null values
        - handle_missing_values(df, prop_required_column, prop_required_row)
    - Handle outliers
        - outlier detection with IQR as a filter
    - Scale data
        - scale_data(df)
    - New features: 
        1. bedroom count to bathroom count ratio
            - zillow_single_unit_prop(df)
                - bed_bath_ratio = bathroomcnt / bedroomcnt
        2. tax rate 
            - zillow_single_unit_prop(df)
                - tax_rate = taxamount / taxvaluedollarcnt 
        3. create three columns for each fips
            - create_county_cols(df)

- Goal: a jupyter notebook that explores the above issues, documents plans to address them, and uses the functions 
    - zillow_clustering.ipynb


- Goal: Data Dictionary

|      	| **ORIGINAL FEATURES**        	|                                                                                               	|
|------	|------------------------------	|-----------------------------------------------------------------------------------------------	|
| i    	| parcelid                     	| identification: numerical id assigned to a parcel region                                      	|
| ii   	| logerror                     	| difference between the actual sale price and the predicted sales pri                          	|
| iii  	| transactiondate              	| date a transaction took place                                                                 	|
| iv   	| bathroomcnt                  	| number of bathrooms a structure houses                                                        	|
| v    	| bedroomcnt                   	| number of bedrooms a structure houses                                                         	|
| vi   	| calculatedfinishedsquarefeet 	| calculated square feet of a completed structure                                               	|
| vii  	| latitude                     	| measurement: angular distance of location, north or south of the equator                      	|
| viii 	| longitude                    	| measurement: angular distance of location, east or west of the meridian at Greenwich, England 	|
| ix   	| lotsizesquarefeet            	| measurement: square foot size of the properties land                                          	|
| x    	| regionidcity                 	| identification: numerical id assigned                                                         	|
| xi   	| regionidzip                  	| identification: numerical zip code                                                            	|
| xii  	| yearbuilt                    	| date: year the structure was completed                                                        	|
| xiii 	| structuretaxvaluedollarcnt   	| monetary: tax value of the structure minus the land value                                     	|
| xiv  	| taxvaluedollarcnt            	| monetary: tax value of the structure and land combined                                        	|
| xv   	| landtaxvaluedollarcnt        	| monetary: tax value of the land minus the structure value                                     	|
| xvi  	| taxamount                    	| monetary: dollar amount of taxes                                                              	|
|      	|                              	|                                                                                               	|
|      	| **CREATED FEATURES:**        	|                                                                                               	|
| i    	| LA                           	| county_name: assigned a 1 if True, otherwise 0                                                	|
| ii   	| Orange                       	| county_name: assigned a 1 if True, otherwise 0                                                	|
| iii  	| Ventura                      	| county_name: assigned a 1 if True, otherwise 0                                                	|
| iv   	| bed_bath_ratio               	| percentage: bathroomcnt / bedroomcnt                                                          	|
| v    	| tax_rate                     	| percentage: taxamount / taxvaluedollarcnt                                                     	|



## Data Exploration
    1.Are there any features that improve the logerror
        - Location, that is, latitude and longitude
        - Size (finished square feet)
        - Location and size

## Modeling
- Goal: Feature Selection
    - Remove any variables that seem to provide limited to no additional information
- Goal: Train (fit, transform, evaluate) multiple different models
- Goal: Compare evaluation metrics across all the models, and select the best performing model.
- Goal: Test the final model (transform, evaluate) on your out-of-sample data (the testing data set). 
    - Summarize the performance. 
    - Interpret your results.








