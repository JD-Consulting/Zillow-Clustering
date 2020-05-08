# JD-Consulting Zillow Clustering Project

## Purpose
Can we improve the zillow logerror?

## Deliverables
1. Report (jupyter notebook) answering the question:
    - "Can we reduce the Zillow logerror?"
    - Clear steps taken to arrive at a conclusion. 
    - End of notebook will be the report.
2. Presentation: [Link] ()
    - Illustrates how the notebook
        - Include the features being used
        - Include whether or not the model works better then Zillow's model
3. Multiple .py files
    - aqcuire.py
    - model.py
    - prepare.py
    - preprocessiing.py
    - set_counties.py
    - summerize.py
     
4. Github Repository:
    - Readme (this file)
    - Final Jupyter notebook walking through the pipeline
    - .py files with all functions necessary to reproduce the model


# Pipeline

## Planning
- Goal: identify 
    
## Acquire Data
- an acquired dataframe
    - Created a file called acquire.py with the following necessary functions to generate this dataframe from SQL
      - calls acquire_data()
      - creates a csv file of the dataframe
## Data Preparation
- prepared the dataframe using the functions listed below, found in prepare.py 
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

|   	| **ORIGINAL FEATURES**               	|                                                                                               	|
|---	|-------------------------------------	|-----------------------------------------------------------------------------------------------	|
|   	| parcelid                            	| identification: numerical id assigned to a parcel region                                      	|
|   	| logerror                            	| difference between the actual sale price and the predicted sales pri                          	|
|   	| transactiondate                     	| date a transaction took place                                                                 	|
|   	| bathroomcnt                         	| number of bathrooms a structure houses                                                        	|
|   	| bedroomcnt                          	| number of bedrooms a structure houses                                                         	|
|   	| calculatedfinishedsquarefeet        	| calculated square feet of a completed structure                                               	|
|   	| county                              	| name: names of the county associated with the property                                        	|
|   	| latitude                            	| measurement: angular distance of location, north or south of the equator                      	|
|   	| longitude                           	| measurement: angular distance of location, east or west of the meridian at Greenwich, England 	|
|   	| lotsizesquarefeet                   	| measurement: square foot size of the properties land                                          	|
|   	| regionidcity                        	| identification: numerical id assigned                                                         	|
|   	| regionidzip                         	| identification: numerical zip code                                                            	|
|   	| yearbuilt                           	| date: year the structure was completed                                                        	|
|   	| structuretaxvaluedollarcnt          	| monetary: tax value of the structure minus the land value                                     	|
|   	| taxvaluedollarcnt                   	| monetary: tax value of the structure and land combined                                        	|
|   	| landtaxvaluedollarcnt               	| monetary: tax value of the land minus the structure value                                     	|
|   	| taxamount                           	| monetary: dollar amount of taxes                                                              	|
|   	|                                     	|                                                                                               	|
|   	| **CREATED FEATURES:**               	|                                                                                               	|
|   	| age                                 	| numerical: how old the house is since 2017 ~ 2017 - yearbuilt                                 	|
|   	| LA                                  	| county_name: assigned a 1 if True, otherwise 0                                                	|
|   	| Orange                              	| county_name: assigned a 1 if True, otherwise 0                                                	|
|   	| Ventura                             	| county_name: assigned a 1 if True, otherwise 0                                                	|
|   	| bed_bath_ratio                      	| percentage: bathroomcnt / bedroomcnt                                                          	|
|   	| tax_rate                            	| percentage: taxamount / taxvaluedollarcnt                                                     	|
|   	| *SCALED*                            	| values scaled to a float between 0 and 1                                                      	|
|   	| scaled_bathroomcnt                  	| scaled count: bedroom count scaled                                                            	|
|   	| scaled_calculatedfinishedsquarefeet 	| scaled measurement: calculated square feet of a finished structure scaled                     	|
|   	| scaled_lotsizesquarefeet            	| scaled measurement: size of the land scaled                                                   	|
|   	| scaled_taxvaluedollarcnt            	| scaled monetary: tax value of the structure and land combined scaled                          	|
|   	| *LOG*                               	| *property cluster assignment*                                                                 	|
|   	| log_cluster                         	| clustered by longitude and latitude                                                           	|
|   	| lotsizesquaredfeet_cluster          	| clustered by square foot size of the properties land                                          	|
|   	| money_bed_cluster                   	| clustered by tax value and bedroom count scaled and logerror                                  	|
|   	| sqft_cluster                        	| clustered by calculated square feet scaled and logerror                                       	|
|   	| tax_rate_cluster                    	| clustered by tax rate                                                                         	|
|   	| *PREDICTIONS*                       	|                                                                                               	|
|   	|                                     	|                                                                                               	|
|   	|                                     	|                                                                                               	|


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


